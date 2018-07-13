from django import template
from django.conf import settings
from django.utils import timezone

register = template.Library()


@register.simple_tag
def get_copyright():
    current_year = timezone.now().year
    if hasattr(settings, "COPYRIGHT_START_YEAR"):
        start_year = getattr(settings, "COPYRIGHT_START_YEAR", )
        if not start_year == current_year:
            return "%s - %s" % (str(settings.COPYRIGHT_START_YEAR), str(current_year))
    return str(current_year)