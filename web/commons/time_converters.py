import datetime


def datetime_to_date_string(datetime_obj: datetime.datetime) -> str:
    return date_to_string(datetime_obj.date())


def date_to_string(date_obj: datetime.date) -> str:
    return date_obj.strftime('%Y-%m-%d')
