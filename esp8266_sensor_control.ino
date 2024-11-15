#include <Wire.h>
#include <Adafruit_MCP3008.h>
#include <LCD_I2C.h>
#include "ESP_Wahaj.h"
#include <SimpleDHT.h>
int pinDHT11 = D0;
SimpleDHT11 dht11(pinDHT11);
Adafruit_MCP3008 adc;
LCD_I2C lcd(0x27);
int pwm = 0;

void setup() {
  Serial.begin(9600);
  pinMode(D4,OUTPUT);
  digitalWrite(D4,LOW);
  pinMode(D3,INPUT); 
  start("Project","12345678");
  adc.begin();
  lcd.begin();
  lcd.backlight();
  // Example: 50% duty cycle
}

void loop() {
  // Read sensor values from MCP3008
   if (CheckNewReq()==1) {
    byte temperature = 0;
  byte humidity = 0;
  int err = SimpleDHTErrSuccess;
  if ((err = dht11.read(&temperature, &humidity, NULL)) != SimpleDHTErrSuccess) {
    Serial.print("Read DHT11 failed, err="); Serial.println(err);delay(1000);
    return;
  }
  
  int a = adc.readADC(0);
  int b = adc.readADC(1);
  int e = adc.readADC(2);
int c = temperature;
int d = humidity;

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("GAS-1: ");
  lcd.print(a); // Print with 2 decimal places
  lcd.print(" PPM");

  lcd.setCursor(0, 1);
  lcd.print("GAS-2");
  lcd.print(b); // Print with 2 decimal places
  lcd.print(" PPM");

  delay(2000); // Display for 2 seconds
lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("GAS-3: ");
  lcd.print(e); // Print with 2 decimal places
  lcd.print(" PPM");
delay(2000);
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("TEMPERATURE:");
  lcd.print(c); // Print with 2 decimal places
  lcd.print(" C");
  lcd.setCursor(0, 1);
  lcd.print("HUMIDITY: ");
  lcd.print(d); // Print with 2 decimal places
  lcd.print(" %");
  delay(2000); // Display for 2 seconds
       String myString = String(a)+String("-")+String(b)+String("-")+String(e)+String("-")+String(c)+String("-")+String(d);
    returnThisStr(myString);
    delay(1000);
String path = getPath();
      path.remove(0,1);
       pwm = path.toInt();
       int pir=digitalRead(D3);
if(pwm==1 && pir==0)
      {
        digitalWrite(D4,HIGH);
        }
        else{
          digitalWrite(D4,LOW);
          }
    } 
}
