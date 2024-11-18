#include <Arduino.h>
#include <string>
#include "display.h"

SignalPloter plotter(display);

void setup()
{
  displaySetup();
}

void loop()
{

  plotter.pushValue(analogRead(A0 / 32));
  delayMicroseconds(100);
}