/*
  AnalogReadSerial

  Reads an analog input on pin 0, prints the result to the Serial Monitor.
  Graphical representation is available using Serial Plotter (Tools > Serial Plotter menu).
  Attach the center pin of a potentiometer to pin A0, and the outside pins to +5V and ground.

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/AnalogReadSerial
*/
String readString;
// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
}

// the loop routine runs over and over again forever:
void loop() {
  Serial.print("clockCheck\n");
  Serial.flush();
  delay(5000);
  while (Serial.available() > 0)
  {
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
  }
  Serial.print(readString + "\n");
  Serial.flush();
  readString = "";
  
  delay(15000);
  
  Serial.print("alarmSet\n");
  Serial.flush();
  delay(5000);
  while (Serial.available()> 0)
  {
      char c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
  }
  Serial.print(readString + "\n");
  Serial.flush();
  readString = "";
  
  delay(15000);  
}

