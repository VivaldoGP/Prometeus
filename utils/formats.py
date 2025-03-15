from datetime import datetime


def to_iso_8601(date: str):
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        return date_obj.strftime("%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD"