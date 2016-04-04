from django import template
register = template.Library()
import datetime

@register.filter(name="longTime")
def longTime(aTime):
    return aTime.strftime("%m/%d/%Y %I:%M%p")

@register.filter(name="teaLower")
def teaLower(s):
    s = str(s)
    s = s.lower()
    return s
