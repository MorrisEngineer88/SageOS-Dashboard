# lunar_phase.py
import math
import datetime

def get_moon_phase(date):
    """Returns moon phase name based on date."""
    diff = date - datetime.datetime(2001, 1, 1)
    days = diff.days + (diff.seconds / 86400)
    lunations = days / 29.53058867
    phase_index = int((lunations % 1) * 8)

    phases = [
        "New Moon", "Waxing Crescent", "First Quarter",
        "Waxing Gibbous", "Full Moon", "Waning Gibbous",
        "Last Quarter", "Waning Crescent"
    ]
    return phases[phase_index]
