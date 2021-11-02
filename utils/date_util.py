import datetime
from typing import List


def generate_date_range(from_date: str, to_date: str) -> List[str]:
	start = datetime.datetime.strptime(from_date, "%Y-%m-%d")
	end = datetime.datetime.strptime(to_date, "%Y-%m-%d")
	date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days + 1)]

	all_dates = [date.strftime("%Y-%m-%d") for date in date_generated]
	return all_dates


def weekday_parser(date: str) -> int:
	weekday_ix = datetime.datetime.strptime(date, "%Y-%m-%d").weekday()
	return weekday_ix
