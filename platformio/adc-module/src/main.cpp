
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

#include <WString.h>

void loop(void)
{

  unsigned long current = micros();
  if (current - latsTick > intervalMicros)

  {
    if (digitalRead(D0) == HIGH)
    {
      plotter->viewFreezed();
    }
    else
    {
      plotter->pushValue(analogRead(A0 / 32));
      latsTick = current;
    }
  }
}