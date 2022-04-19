from datetime import date


class XthDayCount:
    def __init__(self, anniversary: date) -> None:
        self._anniversary = anniversary

    def __call__(self, point: date) -> int:
        delta = point - self._anniversary
        return delta.days + 1
