"""
Unit Test for Assignment A3

This module shows off what a good unit test for a3 should look like.

Philip Coppolino, PCC78
10/8/21
"""
import introcs
import a3


def test_complement():
    """
    Test function complement
    """
    print('Testing complement')

    # One test is really good enough here
    comp = a3.complement_rgb(introcs.RGB(250, 0, 71))
    introcs.assert_equals(255-250, comp.red)
    introcs.assert_equals(255-0,   comp.green)
    introcs.assert_equals(255-71,  comp.blue)

    # One more for good measure
    comp = a3.complement_rgb(introcs.RGB(128, 64, 255))
    introcs.assert_equals(255-128, comp.red)
    introcs.assert_equals(255-64,  comp.green)
    introcs.assert_equals(255-255, comp.blue)


def test_str5():
    """
    Test function str5
    """
    print('Testing str5')
    introcs.assert_equals('130.6',  a3.str5(130.59))
    introcs.assert_equals('130.5',  a3.str5(130.54))
    introcs.assert_equals('100.0',  a3.str5(100))
    introcs.assert_equals('100.6',  a3.str5(100.56))
    introcs.assert_equals('99.57',  a3.str5(99.566))
    introcs.assert_equals('99.99',  a3.str5(99.99))
    introcs.assert_equals('100.0',  a3.str5(99.995))
    introcs.assert_equals('22.00',  a3.str5(21.99575))
    introcs.assert_equals('21.99',  a3.str5(21.994))
    introcs.assert_equals('10.01',  a3.str5(10.013567))
    introcs.assert_equals('10.00',  a3.str5(10.000000005))
    introcs.assert_equals('10.00',  a3.str5(9.9999))
    introcs.assert_equals('9.999',  a3.str5(9.9993))
    introcs.assert_equals('1.355',  a3.str5(1.3546))
    introcs.assert_equals('1.354',  a3.str5(1.3544))
    introcs.assert_equals('0.046',  a3.str5(.0456))
    introcs.assert_equals('0.045',  a3.str5(.0453))
    introcs.assert_equals('0.006',  a3.str5(.0056))
    introcs.assert_equals('0.001',  a3.str5(.0013))
    introcs.assert_equals('0.000',  a3.str5(.0004))
    introcs.assert_equals('0.001',  a3.str5(.0009999))
    introcs.assert_equals('1.000',  a3.str5(1))
    introcs.assert_equals('0.000',  a3.str5(0.0000000001))


def test_str5_color():
    """
    Test the str5 functions for cmyk and hsv.
    """
    print('Testing str5_cmyk and str5_hsl')

    # Tests for str5_cmyk (add one more test)
    # We need to make sure the coordinates round properly
    text = a3.str5_cmyk(introcs.CMYK(98.448, 25.362, 72.8, 1.0))
    introcs.assert_equals('(98.45, 25.36, 72.80, 1.000)',text)

    text = a3.str5_cmyk(introcs.CMYK(0.0, 1.5273, 100.0, 57.846))
    introcs.assert_equals('(0.000, 1.527, 100.0, 57.85)',text)

    # Tests for str5_hsl (add two)
    text = a3.str5_hsl(introcs.HSL(255.99, 0.000000000001, .0009))
    introcs.assert_equals('(256.0, 0.000, 0.001)',text)

    text = a3.str5_hsl(introcs.HSL(56.78, 0.94949494, 1))
    introcs.assert_equals('(56.78, 0.949, 1.000)',text)


def test_rgb_to_cmyk():
    """
    Test translation function rgb_to_cmyk
    """
    print('Testing rgb_to_cmyk')

    # The function should guarantee accuracy to three decimal places
    rgb = introcs.RGB(255, 255, 255);
    cmyk = a3.rgb_to_cmyk(rgb);
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(0.0, round(cmyk.black,3))

    rgb = introcs.RGB(0, 0, 0);
    cmyk = a3.rgb_to_cmyk(rgb);
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(0.0, round(cmyk.magenta,3))
    introcs.assert_equals(0.0, round(cmyk.yellow,3))
    introcs.assert_equals(100.0, round(cmyk.black,3))

    rgb = introcs.RGB(217, 43, 164);
    cmyk = a3.rgb_to_cmyk(rgb);
    introcs.assert_equals(0.0, round(cmyk.cyan,3))
    introcs.assert_equals(80.184, round(cmyk.magenta,3))
    introcs.assert_equals(24.424, round(cmyk.yellow,3))
    introcs.assert_equals(14.902, round(cmyk.black,3))


