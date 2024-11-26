#include <unity.h>
// #define DSPLIB_DISPLAY_H

// class DisplayDevice
// {
// public:
//     DisplayDevice() {};
//     void sendBuffer(void) {};
//     void clearBuffer(void) {};
//     void drawPixel(uint16_t x, uint16_t y) {};
// };

// DisplayDevice display;

// #include <signal_plotter.h>

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

int main()
{

    UNITY_BEGIN();
    RUN_TEST(simple_test);
    UNITY_END();

    return 0;
}
