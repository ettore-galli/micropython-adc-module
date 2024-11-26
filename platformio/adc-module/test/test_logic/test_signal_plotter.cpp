#include <unity.h>
#define DSPLIB_DISPLAY_H

class DisplayDevice
{
public:
    int count;
    DisplayDevice()
    {
        count = 0;
    };

    void sendBuffer(void) {};
    void clearBuffer(void) {};
    void drawPixel(uint16_t x, uint16_t y)
    {
        count++;
    };
};

DisplayDevice display;

#include <signal_plotter.h>

void setUp(void)
{
    // set stuff up here
}

void tearDown(void)
{
    // clean stuff up here
}

void simple_test(void)
{
    TEST_ASSERT_EQUAL(33, 33);
    TEST_ASSERT_EQUAL(1, 1);
}

void signal_plotter_basic(void)
{

    SignalPlotter *sp = new SignalPlotter();

    sp->pushValue((int16_t)111);
    sp->pushValue((int16_t)222);
    sp->pushValue((int16_t)333);

    TEST_ASSERT_EQUAL(111, sp->_values[1]);
    TEST_ASSERT_EQUAL(222, sp->_values[2]);
    TEST_ASSERT_EQUAL(333, sp->_values[3]);

    for (int i = 0; i < SCREEN_WIDTH + 1; i++)
    {
        sp->pushValue(i);
    }
    TEST_ASSERT_EQUAL(128, display.count);
    // TEST_ASSERT_EQUAL(1, 1);
}

int main()
{

    UNITY_BEGIN();
    RUN_TEST(simple_test);
    RUN_TEST(signal_plotter_basic);
    UNITY_END();

    return 0;
}
