
#include <Arduino.h>
#include <signal_plotter.h>
#include <math.h>
#include <WString.h>

SignalPlotter *plotter;

unsigned int s = 0;

void setup(void)
{
    plotter = new SignalPlotter();
    display.begin();
    Serial.begin(9600);
    s = 0;
}

void sine_signal(int phase)
{
    int w = display.getWidth();
    int h = 16 + int(16 * sin(2 * M_PI * s / (w + phase)));
    plotter->pushValue(h);
    s = (s + 1) % (w + phase);
}

void loop(void)
{
    sine_signal(3);
}