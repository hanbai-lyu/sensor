#include <QMC5883LCompass.h>
#include <string.h>

QMC5883LCompass compass;

void setup() {
  Serial.begin(9600);
  compass.init();
}

void loop() {
  int x,y,z;
  char temp[8],arr[32]="";
    
  // Read compass values
  compass.read();

  // Return XYZ readings
  x = compass.getX();
  sprintf(temp,"%d",x);
  strcat(arr,temp);
  strcat(arr,",");
  delay(50);
  y = compass.getY();
  sprintf(temp,"%d",y);
  strcat(arr,temp);
  strcat(arr,",");
  delay(50);
  z = compass.getZ();
  sprintf(temp,"%d",z);
  strcat(arr,temp);
  strcat(arr,",");
  Serial.println(arr);
  delay(150);
}
