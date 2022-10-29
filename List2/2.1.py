import math
import datetime


def compute_Easter_date(year: int = 1990):
    """ Compute the date of Easter in given year.
    :param year: (int) Year of Easter.
    :return: (str) Day, month and year of Easter.
    """
    if year < 0:
        print("Year can't be minus.")
    else:
        a = year % 19
        b = math.floor(year / 100)
        c = year % 100
        d = math.floor(b / 4)
        e = b % 4
        f = math.floor((b + 8) / 25)
        g = math.floor((b - f + 1) / 3)
        h = (19 * a + b - d - g + 15) % 30
        i = math.floor(c / 4)
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = math.floor((a + 11 * h + 22 * l) / 451)
        p = (h + l - 7 * m + 114) % 31
        day = p + 1
        month = math.floor((h + l - 7 * m + 114) / 31)
        return datetime.date(year, month, day).strftime("%d %B %Y")


