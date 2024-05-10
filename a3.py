"""
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

Philip Coppolino, PCC78
10/8/21
"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.

    Parameter rgb: the color to complement
    Precondition: rgb is an RGB objecthirdfifthdigit = int(toberounded[4:5])
    """
    complementred = 255 - rgb.red
    complementgreen = 255 - rgb.green
    complementblue = 255 - rgb.blue

    return introcs.RGB(complementred, complementgreen, complementblue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.

    The decimal point counts as one of the five characters.

    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.print(roundup + 'hello')
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'. + 1)


    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    tobesliced = str(value)
    valuelength = len(tobesliced)
    decimalpos = tobesliced.find('.')
    scientific = (tobesliced.find('e') != -1)

    if (valuelength >= 6) and (int(tobesliced[5:6]) >= 5):
        newvalue = float(tobesliced[:5])
        roundup = float('0.' + ('0' * (3 - decimalpos)) + '1')
        rounded = newvalue + roundup
        sliced = (str(rounded) + '0')[:5]

    elif (valuelength >= 6) and (int(tobesliced[5:6]) < 5):
        sliced = tobesliced[:5]

    elif (valuelength < 5) and (tobesliced.find('.') == -1):
        sliced = tobesliced + '.' + ('0' * (4 - valuelength))

    elif (valuelength < 5) and (tobesliced.find('.') != -1):
        sliced = tobesliced + ('0' * (5 - valuelength))

    else:
        sliced = tobesliced

    if (scientific == True):
        sliced = '0.000'

    return sliced


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".

    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)

    Example: if str(cmyk) is

          '(0.0,31.3725490196,31.3725490196,0.0)'

    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.

    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    crounded = str5(cmyk.cyan)
    mrounded = str5(cmyk.magenta)
    yrounded = str5(cmyk.yellow)
    krounded = str5(cmyk.black)

    return ('(' + crounded +', '+mrounded +', '+yrounded +', '+krounded + ')')


def str5_hsl(hsl):
    """
    Returns the string representation of hsl in the form "(H, S, L)".

    In the output, each of H, S, and L should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)

    Example: if str(hsl) is

          '(0.0,0.313725490196,0.5)'

    then str5_hsv(hsl) is '(0.000, 0.314, 0.500)'. Note the spaces after the
    commas. These must be there.

    Parameter hsl: the color to convert to a string
    Precondition: hsl is an HSL object.
    """
    hrounded = str5(hsl.hue)
    srounded = str5(hsl.saturation)
    lrounded = str5(hsl.lightness)

    return ('(' + hrounded + ', ' + srounded + ', ' + lrounded + ')')


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.

    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html

    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change the RGB numbers to the range 0..1 by dividing them by 255.0.
    r = rgb.red / 255.0
    g = rgb.green / 255.0
    b = rgb.blue / 255.0

    k = 1.0 - max(r,g,b)

    if k == 1:
        c = 0
        m = 0
        y = 0
    else:
        c = (1.0-r-k) / (1.0-k)
        m = (1.0-g-k) / (1.0-k)
        y = (1.0-b-k) / (1.0-k)

    cconverted = c * 100.0
    mconverted = m * 100.0
    yconverted = y * 100.0
    kconverted = k * 100.0

    return introcs.CMYK(cconverted, mconverted, yconverted, kconverted)


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk

    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html

    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    c = cmyk.cyan / 100.0
    m = cmyk.magenta / 100.0
    y = cmyk.yellow / 100.0
    k = cmyk.black / 100.0

    r = (1.0-c)*(1.0-k)
    g = (1.0-m)*(1.0-k)
    b = (1.0-y)*(1.0-k)

    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)

    return introcs.RGB(r, g, b)


def rgb_to_hsl(rgb):
    """
    Return an HSL object equivalent to rgb

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter rgb: the color to convert to a HSL object
    Precondition: rgb is an RGB object
    """
    r = (rgb.red)/255
    g = (rgb.green)/255
    b = (rgb.blue)/255
    minimum = min(r,g,b)
    maximum = max(r,g,b)

    if maximum == minimum:
        h = 0
    elif maximum == r and g >= b:
        h = (60.0 * (g-b) / (maximum-minimum))
    elif maximum == r and g < b:
        h = (60.0 * (g-b) / (maximum-minimum) + 360.0)
    elif maximum == g:
        h = (60.0 * (b-r) / (maximum-minimum) + 120.0)
    elif maximum == b:
        h = (60.0 * (r-g) / (maximum-minimum) + 240.0)

    l = (maximum + minimum) / 2

    if l == 0 or l == 1:
        s = 0
    else:
        s = (maximum-l) / (min(l, (1-l)))

    return introcs.HSL(h,s,l)


def hsl_to_rgb(hsl):
    """
    Returns an RGB object equivalent to hsl

    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV

    Parameter hsl: the color to convert to a RGB object
    Precondition: hsl is an HSL object.
    """
    h = hsl.hue
    s = hsl.saturation
    l = hsl.lightness

    hi = math.floor(h / 60)
    f = h / 60 - hi
    c = min(l, 1-l) * s
    p = l + c
    q = l - c
    u = l - (1-(2*f)) * c
    v = l + (1-(2*f)) * c

    if hi == 0:
        r = p
        g = u
        b = q
    elif hi == 1:
        r = v
        g = p
        b = q
    elif hi == 2:
        r = q
        g = p
        b = u
    elif hi == 3:
        r = q
        g = v
        b = p
    elif hi == 4:
        r = u
        g = q
        b = p
    elif hi == 5:
        r = p
        g = q
        b = v

    r = round(r * 255)
    g = round(g * 255)
    b = round(b * 255)

    return introcs.RGB(r,g,b)


def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast

    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart,
    with all values becoming 0 or 1 when contrast = 1.

    Parameter value: the value to adjust
    Precondition: value is a float in 0..1

    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    x = value #0.1
    c = contrast #-0.5

    if -1 <= c < 1 and x < (0.25 + (0.25 * c)):
        y = ((1-c)/(1+c))*x
    elif -1 <= c < 1 and (x > 0.75 - (0.25 * c)):
        y = ((1-c)/(1+c))*(x-((3-c)/4))+((3+c)/4)
    elif -1 <= c < 1:
        y = ((1+c)/(1-c))*(x-((1+c)/4))+((1-c)/4)
    elif c == 1 and x >= 0.5:
        y = 1
    elif c == 1:
        y = 0

    return y


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb

    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.

    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object

    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    rgb.red = round((contrast_value(rgb.red / 255, contrast)) * 255)
    rgb.green = round((contrast_value(rgb.green / 255, contrast)) * 255)
    rgb.blue = round((contrast_value(rgb.blue / 255, contrast)) * 255)
