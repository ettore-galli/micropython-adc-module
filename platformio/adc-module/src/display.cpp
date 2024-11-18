
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <string>
#include <display.h>
#include <display_base.h>

#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32

void displaySetup()
{
  Serial.begin(9600);

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if (!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS))
  {
    Serial.println(F("SSD1306 allocation failed"));
  }

  // Show initial display buffer contents on the screen --
  // the library initializes this with an Adafruit splash screen.
  display.display();
  delay(2000); // Pause for 2 seconds
  display.clearDisplay();
  display.display();
}

void printString(int16_t x, int16_t y, std::string message, int size)
{
  display.clearDisplay();
  display.setTextSize(size);           // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE); // Draw white text
  display.setCursor(x, y);             // Start at top-left corner
  display.cp437(true);                 // Use full 256 char 'Code Page 437' font
  for (char c : message)
  {
    display.print(c);
  }
  display.display();
}

void displayValueBar(int value)
{
  display.clearDisplay();

  for (int v = 0; v < value; ++v)
  {
    // display.drawLine(0, v, display.width() - 1, v, SSD1306_WHITE);
    display.drawLine(4 * v, 0, 4 * v, display.height() - 1, SSD1306_WHITE);
  }

  display.display();
}
