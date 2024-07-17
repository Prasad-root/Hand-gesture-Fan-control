int pwm = 9;

void setup() {
  Serial.begin(9600);

  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(13, OUTPUT);
  pinMode(7, OUTPUT); // Pin to control motor driver

  digitalWrite(7, LOW); // Ensure motor is initially off
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    Serial.println(command);
    
    switch (command) {
      case 'T':
        // Turn on the fan at full speed
        analogWrite(pwm, 255); // Full speed
        digitalWrite(7, HIGH);

        digitalWrite(13, HIGH);
        digitalWrite(12, HIGH);
        digitalWrite(11, HIGH);
        break;
      case '1':
        // Speed 1
        analogWrite(pwm, 100); // Set a lower PWM value for speed 1
        digitalWrite(7, HIGH);

        digitalWrite(13, LOW);
        digitalWrite(12, LOW);
        digitalWrite(11, HIGH);
        digitalWrite(10, LOW);
        break;
      case '2':
        // Speed 2
        analogWrite(pwm, 150); // Set a mid PWM value for speed 2
        digitalWrite(7, HIGH);

        digitalWrite(13, LOW);
        digitalWrite(12, HIGH);
        digitalWrite(11, LOW);
        digitalWrite(10, LOW);
        break;
      case '3':
        // Speed 3
        analogWrite(pwm, 255); // Set a higher PWM value for speed 3
        digitalWrite(7, HIGH);

        digitalWrite(13, HIGH);
        digitalWrite(12, LOW);
        digitalWrite(11, LOW);
        digitalWrite(10, LOW);
        break;
      default:
        // Turn off the fan
        analogWrite(pwm, 0);
        digitalWrite(7, LOW);
        digitalWrite(13, LOW);
        digitalWrite(12, LOW);
        digitalWrite(11, LOW);
        break;
    }
  }
}
