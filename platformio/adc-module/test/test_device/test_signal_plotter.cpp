
#include <Arduino.h>
#include <signal_plotter.h>

SignalPlotter *plotter;

unsigned int s = 0;

void setup(void)
{
    plotter = new SignalPlotter();
    display.begin();
    Serial.begin(9600);
    s = 0;
}

#include <WString.h>

void loop(void)
{
    int h = s / 4;
    plotter->pushValue(h);
    s = (s + 1) % display.getWidth();
}