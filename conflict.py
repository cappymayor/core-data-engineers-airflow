import logging
from calendar import monthrange
from datetime import datetime, timedelta

import pandas as pd
from airflow.models import Variable

logger = logging.getLogger(__name__)


def diff_date(date2: datetime, date1: datetime = datetime.today()):
    """This function compares 3 dates, date1 minus date2, and returns the difference in years.
    Both dates have to be datetime.datetime type.

    Args:
        date2 (datetime)
        date1 (datetime, optional):Defaults to datetime.today().

    Returns:
        [type]: [description]
    """

    date_diff = date1 - date2

    return date_diff


def get_hours(config_variable_name, delta_hours=1, end_hour_delta=0):
    config = Variable.get(config_variable_name, deserialize_json=True, default_var={})
    d_start_at = datetime.utcnow().replace(
        minute=0,
        second=0,
        microsecond=0) - timedelta(hours=delta_hours)
    d_end_at = datetime.utcnow().replace(
        minute=0,
        second=0,
        microsecond=0) - timedelta(hours=end_hour_delta)
    starting_at = config.get('start_at') or d_start_at
    ending_at = config.get('end_at') or d_end_at

    return pd.date_range(starting_at, ending_at, freq='H')


def requests_date_handler(obj):
    if isinstance(obj, (datetime, datetime.date)):
        return obj.isoformat()


def convert_unix_ts(unix_ts: int, ts_format: str = '%Y-%m-%d %H:%M:%S') -> str:
    """Given a unix timstamp, this function converts it to the desired string using datetime lib
    Default is YYYY-MM-DD HH:MM:SS

    Args:
        unix_ts = Timestamp in unix time format
        tstamp_format = Output timestamp format

    Returns:
        Regular timestamp string
    """

    return datetime.utcfromtimestamp(unix_ts).strftime(ts_format)


def get_last_day_of_month(month: str, year: str) -> str:
    """Returns the last day of the month based on the year and the month passed as arguments.

    Args:
        month (str): format 'mm'
        year (str): format 'yyym'

    Returns:
        str: last day of the month
    """
    return str(monthrange(str(year), int(month))[1])