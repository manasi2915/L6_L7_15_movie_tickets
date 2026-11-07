import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ---------- ticket_price: line coverage ----------

def test_unknown_seat_raises():
    with pytest.raises(ValueError):
        ticket_price("vip", 25, 15, False)


def test_invalid_show_hour_raises():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, 24, False)


def test_morning_show_discount():
    assert ticket_price("regular", 25, 9, False) == 100


def test_evening_show_surcharge():
    assert ticket_price("regular", 25, 19, False) == 180


def test_weekend_surcharge():
    assert ticket_price("premium", 25, 15, True) == 290


def test_infant_is_free():
    assert ticket_price("recliner", 1, 15, False) == 0


def test_child_half_price():
    assert ticket_price("regular", 8, 15, False) == 75


def test_senior_half_price():
    assert ticket_price("regular", 65, 15, False) == 75


# ---------- group_discount: line coverage ----------

def test_no_tickets_raises():
    with pytest.raises(ValueError):
        group_discount(0, False)


def test_small_group_no_discount():
    assert group_discount(2, False) == 0


def test_large_group_discount():
    assert group_discount(12, False) == 15


def test_medium_group_discount():
    assert group_discount(6, False) == 10


def test_student_group_bonus():
    assert group_discount(6, True) == 15


# ---------- snack_combo: line coverage ----------

def test_small_snack():
    assert snack_combo("small", False) == 120


def test_medium_snack():
    assert snack_combo("medium", False) == 180


def test_large_snack_with_coupon():
    assert snack_combo("large", True) == 200
