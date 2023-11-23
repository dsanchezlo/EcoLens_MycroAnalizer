#include "WifiCam.hpp"
#include <WiFi.h>
#include "BluetoothSerial.h"

#define led_FLASH 4

BluetoothSerial BT;
static const char* WIFI_SSID = "LAPTOP-DS-HCUSUNAV";
static const char* WIFI_PASS = "contrasena";

esp32cam::Resolution initialResolution;

WebServer server(80);

void
setup()
{

  BT.begin("ESP32-CAM");
  Serial.begin(115200);
  Serial.println();
  delay(2000);

  pinMode(led_FLASH, OUTPUT);

  WiFi.persistent(false);
  WiFi.mode(WIFI_STA);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
  if (WiFi.waitForConnectResult() != WL_CONNECTED) {
    Serial.println("WiFi failure");
    delay(5000);
    ESP.restart();
  }
  Serial.println("WiFi connected");

  {
    using namespace esp32cam;

    initialResolution = Resolution::find(1024, 768);

    Config cfg;
    cfg.setPins(pins::AiThinker);
    cfg.setResolution(initialResolution);
    cfg.setJpeg(80);

    bool ok = Camera.begin(cfg);
    if (!ok) {
      Serial.println("camera initialize failure");
      delay(5000);
      ESP.restart();
    }
    Serial.println("camera initialize success");
  }

  Serial.println("camera starting");
  Serial.print("http://");
  Serial.println(WiFi.localIP());

  digitalWrite(led_FLASH, LOW);

  addRequestHandlers();
  server.begin();
}

void
loop()
{
  server.handleClient();

  if (BT.available()>0){
    char Data=BT.read();
    if(Data=='0'){
      BT.println(WiFi.localIP());

    }
  }
}
