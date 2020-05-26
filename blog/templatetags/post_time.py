from django.template.defaultfilters import date, timesince_filter
from django import template

register = template.Library()

time_strings = ['year', 'week', 'day']

@register.filter
def post_time(value, arg):
    """
    timesince_filter formats a date as the time since that date (i.e. "4 days, 6 hours").
    By default this formatting is done between the current time and the 'value'.

    This function converts string obtained by timesince_filter to:
    1. minutes when timesince <  1 hour
    2. if timesince > 1 hour only keeps the hours part
    3. if timesince > 24 hours returns the original date of posting, formatted
    by the 'arg' parameter (achieved using the date filter)

    Use Case:
    Use for mimicing post times used by Facebook, Youtube etc.
    """
    result = timesince_filter(value)

    for string in time_strings:
        if string in result:
            return date(value, arg)

    if 'hour' in result:
        result = result.split(",")[0]
        return result + ' ' + 'ago'

    else:
        return result + ' ' + 'ago'
