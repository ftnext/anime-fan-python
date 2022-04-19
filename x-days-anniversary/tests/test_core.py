from datetime import date
from unittest import TestCase

from src.core import XthDayCount


class XthDayCountTestCase(TestCase):
    def test_calculate_count(self):
        sut = XthDayCount(date(2021, 10, 29))

        actual = sut(date(2021, 11, 4))

        # 2021/10/29の次の週が2021/11/5なので、2021/11/4は7日目
        self.assertEqual(actual, 7)
