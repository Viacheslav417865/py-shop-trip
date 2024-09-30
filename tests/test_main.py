from datetime import datetime
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import MagicMock
from app.main import shop_trip


def test_shop_trip_output(monkeypatch):
    mocked_datetime = MagicMock(wraps=datetime)
    mocked_datetime.now.return_value = datetime(2021, 1, 4, 12, 33, 41)
    monkeypatch.setattr("datetime.datetime", mocked_datetime)

    shop_trip()

    expected_output = '''
Bob has 55 dollars
Bob's trip to Outskirts Shop costs 28.21
Bob's trip to Shop '24/7' costs 31.48
Bob's trip to Central Shop costs 39.28
Bob rides to Outskirts Shop

Date: 04/01/2021 12:33:41
Thanks, Bob, for your purchase!
4 milk(s) for 12 dollars
2 bread(s) for 2 dollars
5 butter(s) for 12.5 dollars
Total cost is 26.5 dollars
See you again!
Bob rides home
Bob now has 26.79 dollars

Alex has 41 dollars
Alex's trip to Outskirts Shop costs 17.14
Alex's trip to Shop '24/7' costs 15.95
Alex's trip to Central Shop costs 17.98
Alex rides to Shop '24/7'

Date: 04/01/2021 12:33:41
Thanks, Alex, for your purchase!
2 milk(s) for 4 dollars
2 bread(s) for 3.0 dollars
2 butter(s) for 6.4 dollars
Total cost is 13.4 dollars
See you again!
Alex rides home
Alex now has 25.05 dollars

Monica has 12 dollars
Monica's trip to Outskirts Shop costs 15.65
Monica's trip to Shop '24/7' costs 16.84
Monica's trip to Central Shop costs 22.58
Monica doesn't have enough money to make a purchase at Outskirts Shop
'''.strip()

    assert mocked_datetime.now().strftime("%d/%m/%Y %H:%M:%S") == "04/01/2021 12:33:41"
