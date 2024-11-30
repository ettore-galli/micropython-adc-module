
#include <Arduino.h>
#include <signal_plotter.h>

SignalPlotter *plotter;

const unsigned intervalMicros = 250;
unsigned long lastTick = 0;

void setup(void)
{
  pinMode(D0, INPUT);
  plotter = new SignalPlotter();
  display.begin();
  Serial.begin(9600);
  lastTick = 0;
}

int16_t readAnalogValue()
{
  return analogRead(A0);
}

int readFreezeButton()
{
  return digitalRead(D0);
}

void loop(void)
{

  unsigned long current = micros();
  if (current - lastTick > intervalMicros)

  {
    if (readFreezeButton() == HIGH)
    {
      plotter->viewFreezed();
    }
    else
    {
      plotter->pushValue(readAnalogValue());
      lastTick = current;
    }
  }
}