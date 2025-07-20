import serial
import subprocess
import threading
import time
import logging
from queue import Queue, Empty
from pathlib import Path

# ------------------------------
# Config
# ------------------------------
SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600
EVENT_COOLDOWN = {
    "BTN_1": 1,
    "BTN_2": 1,
    "BTN_3": 1,
}
EVENT_MAP = {
    "BTN_1": ["Scripts/print_message.py"],
    "BTN_2": ["Scripts/LEDs/ledTest.py"],
    "BTN_3": [],
}

# ------------------------------
# Setup Logging
# ------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
log_path = BASE_DIR / "logs"
log_path.mkdir(exist_ok=True)
logging.basicConfig(
    filename=log_path / "bot_oracle.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

# ------------------------------
# Globals
# ------------------------------
event_queue = Queue()
resource_locks = {
    "printer": threading.Lock(),
    "leds": threading.Lock()
}
last_triggered = {}

# ------------------------------
# Serial Listener
# ------------------------------
def serial_listener():
    while True:
        try:
            with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
                logging.info(f"Connected to {SERIAL_PORT}")
                while True:
                    try:
                        line = ser.readline().decode('utf-8').strip()
                    except UnicodeDecodeError:
                        logging.warning("Received undecodable serial data.")
                        continue
                    if line:
                        logging.info(f"Received: {line}")
                        event_queue.put(line)
        except (serial.SerialException, OSError) as e:
            logging.warning(f"Serial error: {e}. Retrying in 5 seconds...")
            time.sleep(5)

# ------------------------------
# Event Handler
# ------------------------------
def event_handler():
    while True:
        try:
            event = event_queue.get(timeout=1)
            if not is_on_cooldown(event):
                launch_scripts(event)
                last_triggered[event] = time.time()
            else:
                logging.info(f"Ignored {event} due to cooldown.")
        except Empty:
            continue

# ------------------------------
# Cooldown Check
# ------------------------------
def is_on_cooldown(event):
    if event not in last_triggered:
        return False
    elapsed = time.time() - last_triggered[event]
    return elapsed < EVENT_COOLDOWN.get(event, 0)

# ------------------------------
# Launch Scripts
# ------------------------------
def launch_scripts(event):
    scripts = EVENT_MAP.get(event, [])
    for script in scripts:
        lock = get_required_lock(script)
        if lock:
            threading.Thread(target=run_with_lock, args=(script, lock), daemon=True).start()
        else:
            threading.Thread(target=run_script, args=(script,), daemon=True).start()

def get_required_lock(script):
    # Simple hardcoded example: adjust as needed
    if "print" in script:
        return resource_locks["printer"]
    elif "led" in script:
        return resource_locks["leds"]
    return None

def run_with_lock(script, lock):
    with lock:
        run_script(script)

def run_script(script_path):
    try:
        logging.info(f"Running script: {script_path}")
        subprocess.run(["python3", script_path], check=True)
        logging.info(f"Finished: {script_path}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running {script_path}: {e}")

# ------------------------------
# Main Entry Point
# ------------------------------
if __name__ == "__main__":
    logging.info("Bot-Oracle starting...")
    threading.Thread(target=serial_listener, daemon=True).start()

    try:
        from Scripts.LEDs.clear_matrix import clear_display
        clear_display()
        logging.info("LED matrix cleared successfully")
    except Exception as e:
        logging.warning(f"Failed to clear LED matrix: {e}")

    event_handler()  # blocks forever