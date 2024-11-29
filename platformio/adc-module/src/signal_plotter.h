#include <string>
#include <dsplib_display.h>

#define SCREEN_WIDTH 128

void displayValuesChunkAsLine(int16_t values[SCREEN_WIDTH])
{
    display.clearBuffer();

    for (int16_t x = 0; x < SCREEN_WIDTH; ++x)
    {
        display.drawPixel(x, values[x]);
    }
    display.sendBuffer();
}

void displayValuesChunkAsHistogram(int16_t values[SCREEN_WIDTH])
{
    display.clearBuffer();
    display.setDrawColor(1);
    for (int16_t x = 0; x < SCREEN_WIDTH; ++x)
    {
        int16_t currentValue = values[x];
        display.drawVLine(x, display.getDisplayHeight() - currentValue, currentValue);
    }
    display.sendBuffer();
}

class SignalPlotter
{
public:
    bool _hold;
    int16_t _x;
    int16_t _values[SCREEN_WIDTH];
    int (*func)(int, int);
    void (*_screenDraw)(int16_t _values[]);

    SignalPlotter()
    {
        _x = 0;
        _screenDraw = displayValuesChunkAsHistogram;
    };

    void pushValue(int16_t v)
    {
        if (_x == SCREEN_WIDTH)
        {
            _screenDraw(_values);
            _x = 0;
        }
        _values[_x] = v;
        _x++;
    };
    void viewFreezed()
    {
        _screenDraw(_values);
    }
};
