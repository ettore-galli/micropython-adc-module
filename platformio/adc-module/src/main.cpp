
#include <Arduino.h>
#include <signal_plotter.h>

SignalPlotter *plotter;

const unsigned intervalMicros = 100;
unsigned long latsTick = 0;

void setup(void)
{
  pinMode(D0, INPUT);
  plotter = new SignalPlotter();
  display.begin();
  Serial.begin(9600);
  latsTick = 0;
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
  if (current - latsTick > intervalMicros)

  {
    if (readFreezeButton() == HIGH)
    {
      plotter->viewFreezed();
    }
    else
    {
      plotter->pushValue(readAnalogValue());
      latsTick = current;
    }
  }
}