import pytest
from api.models import Date
from api.lib.db import drop_all_tables, test_conn, test_cursor, save, find_all


@pytest.fixture()
def clean_tables():
    drop_all_tables(test_conn, test_cursor)

    yield
    drop_all_tables(test_conn, test_cursor)


def test_date_mass_assignment():
    date=Date(month="March", year=2022)
    assert date.__dict__=={"month":"March", "year":2022}

def test_save_date():
    pass


# @pytest.fixture()
# def save_dates():
#     drop_all_tables(test_conn, test_cursor)
#
#     date_1=Date(**{})
#     saved_date_1=save()
#
#     date_2=Date(**{""})
#     saved_date_2=save()
#
#     yield
#     drop_all_tables(test_conn, test_cursor)
#
#
# def test_find_all_dates(save_dates):
#     fishes=find_all(Date, test_conn)
#     assert []==[]

