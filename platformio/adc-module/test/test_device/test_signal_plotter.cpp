
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

void linear_signal()
{
    int h = s / 4;
    plotter->pushValue(h);
}
void linear_signal_inv()
{
    int h = 32 - s / 4;
    plotter->pushValue(h);
}

void sine_signal()
{
    int h = 16 + int(16 * sin(2 * M_PI * s / 132));
    plotter->pushValue(h);
}

void cosine_signal()
{
    int h = 16 + int(16 * cos(2 * M_PI * s / 132));
    plotter->pushValue(h);
}

void loop(void)
{

    sine_signal();

    s = (s + 1) % display.getWidth();
}