from datetime import date
from unittest import TestCase

from src.core import DayCountDown, XthDayCount


class XthDayCountTestCase(TestCase):
    def test_calculate_count(self):
        sut = XthDayCount(date(2021, 10, 29))

        actual = sut(date(2021, 11, 4))

        # 2021/10/29の次の週が2021/11/5なので、2021/11/4は7日目
        self.assertEqual(actual, 7)

    def test_calculate_with_anniversary_itself(self):
        sut = XthDayCount(date(2022, 4, 19))

        actual = sut(date(2022, 4, 19))

        # 2022/4/19自身は1日目（例えば公開日は初日なので1日目）
        self.assertEqual(actual, 1)


class DayCountDownTestCase(TestCase):
    def test_when_goal_is_not_included(self):
        sut = DayCountDown(date(2022, 1, 8), include=False)

        actual = sut(date(2022, 1, 6))

        # 2022/1/8を含まずに2022/1/6から何日あるか -> 1/6, 1/7の2日
        self.assertEqual(actual, 2)
