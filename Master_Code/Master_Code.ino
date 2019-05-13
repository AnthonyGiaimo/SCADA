int state = 0;

void setup() 
{
  Serial.begin(9600);
  while(!Serial){}
  Serial.println("Brew Commands:");
  Serial1.begin(38400);  // HC-05 default speed in AT command more
}

void loop()
{

  // Keep reading from HC-05 and send to Arduino Serial Monitor
  if (Serial1.available()){
    Serial.write(Serial1.read());
  }

  // Keep reading from Arduino Serial Monitor and send to HC-05
  if (Serial.available()){
   state = Serial.read();
   Serial.write(state);
   Serial1.write(state);
  }
  
}
