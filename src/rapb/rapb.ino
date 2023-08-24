int relayPin = 2;

void setup() {
  pinMode(relayPin, OUTPUT);  // D2 pin on arduino connected to the relay module IN pin
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    // Turn off the relay
    if (command == '0') {
      digitalWrite(relayPin, HIGH);

      // Turn on the relay
    } else if (command == '1') {
      digitalWrite(relayPin, LOW);

      // Get the relay status
    } else if (command == '2') {
      bool currentState = digitalRead(relayPin);
      
      if (!currentState) {
        Serial.println("-          charger turned on");

      } else {
        Serial.println("-          charger turned off");
      }
    }
  }
}