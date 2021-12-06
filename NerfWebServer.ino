#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <WiFi.h>
#include <WebServer.h>
#include <ESPmDNS.h>

#define TRIGGER 15
#define MOTOR 13

WebServer server(80);
const char *mDNSAddr = "nerfornothing";

void setup() {
  Serial.begin(9600);
  pinMode(TRIGGER, OUTPUT);
  pinMode(MOTOR, OUTPUT);

  // For some reason, a HIGH state means OFF for our relay.
  digitalWrite(TRIGGER, HIGH);
  digitalWrite(MOTOR, HIGH);

  // Initialize web server.
  WiFi.mode(WIFI_STA);
  WiFi.begin("Dam", "");

  while(WiFi.status() != WL_CONNECTED) { 
    delay(500); 
  }
  Serial.println("Connected.");
  server.on("/", initialPage);
  server.on("/toggleMotor", toggleMotor);
  server.on("/toggleTrigger", toggleTrigger);

  if (MDNS.begin(mDNSAddr)) {
    Serial.println("mdns registered.");
  } else { 
    Serial.println("Could not register mdns.");
  }

  server.begin();
}

void initialPage() {
  server.send(200, "text/html", "<img src=\"https://cdn.discordapp.com/attachments/642491654967787572/821473531383513108/image0.gif\"/>"); 
}

void toggleMotor() {
  digitalWrite(MOTOR, 1 - digitalRead(MOTOR));
  server.send(200, "text/html", "<p>Success</p>");
}

void toggleTrigger() {
  digitalWrite(TRIGGER, 1 - digitalRead(TRIGGER));
  server.send(200, "text/html", "<p>Success</p>");
}

void toggleTriggerBlocking() {
  digitalWrite(TRIGGER, 1 - digitalRead(TRIGGER));
  delay(0.4);
  digitalWrite(TRIGGER, 1 - digitalRead(TRIGGER));
  server.send(200, "text/html", "<p>Success</p>");
}

void loop() {
  server.handleClient(); 
}
