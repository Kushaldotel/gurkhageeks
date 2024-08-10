
from datetime import timedelta, datetime
from django.utils import timezone

def start_and_end_days_of_week():
    today= timezone.now().date()
    start_day= today - timedelta(today.weekday())
    end_day= start_day + timedelta(days=6)
    return start_day, end_day