def test_cmyk_to_rgb():
    """
    Test translation function cmyk_to_rgb
    """
    print('Testing cmyk_to_rgb')

    cmyk = introcs.CMYK(0,0,0,0)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(255, (rgb.red))
    introcs.assert_equals(255, (rgb.green))
    introcs.assert_equals(255, (rgb.blue))

    cmyk = introcs.CMYK(38,76,0,7)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(147, (rgb.red))
    introcs.assert_equals(57, (rgb.green))
    introcs.assert_equals(237, (rgb.blue))

    cmyk = introcs.CMYK(0,0,0,100)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(0, (rgb.red))
    introcs.assert_equals(0, (rgb.green))
    introcs.assert_equals(0, (rgb.blue))

    cmyk = introcs.CMYK(32.49999999, 55.213,11.0, 18.999)
    rgb = a3.cmyk_to_rgb(cmyk)
    introcs.assert_equals(139, (rgb.red))
    introcs.assert_equals(93, (rgb.green))
    introcs.assert_equals(184, (rgb.blue))


def test_rgb_to_hsl():
    """
    Test translation function rgb_to_hsv
    """
    print('Testing rgb_to_hsl')

    #if l == 1.0
    rgb = introcs.RGB(255, 255, 255);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(0.0, round(hsl.saturation,3))
    introcs.assert_equals(1.0, round(hsl.lightness,3))
    #if l == 0.0
    rgb = introcs.RGB(0, 0, 0);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(0.0, round(hsl.saturation,3))
    introcs.assert_equals(0.0, round(hsl.lightness,3))
    #if maximum == minimum
    rgb = introcs.RGB(55, 55, 55);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(0.0, round(hsl.hue,3))
    introcs.assert_equals(0.0, round(hsl.saturation,3))
    introcs.assert_equals(0.216, round(hsl.lightness,3))
    #if maximum == r and g >= b
    rgb = introcs.RGB(200, 168, 22);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(49.213, round(hsl.hue,3))
    introcs.assert_equals(0.802, round(hsl.saturation,3))
    introcs.assert_equals(0.435, round(hsl.lightness,3))
    #if maximum == r and g < b
    rgb = introcs.RGB(179, 5, 88);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(331.379, round(hsl.hue,3))
    introcs.assert_equals(0.946, round(hsl.saturation,3))
    introcs.assert_equals(0.361, round(hsl.lightness,3))
    #if maximum == g
    rgb = introcs.RGB(1, 3, 2);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(150.0, round(hsl.hue,3))
    introcs.assert_equals(0.5, round(hsl.saturation,3))
    introcs.assert_equals(0.008, round(hsl.lightness,3))
    #if maximum == b
    rgb = introcs.RGB(0, 0, 255);
    hsl = a3.rgb_to_hsl(rgb);
    introcs.assert_equals(240.0, round(hsl.hue,3))
    introcs.assert_equals(1.0, round(hsl.saturation,3))
    introcs.assert_equals(0.5, round(hsl.lightness,3))


def test_hsl_to_rgb():
    """
    Test translation function hsv_to_rgb
    """
    print('Testing hsl_to_rgb')

    hsl = introcs.HSL(0.0,0.0,0.0)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(0, rgb.green)
    introcs.assert_equals(0, rgb.blue)

    hsl = introcs.HSL(0.0,0.0,1.0)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)
    #if hi == 0
    hsl = introcs.HSL(35.873,0.45,0.87654321)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(238, rgb.red)
    introcs.assert_equals(226, rgb.green)
    introcs.assert_equals(209, rgb.blue)
    #if hi == 1
    hsl = introcs.HSL(60.0,0.2,0.435)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(133, rgb.red)
    introcs.assert_equals(133, rgb.green)
    introcs.assert_equals(89, rgb.blue)
    #if hi == 2
    hsl = introcs.HSL(140.123456789,0.0000001,0.87)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(222, rgb.red)
    introcs.assert_equals(222, rgb.green)
    introcs.assert_equals(222, rgb.blue)
    #if hi == 3
    hsl = introcs.HSL(201.999,0.99,0.49)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(1, rgb.red)
    introcs.assert_equals(158, rgb.green)
    introcs.assert_equals(249, rgb.blue)
    #if hi == 4
    hsl = introcs.HSL(255,.459,0.76)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(180, rgb.red)
    introcs.assert_equals(166, rgb.green)
    introcs.assert_equals(222, rgb.blue)
    #if hi == 5
    hsl = introcs.HSL(359.9999999,1,1)
    rgb = a3.hsl_to_rgb(hsl)
    introcs.assert_equals(255, rgb.red)
    introcs.assert_equals(255, rgb.green)
    introcs.assert_equals(255, rgb.blue)


def test_contrast_value():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_value')

    # contrast == -1.0 (extreme)
    result = a3.contrast_value(0.0,-1.0)
    introcs.assert_floats_equal(0.5,result)

    result = a3.contrast_value(1.0,-1.0)
    introcs.assert_floats_equal(0.5,result)

    # contrast < 0, bottom part of sawtooth
    result = a3.contrast_value(0.1,-0.5)
    introcs.assert_floats_equal(0.3,result)

    # contrast < 0, middle of sawtooth
    result = a3.contrast_value(0.4,-0.4)
    introcs.assert_floats_equal(0.4571429,result)

    # contrast < 0, upper part of sawtooth
    result = a3.contrast_value(0.9,-0.3)
    introcs.assert_floats_equal(0.8142857,result)

    # contrast == 0.0, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.0)
    introcs.assert_floats_equal(0.1,result)

    # contrast == 0, middle of sawtooth
    result = a3.contrast_value(0.6,0.0)
    introcs.assert_floats_equal(0.6,result)

    # contrast == 0.0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.0)
    introcs.assert_floats_equal(0.9,result)

    # contrast > 0, bottom part of sawtooth
    result = a3.contrast_value(0.1,0.3)
    introcs.assert_floats_equal(0.05384615,result)

    # contrast > 0, middle of sawtooth
    result = a3.contrast_value(0.4,0.5)
    introcs.assert_floats_equal(0.2,result)

    # contrast > 0, upper part of sawtooth
    result = a3.contrast_value(0.9,0.4)
    introcs.assert_floats_equal(0.95714286,result)

    # contrast == 1.0 (extreme)
    result = a3.contrast_value(0.2,1.0)
    introcs.assert_floats_equal(0.0,result)

    result = a3.contrast_value(0.6,1.0)
    introcs.assert_floats_equal(1.0,result)


def test_contrast_rgb():
    """
    Test translation function contrast_value
    """
    print('Testing contrast_rgb')

    # Negative contrast
    rgb = introcs.RGB(240, 15, 118)
    hsv = a3.contrast_rgb(rgb,-0.4)
    introcs.assert_equals(220, rgb.red)
    introcs.assert_equals(35,  rgb.green)
    introcs.assert_equals(123, rgb.blue)
    #Positive contrast
    rgb = introcs.RGB(32, 0, 255)
    hsv = a3.contrast_rgb(rgb, 0.725)
    introcs.assert_equals(5, rgb.red)
    introcs.assert_equals(0,  rgb.green)
    introcs.assert_equals(255, rgb.blue)
    #0 contrast
    rgb = introcs.RGB(135, 201, 11)
    hsv = a3.contrast_rgb(rgb, 0.0)
    introcs.assert_equals(135, rgb.red)
    introcs.assert_equals(201,  rgb.green)
    introcs.assert_equals(11, rgb.blue)
    #contrast = 1
    rgb = introcs.RGB(10, 180, 230)
    hsv = a3.contrast_rgb(rgb, 1.0)
    introcs.assert_equals(0, rgb.red)
    introcs.assert_equals(255,  rgb.green)
    introcs.assert_equals(255, rgb.blue)
    #contrast = -1
    rgb = introcs.RGB(39, 77, 130)
    hsv = a3.contrast_rgb(rgb, -1.0)
    introcs.assert_equals(128, rgb.red)
    introcs.assert_equals(128,  rgb.green)
    introcs.assert_equals(128, rgb.blue)


# Script Code (Prevents tests running on import)
if __name__ == "__main__":
    test_complement()
    test_str5()
    test_str5_color()
    test_rgb_to_cmyk()
    test_cmyk_to_rgb()
    test_rgb_to_hsl()
    test_hsl_to_rgb()
    test_contrast_value()
    test_contrast_rgb()
    print('Module a3 passed all tests.')
