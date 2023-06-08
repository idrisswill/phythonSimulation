from datetime import datetime
import itertools
import datetime, time
from IPython.display import display, Image, Markdown, HTML

_start_time = None
_end_time = None
_chrono_start = None
_chrono_stop = None


def hdelay(sec):
    return str(datetime.timedelta(seconds=int(sec)))


# Return human delay like 01:14:28 543ms
# delay can be timedelta or seconds
def hdelay_ms(delay):
    if type(delay) is not datetime.timedelta:
        delay = datetime.timedelta(seconds=delay)
    sec = delay.total_seconds()
    hh = sec // 3600
    mm = (sec // 60) - (hh * 60)
    ss = sec - hh * 3600 - mm * 60
    ms = (sec - int(sec)) * 1000
    return f'{hh:02.0f}:{mm:02.0f}:{ss:02.0f} {ms:03.0f}ms'


def chrono_start():
    global _chrono_start, _chrono_stop
    _chrono_start = time.time()


# return delay in seconds or in humain format
def chrono_stop(hdelay=False):
    global _chrono_start, _chrono_stop
    _chrono_stop = time.time()
    sec = _chrono_stop - _chrono_start
    if hdelay: return hdelay_ms(sec)
    return sec


def chrono_show():
    print('\nDuration : ', hdelay_ms(time.time() - _chrono_start))
