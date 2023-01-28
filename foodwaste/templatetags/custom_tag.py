from django import template
from foodwaste.models import *
from datetime import date, datetime

register = template.Library()

@register.filter(name = 'notification')
def notification(obj):
    foodrequest  = Foodrequests.objects.filter(status=None)
    return foodrequest

@register.simple_tag()
def notificationcount(*args, **kwargs):
    foodrequestcount  = Foodrequests.objects.filter(status=None).count()
    return foodrequestcount

@register.simple_tag
def update_variable(value):
    """Allows to update existing variable in template"""
    return value+1

@register.simple_tag
def checkdate(self):
    valuetocheck = self.strftime("%Y-%m-%d %H:%M:%S.%f")
    # return valuetocheck
    valuetocheckwith = date.today().strftime("%Y-%m-%d %H:%M:%S.%f")
    if  valuetocheck < valuetocheckwith:
        return False
    return True
