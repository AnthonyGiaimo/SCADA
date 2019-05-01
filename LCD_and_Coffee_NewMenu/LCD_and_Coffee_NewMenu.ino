
/*

Key Codes (in left-to-right order):

None   - 0
Select - 1
Left   - 2
Up     - 3
Down   - 4
Right  - 5

*/

#include <LiquidCrystal.h>
#include <CurieTime.h>

//Pin assignments for DFRobot LCD Keypad Shield
LiquidCrystal lcd(8, 9, 4, 5, 6, 7); 
//---------------------------------------------
int backlight = 256;
int positionC = 3;
int localKey = 0;
int menu = 1; 
int hourAlarm1 = 6;
int minuteAlarm1 = 40; 
unsigned long brewTime = 600000;
unsigned long elapsedTime;   
unsigned long storedTime;
int newHour, newMinute, newsecond, newDay, newMonth, newYear;
int lcd_key     = 0;
int adc_key_in  = 0;
//char request;
#define btnRIGHT  0
#define btnUP     1
#define btnDOWN   2
#define btnLEFT   3
#define btnSELECT 4
#define btnNONE   5

//read the buttons
int read_LCD_buttons()
{
 adc_key_in = analogRead(0);      // read the value from the sensor 
 // my buttons when read are centered at these valies: 0, 144, 329, 504, 741
 // we add approx 50 to those values and check to see if we are close
 if (adc_key_in > 1000) return btnNONE; // We make this the 1st option for speed reasons since it will be the most likely result
 if (adc_key_in < 50)   return btnRIGHT;  
 if (adc_key_in < 250)  return btnUP; 
 if (adc_key_in < 650)  return btnDOWN; 
 if (adc_key_in < 850)  return btnSELECT;  
 return btnNONE;  // when all others fail, return this...
}

void setup() 
{ 
  lcd.begin(16, 2);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Initializing...");
  pinMode(13, OUTPUT);
  analogWrite(9,0);
  Serial.begin(9600); // initialize Serial communication
  setTime(20, 59, 50, 17, 8, 2018);   
  delay(1000);
} 


void loop() 
{ 
  switch (menu){
    case 1:
    {
      timeStringUpdater();
    }
    break;
    case 2:
    {
      chngTime();
    }
    break;
    case 3:
    {
      brewing();
    }
    break;
    case 4:
    { 
      alarm1(); 
    }
  }
   
  if ((hour() == hourAlarm1) && (minute() == minuteAlarm1) && (second() == 00))
    {
      storedTime = millis();
      digitalWrite(13, HIGH);
      menu = 3;
    }
}

void timeStringUpdater()
{
  lcd.setCursor(0, 0);
  print2digits(hour());
  lcd.print(":");
  print2digits(minute());
  lcd.print(":");
  print2digits(second());
  lcd.print("   ");
  print2digits(day());
  lcd.print("/");
  print2digits(month());
  lcd.setCursor(0, 1);
  lcd.print("Time Brew Alarm ");
  lcd_key = read_LCD_buttons();
  lcd.setCursor(positionC,1);
  lcd.cursor();
  lcd_key = read_LCD_buttons();
  switch(lcd_key){
    case btnSELECT:
    {
      switch(positionC){
        case 3:
        {
          menu = 2;
        }break;
        case 8:
        {
          menu = 3;
          storedTime = millis();
          digitalWrite(13,HIGH);
        }break;
        case 14:
        {
          menu = 4;
        }break;
       }
      delay(250);
    }break;
   case btnRIGHT:
   {
    switch(positionC){
        case 3:
        {
         positionC = 8;
         delay(250);
        }break;
        case 8:
        {
         positionC = 14;
         delay(250);
        }break;
        case 14:
        {
         positionC = 3;
         delay(250);
        }break;
   }
  }break;
 }
 delay(50);
}
void print2digits(int number) {
  if (number >= 0 && number < 10) {
    lcd.print("0");
  }
  lcd.print(number);
}
void brewing()
{
  elapsedTime = millis();
  lcd.setCursor(0,0);
  lcd.print("     Brewing    ");
  lcd.setCursor(0,1);
  lcd.print("Please Wait CANX");
  lcd.setCursor(12,1);
  lcd.cursor();
  if (elapsedTime - storedTime >= brewTime)
  {
    digitalWrite(13,LOW);
    menu = 1;
  }
 lcd_key = read_LCD_buttons();
 if (lcd_key == btnSELECT)
 {
  digitalWrite(13,LOW);
  menu = 1;
  positionC = 3;
  delay(250);
 }
}
void chngTimeString()
{
  lcd.setCursor(0, 0);
  print2digits(newHour);
  lcd.print(":");
  print2digits(newMinute);
  lcd.print(":");
  print2digits(newsecond);
  lcd.print("   ");
  print2digits(newDay);
  lcd.print("/");
  print2digits(newMonth);
  lcd.cursor();
}
void alarmString1()
{
  lcd.setCursor(0, 0);
  print2digits(hourAlarm1);
  lcd.print(":");
  print2digits(minuteAlarm1);
  lcd.print(":");
  lcd.print("00");
  lcd.print("   ");
  print2digits(day());
  lcd.print("/");
  print2digits(month());
  lcd.cursor();
}

