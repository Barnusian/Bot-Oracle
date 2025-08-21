*My hopefully idiot-proof guide to getting this set up on a new Pi.*

To start, SSH in and run the following to upgrade all packages:

```
sudo apt update
sudo apt upgrade
```

Install pip to install python libraries:

```
sudo apt install python3-pip -y
```

Install git to pull code from github:

```
sudo apt install git -y
```

Or install both with one command:

```
sudo apt install python3-pip git -y
```

Pull repo with:

```
git clone https://github.com/Barnusian/Bot-Oracle
```

cd into /Bot-Oracle directory and set up virtual environment:

```
python -m venv .venv
```
(use ".venv" over ".env" to avoid confusion with an environment variables file)#

##### Auto-activate the Environment:

Install helper tool:

```
sudo apt install direnv
```

Tell terminal to use it:

```
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
```

Reload settings:

```
source ~/.bashrc
```

cd into /ReceiptWriter directory, create .envrc file that tells direnv what to do, and allow direnv:

```
echo 'source .venv/bin/activate' > .envrc
direnv allow
```
(make sure environment name is same as before, i.e. ".venv")

Environment will auto-activate when in directory now.

### Install requirements.txt

```
pip install -r requirements.txt
```

### Install libusb for USB support

```
sudo apt install libusb-1.0-0
```

Create udev rule to enable USB access for all users:

```
echo 'SUBSYSTEM=="usb", ATTR{idVendor}=="04b8", ATTR{idProduct}=="0202", MODE="0666"' | sudo tee /etc/udev/rules.d/99-escpos.rules
```

Reload udev:

```
sudo udevadm control --reload-rules
sudo udevadm trigger
```
