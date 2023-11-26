#include "WifiCam.hpp"
#include <WiFi.h>

#define led_FLASH 4

static const char* AP_SSID = "EcoLensNUM0002";  // SSID
static const char* AP_PASS = "";                // Password
static const int   Channel = 1;                 // Wifi Channel
static const int   Hidden = 1;                  // SSID Hiden? True=1, False=0
static const int   AP_Max_Connection = 3;       // Max devices

esp32cam::Resolution initialResolution;

WebServer server(80);

void
setup()
{
  Serial.begin(115200);
  Serial.println();
  delay(2000);

  pinMode(led_FLASH, OUTPUT);

  // WiFi-Modus auf Access Point (WIFI_AP) setzen
  WiFi.mode(WIFI_AP);
  Serial.println(WiFi.softAP(AP_SSID, AP_PASS, Channel, Hidden, AP_Max_Connection) ? "Configuration successful" : "Configuration error!");

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
  Serial.println(WiFi.softAPIP());
  Serial.println("SSID of the network: " + WiFi.softAPSSID());

  digitalWrite(led_FLASH, LOW);

  addRequestHandlers();
  server.begin();
}

void
loop()
{
  server.handleClient();
}
