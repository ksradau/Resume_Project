from datetime import date
from datetime import datetime

from delorean import Delorean


def utcnow() -> datetime:
    return Delorean().datetime