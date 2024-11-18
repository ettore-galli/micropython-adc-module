#include <Arduino.h>
#include <string>
#include "display.h"

SignalPloter plotter(display);

const unsigned intervalMicros = 100;
unsigned long latsTick = 0;

void setup()
{
  displaySetup();
  latsTick = 0;
}

void loop()
{
  unsigned long current = micros();
  if (current - latsTick > intervalMicros)
  {
    plotter.pushValue(analogRead(A0 / 32));
    latsTick = current;
  }
}