# -*- coding: utf-8 -*-


r"""
>>> format(my_birthday, '')
''
>>> format(my_birthday, 'a')
'p.m.'
>>> format(my_birthday, 'A')
'PM'
>>> format(my_birthday, 'd')
'08'
>>> format(my_birthday, 'j')
'8'
>>> format(my_birthday, 'l')
'Sunday'
>>> format(my_birthday, 'L')
'False'
>>> format(my_birthday, 'm')
'07'
>>> format(my_birthday, 'M')
'Jul'
>>> format(my_birthday, 'b')
'jul'
>>> format(my_birthday, 'n')
'7'
>>> format(my_birthday, 'N')
'July'
>>> no_tz or format(my_birthday, 'O') == '+0100'
True
>>> format(my_birthday, 'P')
'10 p.m.'
>>> no_tz or format(my_birthday, 'r') == 'Sun, 8 Jul 1979 22:00:00 +0100'
True
>>> format(my_birthday, 's')
'00'
>>> format(my_birthday, 'S')
'th'
>>> format(my_birthday, 't')
'31'
>>> no_tz or format(my_birthday, 'T') == 'CET'
True
>>> no_tz or format(my_birthday, 'U') == '300531600'
True
>>> format(my_birthday, 'w')
'0'
>>> format(my_birthday, 'W')
'27'
>>> format(my_birthday, 'y')
'79'
>>> format(my_birthday, 'Y')
'1979'
>>> format(my_birthday, 'z')
'189'
>>> no_tz or format(my_birthday, 'Z') == '3600'
True

>>> no_tz or format(summertime, 'I') == '1'
True
>>> no_tz or format(summertime, 'O') == '+0200'
True
>>> no_tz or format(wintertime, 'I') == '0'
True
>>> no_tz or format(wintertime, 'O') == '+0100'
True

>>> format(my_birthday, r'Y z \C\E\T')
'1979 189 CET'

>>> format(my_birthday, r'jS o\f F')
'8th of July'

# >>> translation.activate('el-gr')

>>> format(my_birthday, r'd {Fp} Y', 'el_gr')
u'08 \u0399\u03bf\u03c5\u03bb\u03af\u03bf\u03c5 1979'

>>> format(my_birthday, r'{FULL_DATE}', 'el_gr')
u'Sunday, 8 \u0399\u03bf\u03c5\u03bb\u03af\u03bf\u03c5, 1979'

>>> format(my_birthday, r'{ABBR_DATE}', 'el_gr')
'8 Jul, 1979'

>>> format(my_birthday, r'{NUM_DATE}', 'el_gr')
'8/7/1979'

>>> format(my_birthday, r'{FULL_DATETIME}', 'el_gr')
u'Sunday, 8 \u0399\u03bf\u03c5\u03bb\u03af\u03bf\u03c5, 1979, 10 p.m.'

>>> format(my_birthday, r'{ABBR_DATETIME}', 'el_gr')
'8 Jul, 1979, 10 p.m.'

>>> format(my_birthday, r'{NUM_DATETIME}', 'el_gr')
'8/7/1979, 10 p.m.'

"""

from django.utils import  translation
import local_dateformat
import datetime, os, time

format = local_dateformat.format
os.environ['TZ'] = 'Europe/Copenhagen'
translation.activate('en-us')

try:
    time.tzset()
    no_tz = False
except AttributeError:
    no_tz = True

my_birthday = datetime.datetime(1979, 7, 8, 22, 00)
my_birthday2 = datetime.datetime(1979, 7, 8, 22, 30)
summertime = datetime.datetime(2005, 10, 30, 1, 00)
wintertime = datetime.datetime(2005, 10, 30, 4, 00)
