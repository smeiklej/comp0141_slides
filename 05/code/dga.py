
import datetime
import random
import time

def generate_domain(year, month, day, sec):
    """Generate a domain name for the given date."""
    domain = ""

    for i in range(16):
        year = ((year ^ 8 * year) >> 11) ^ ((year & 0xFFFFFFF0) << 17)
        month = ((month ^ 4 * month) >> 25) ^ 16 * (month & 0xFFFFFFF8)
        day = ((day ^ (day << 13)) >> 19) ^ ((day & 0xFFFFFFFE) << 12)
        sec = ((sec ^ (sec << 20)) >> 9) ^ ((sec & 0xFFFFFFFA) << 19)
        domain += chr(((year ^ month ^ day ^ sec) % 25) + 97)

    return domain + ".com"

i = 0
while i < 20:
    i += 1
    now = datetime.datetime.now()
    y = now.year
    m = now.month
    d = now.day
    s = now.second

    print generate_domain(y, m, d, s)
    time.sleep(random.random())
