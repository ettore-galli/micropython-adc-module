#ifndef DSPLIB_DISPLAY_H
#define DSPLIB_DISPLAY_H

#include <dsplib.h>
DisplayDevice display(U8G2_R0, /* reset=*/U8X8_PIN_NONE, /* clock=*/SCL, /* data=*/SDA); // pin remapping with ESP8266 HW I2C

#endif