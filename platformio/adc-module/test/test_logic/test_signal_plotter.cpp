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
    void drawPixel(uint16_t x, uint16_t y) { count++; };
    void setDrawColor(uint8_t color_index) {};
    void drawVLine(uint8_t x, uint8_t y, uint8_t h) { count++; };
    uint8_t getDisplayHeight(void) { return 32; };
    uint8_t getDisplayWidth(void) { return 128; };
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

    display = *new DisplayDevice();
    SignalPlotter *sp = new SignalPlotter();

    sp->pushValue((int16_t)111);
    sp->pushValue((int16_t)222);
    sp->pushValue((int16_t)333);

    TEST_ASSERT_EQUAL(111, sp->_values[0]);
    TEST_ASSERT_EQUAL(222, sp->_values[1]);
    TEST_ASSERT_EQUAL(333, sp->_values[2]);
}

void signal_plotter_triggers_plot_after_buffer_full(void)
{

    display = *new DisplayDevice();
    SignalPlotter *sp = new SignalPlotter();

    for (int i = 0; i < SCREEN_WIDTH; i++)
    {
        sp->pushValue(i);
    }

    TEST_ASSERT_EQUAL(0, display.count);

    sp->pushValue(0);

    TEST_ASSERT_EQUAL(128, display.count);
}

int main()
{

    UNITY_BEGIN();
    RUN_TEST(simple_test);
    RUN_TEST(signal_plotter_basic);
    RUN_TEST(signal_plotter_triggers_plot_after_buffer_full);
    UNITY_END();

    return 0;
}
