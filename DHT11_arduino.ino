#include "DHT.h"
#include <Ultrasonic.h>

#define DHTPIN A1
#define DHTTYPE DHT11

const int trigPin = 2;
const int echoPin = 4;

float d;

Ultrasonic ultrasonic(trigPin, echoPin);
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  dht.begin();
}

void loop() {
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  Serial.print(t);
  Serial.print(",");
  Serial.print(h);
  Serial.print(",");
  
  d = ultrasonic.Ranging(CM);
  Serial.println(d);
  delay(1000);
}
