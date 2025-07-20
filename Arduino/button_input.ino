struct Button {
  int pin;
  const char* label;
  bool state;
  bool lastState;
  unsigned long lastDebounce;
};

unsigned long debounceDelay = 50;
const int ledPin = 13;

// Add more buttons here!
Button buttons[] = {
  {2, "BTN_1", HIGH, HIGH, 0},
  {3, "BTN_2", HIGH, HIGH, 0},
  {4, "BTN_3", HIGH, HIGH, 0},
};

const int buttonCount = sizeof(buttons) / sizeof(buttons[0]);

void setup() {
  pinMode(ledPin, OUTPUT); // LED on pin 13
  Serial.begin(9600);

  for (int i = 0; i < buttonCount; i++) {
    pinMode(buttons[i].pin, INPUT_PULLUP);
  }
}

void loop() {
  for (int i = 0; i < buttonCount; i++) {
    Serial.print("Pin ");
    Serial.print(buttons[i].pin);
    Serial.print(": ");
    Serial.println(digitalRead(buttons[i].pin));

    int reading = digitalRead(buttons[i].pin);

    if (reading != buttons[i].lastState) {
      buttons[i].lastDebounce = millis();
    }

    if ((millis() - buttons[i].lastDebounce) > debounceDelay) {
      if (reading != buttons[i].state) {
        buttons[i].state = reading;
        if (buttons[i].state == LOW) {
          Serial.println(buttons[i].label);
          digitalWrite(ledPin, HIGH); // These 3 lines turn the LED on and off when a button is pressed
          delay(1000);
          digitalWrite(ledPin, LOW);
        }
      }
    }

    buttons[i].lastState = reading;
  }
}