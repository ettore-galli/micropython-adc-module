#ifndef DSPLIB_H
#define DSPLIB_H
#include <Wire.h>
#include <U8g2lib.h>

// From docs:
// U8G2_SSD1306_128X32_UNIVISION_F_HW_I2C u8g2(U8G2_R0, /* reset=*/U8X8_PIN_NONE, /* clock=*/SCL, /* data=*/SDA); // pin remapping with ESP8266 HW I2C
// U8G2_SSD1306_128X32_UNIVISION_F_HW_I2C(rotation, [reset [, clock, data]]) [full framebuffer, size = 512 bytes]

class DisplayDevice : public U8G2_SSD1306_128X32_UNIVISION_F_HW_I2C
{
public:
    DisplayDevice(
        const u8g2_cb_t *rotation,
        uint8_t reset = U8X8_PIN_NONE,
        uint8_t clock = U8X8_PIN_NONE,
        uint8_t data = U8X8_PIN_NONE) : U8G2_SSD1306_128X32_UNIVISION_F_HW_I2C(rotation, reset, clock, data) {
                                        };
};

#endif