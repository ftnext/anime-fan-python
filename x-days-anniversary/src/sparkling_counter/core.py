from datetime import date


class IllegalDayCountError(Exception):
    ...


class ArrivingTheDayException(Exception):
    ...


class XthDayCount:
    def __init__(self, anniversary: date) -> None:
        self._anniversary = anniversary

    def __call__(self, point: date) -> int:
        delta = point - self._anniversary
        return delta.days + 1


class DayCountDown:
    def __init__(self, goal: date, *, include: bool):
        self._goal = goal
        self._include = include

    def __call__(self, point: date) -> int:
        delta = self._goal - point
        day_count = delta.days
        if self._include:
            day_count += 1

        if not self._include and day_count == 0:
            raise ArrivingTheDayException
        if day_count <= 0:
            raise IllegalDayCountError

        return day_count
