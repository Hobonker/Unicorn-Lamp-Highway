#include <Adafruit_NeoPixel.h>

#define LED_PIN     6 
#define NUM_LEDS    8
#define BRIGHTNESS  255

Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

// Duration settings (in milliseconds)
const unsigned long onTime  = 10UL * 60UL * 1000UL;  // 10 minutes
const unsigned long offTime = 1UL * 60UL * 1000UL;   // 1 minute

void setup() {
  strip.begin();
  strip.setBrightness(BRIGHTNESS);
  strip.show(); // Ensure all LEDs start off
}

void loop() {
  for (int i = 0; i < NUM_LEDS; i++) {
    strip.setPixelColor(i, strip.Color(255, 0, 0)); // Red
  }
  strip.show();
  delay(onTime); // Wait 10 minutes

  for (int i = 0; i < NUM_LEDS; i++) {
    strip.setPixelColor(i, 0); // Off
  }
  strip.show();
  delay(offTime); // Wait 1 minute
}