void alarm1()
{
  lcd.setCursor(0,1);
  lcd.print("  Change Alarm  ");
  int exitY = 0;
  positionC = 0;
  lcd.cursor();
  delay(250);
  alarmString1();
  do{
    lcd_key = read_LCD_buttons();
    lcd.setCursor(positionC,0);
    switch(lcd_key){
    case btnSELECT:
    {
      exitY = 1;
      delay(250);
    } break;
    case btnUP:
    {
      if (positionC == 0)
      {
        hourAlarm1 = hourAlarm1 + 10;
        delay(250);
        alarmString1();
      }
      else if (positionC == 1)
      {
        hourAlarm1 = hourAlarm1 + 1;
        delay(250);
        alarmString1();
      }
      else if (positionC == 3)
      {
        minuteAlarm1 = minuteAlarm1 + 10;
        delay(250);
        alarmString1();
      }
      else if (positionC == 4)
      {
        minuteAlarm1 = minuteAlarm1 + 1;
        delay(250);
        alarmString1();
      }
    }break;
    case btnDOWN:
    {
      if (positionC == 0)
      {
        hourAlarm1 = hourAlarm1 - 10;
        delay(250);
        alarmString1();
      }
      else if (positionC == 1)
      {
        hourAlarm1 = hourAlarm1 - 1;
        delay(250);
        alarmString1();
      }
      else if (positionC == 3)
      {
        minuteAlarm1 = minuteAlarm1 - 10;
        delay(250);
        alarmString1();
      }
      else if (positionC == 4)
      {
        minuteAlarm1 = minuteAlarm1 - 1;
        delay(250);
        alarmString1();
      }
    }break;
    case btnRIGHT:
    {
      if (positionC!= 15)
      {
        positionC = positionC + 1;
      }
      else if (positionC == 16)
      {
       positionC = 0;
      }
      delay(250);
      lcd.setCursor(positionC,0);
      alarmString1();      
    }break;
  }
  
 }while(exitY != 1);
      menu = 1;
      positionC = 3;
}

void chngTime()
{
  lcd.setCursor(0,1);
  lcd.print("                ");
  int exitY = 0;
  positionC = 0;
  newHour = hour();
  newMinute = minute();
  newsecond = second();
  newDay = day();
  newMonth = month();
  newYear = year();
  lcd.cursor();
  delay(250);\
  do{
    lcd_key = read_LCD_buttons();
    lcd.setCursor(positionC,0);
    switch(lcd_key){
    case btnSELECT:
    {
      setTime(newHour, newMinute, newsecond, newDay, newMonth, newYear);
      exitY = 1;
      delay(250);
    } break;
    case btnUP:
    {
      if (positionC == 0)
      {
        newHour = newHour + 10;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 1)
      {
        newHour = newHour + 1;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 3)
      {
        newMinute = newMinute + 10;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 4)
      {
        newMinute = newMinute + 1;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 6)
      {
        newsecond = newsecond + 10;
        delay(250);
        chngTimeString();
      }
       else if (positionC == 7)
      {
        newsecond = newsecond + 1;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 11)
      {
        newDay = newDay + 10;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 12)
      {
        newDay = newDay + 1;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 14)
      {
        newMonth = newMonth + 10;
        delay(250);
        chngTimeString();
      }
       else if (positionC == 15)
      {
        newMonth = newMonth + 1;
        delay(250);
        chngTimeString();
      }
    }break;
    case btnDOWN:
    {
      if (positionC == 0)
      {
        newHour = newHour - 10;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 1)
      {
        newHour = newHour - 1;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 3)
      {
        newMinute = newMinute - 10;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 4)
      {
        newMinute = newMinute - 1;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 6)
      {
        newsecond = newsecond - 10;
        delay(250);
        chngTimeString();
      }
       else if (positionC == 7)
      {
        newsecond = newsecond - 1;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 11)
      {
        newDay = newDay - 10;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 12)
      {
        newDay = newDay - 1;
        delay(250);
        chngTimeString();
      }
      else if (positionC == 14)
      {
        newMonth = newMonth - 10;
        delay(250);
        chngTimeString();
      }
       else if (positionC == 15)
      {
        newMonth = newMonth - 1;
        delay(250);
        chngTimeString();
      }
    }break;
    case btnRIGHT:
    {
      if (positionC!= 15)
      {
        positionC = positionC + 1;
      }
      else if (positionC == 16)
      {
       positionC = 0;
      }
      delay(250);
      lcd.setCursor(positionC,0);
      chngTimeString();      
    }break;
  }
  
 }while(exitY != 1);
      menu = 1;
      positionC = 3;
}

