from django import template

register = template.Library()


@register.filter
def str_in_list(string: str, sep: str) -> list:
    """Преоразует строку в список."""
    return string.split(sep)
