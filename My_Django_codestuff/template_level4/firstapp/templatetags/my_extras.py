from django import template
register=template.Library()


def appendname(value,name_para):
    """
    append name in value
    """
    return value+" "+name_para

register.filter('appendname',appendname)
