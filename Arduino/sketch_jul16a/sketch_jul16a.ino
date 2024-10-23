#include <ESP8266WiFi.h>

const char* ssid = "HUAWEI Y3 2017";
const char* password = "prasad11613";

const int pwm = D1;
const int motor = D2;
const int ledPin1 = D5;
const int ledPin2 = D6;
const int ledPin3 = D7;


char command;

WiFiServer server(80);


void establish_connection(){
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("Connected to WiFi");
  Serial.println(WiFi.localIP());
  
  server.begin();
}

void handle_messages(){
  WiFiClient client = server.available();
  if (client) {
    Serial.println("New Client.");
    String currentLine = "";

    while (client.connected()) {
      if (client.available()) {
        // Read a byte from the client
        command = client.read(); // Read a single byte
        currentLine += command; // Append it to the current line
        
        Serial.print(command);  // Print the received character to Serial Monitor
        
        // If the received data ends with a newline character
        
        Serial.print("Received: ");
        Serial.println(currentLine);
          
          // Send a response
        client.println("SUCCESS NODEMCU");
          currentLine = ""; // Reset for next message
      }
    }
    client.stop();
    Serial.println("Client Disconnected.");
  }
}

void Speed1(){
  digitalWrite(ledPin1, HIGH); // Set the LED pin as output
  digitalWrite(ledPin2,LOW);
  digitalWrite(ledPin3,LOW);
  digitalWrite(motor,HIGH);
  analogWrite(pwm, 100);

}
void Speed2(){
  digitalWrite(ledPin1, LOW); // Set the LED pin as output
  digitalWrite(ledPin2,HIGH);
  digitalWrite(ledPin3,LOW);
  digitalWrite(motor,HIGH);
  analogWrite(pwm, 150);
}

void Speed3(){
  digitalWrite(ledPin1,LOW); // Set the LED pin as output
  digitalWrite(ledPin2,LOW);
  digitalWrite(ledPin3,HIGH);
  digitalWrite(motor,HIGH);
  analogWrite(pwm, 200);
}

void Speed4(){
  digitalWrite(ledPin1,HIGH); // Set the LED pin as output
  digitalWrite(ledPin2,HIGH);
  digitalWrite(ledPin3,HIGH);
  digitalWrite(motor,HIGH);
  analogWrite(pwm, 250);
}

void FanOFF(){
  digitalWrite(ledPin1, LOW); // Set the LED pin as output
  digitalWrite(ledPin2,LOW);
  digitalWrite(ledPin3,LOW);
  digitalWrite(motor,LOW);
  analogWrite(pwm, 0);
}


void setup() {
  pinMode(ledPin1, OUTPUT); // Set the LED pin as output
  pinMode(ledPin2,OUTPUT);
  pinMode(ledPin3,OUTPUT);
  pinMode(motor,OUTPUT);

  digitalWrite(ledPin1, LOW); // Set the LED pin as output
  digitalWrite(ledPin2,LOW);
  digitalWrite(ledPin3,LOW);
  digitalWrite(motor,LOW);
  analogWrite(pwm, 0); 

  establish_connection();
}

void loop() {
  handle_messages();
  if(command=='1'){
    Serial.println("Command is 1");
    Speed1();
  }else if(command=='2'){
    Serial.println("Command is 2");
    Speed2();
  }else if(command=='3'){
    Serial.println("Command is 3");
    Speed3();
  }else if(command=='4'){
    Serial.println("Command is 3");
    Speed4();
  }else{
    FanOFF();
  }
}

