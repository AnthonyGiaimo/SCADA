#include <SoftwareSerial.h>

SoftwareSerial BTSerial(10, 11); // RX | TX

int state = 0;

void setup() 
{ 
  pinMode(13, OUTPUT);
  BTSerial.begin(38400); // initialize Serial communication for bt module
  delay(1000);
} 


void loop() 
{
  if (BTSerial.available()>0){
    state = BTSerial.read(); 
  }
  if (state == '1')
    {
      digitalWrite(13, HIGH);
    }
  if (state == '0')
    {
      digitalWrite(13, LOW);
    }   
}
