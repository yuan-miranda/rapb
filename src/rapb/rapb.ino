int relayPin = 2; // D2 pin on arduino connected to the relay module's IN pin

void setup() {
  pinMode(relayPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    // Turn off the relay
    if (command == '1') {
      digitalWrite(relayPin, LOW);

      // Turn on the relay
    } else if (command == '0') {
      digitalWrite(relayPin, HIGH);
      
      // Get the relay status
    } else if (command == '2') {
      bool currentState = digitalRead(relayPin);
      
      if (!currentState) {
        Serial.println("charger turned on");

      } else {
        Serial.println("charger turned off");
      }
    }
  }
}