from datetime import date


class IllegalDayCountError(Exception):
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
        if self._include:
            if self._goal < point:
                raise IllegalDayCountError
        else:
            if self._goal <= point:
                raise IllegalDayCountError

        delta = self._goal - point
        if self._include:
            return delta.days + 1
        return delta.days
