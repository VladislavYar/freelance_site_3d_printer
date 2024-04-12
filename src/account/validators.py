from datetime import date, timedelta

from django.conf import settings


def validate_min_year() -> date:
    """Возвращает дату на 150 лет назад от сегодняшней."""
    return date.today() - timedelta(days=settings.YEARS_150_IN_DAYS)
