const int buttonPin = 2; // button wired between D2 and GND
bool buttonState = HIGH;
bool lastButtonState = HIGH;
unsigned long lastDebounceTime = 0;
unsigned long debounceDelay = 50;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP); // Assumes button connected to GND
  pinMode(13, OUTPUT); // LED on 13
  Serial.begin(9600);
}

void loop() {
  int reading = digitalRead(buttonPin);

  if (reading != lastButtonState) {
    lastDebounceTime = millis();
  }

  if ((millis() - lastDebounceTime) > debounceDelay) {
    if (reading != buttonState) {
      buttonState = reading;
      if (buttonState == LOW) {
        Serial.println("BTN_1");
        digitalWrite(13, HIGH);
        delay (1000);
        digitalWrite(13, LOW);
      }
    }
  }

  lastButtonState = reading;
}