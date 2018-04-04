from django import template
from datetime import datetime
register=template.Library()

def timedifference(value,firsttime):
    print(firsttime)
    """
    return difference of last_submit_time and firsttime
    """
    return value - firsttime

register.filter('time_difference',timedifference)
