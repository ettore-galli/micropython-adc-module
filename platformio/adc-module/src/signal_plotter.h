#include <string>
#include <dsplib_display.h>

#define SCREEN_WIDTH 128

class SignalPlotter
{
public:
    int16_t _samples{SCREEN_WIDTH};
    int16_t _x;
    int16_t _values[SCREEN_WIDTH];

    SignalPlotter()
    {
        _x = 0;
    };

    void displayValuesChunk()
    {
        display.clearBuffer();

        for (int16_t x = 0; x < SCREEN_WIDTH; ++x)
        {
            display.drawPixel(x, _values[x]);
        }
        display.sendBuffer();
    }

    void pushValue(int16_t v)
    {
        _x++;
        if (_x > _samples)
        {
            displayValuesChunk();
            _x = 0;
        }
        _values[_x] = v;
    };
};
