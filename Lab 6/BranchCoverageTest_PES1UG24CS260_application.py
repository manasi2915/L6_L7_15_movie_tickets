import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ---------- ticket_price: every if / elif / else outcome ----------

@pytest.mark.parametrize("seat, age, hour, weekend, expected", [
    ("regular", 25, 15, False, 150),   # afternoon: no time adjustment
    ("regular", 25, 9, False, 100),    # morning branch (hour < 12)
    ("regular", 25, 11, False, 100),   # morning boundary (just below 12)
    ("regular", 25, 12, False, 150),   # boundary: 12 is NOT morning
    ("regular", 25, 17, False, 150),   # boundary: 17 is NOT evening
    ("regular", 25, 18, False, 180),   # evening branch (elif hour >= 18)
    ("regular", 25, 23, False, 180),   # last valid hour
    ("premium", 25, 15, True, 290),    # weekend branch True
    ("premium", 25, 15, False, 250),   # weekend branch False
    ("regular", 2, 15, False, 0),      # age < 3 branch True (free)
    ("regular", 1, 20, True, 0),       # free even with surcharges
    ("regular", 3, 15, False, 75),     # age < 3 False; child boundary
    ("regular", 12, 15, False, 75),    # child (<= 12) branch True
    ("regular", 13, 15, False, 150),   # child branch False
    ("regular", 59, 15, False, 150),   # senior branch False
    ("regular", 60, 15, False, 75),    # senior (>= 60) branch True
    ("recliner", 5, 9, True, 195),     # morning + weekend + child
    ("recliner", 30, 20, True, 470),   # evening + weekend + adult
])
def test_ticket_price_branches(seat, age, hour, weekend, expected):
    assert ticket_price(seat, age, hour, weekend) == expected


@pytest.mark.parametrize("seat, age, hour", [
    ("vip", 25, 15),       # unknown seat -> raise
    ("regular", 25, -1),   # hour below range -> raise
    ("regular", 25, 24),   # hour above range -> raise
])
def test_ticket_price_invalid_inputs(seat, age, hour):
    with pytest.raises(ValueError):
        ticket_price(seat, age, hour, False)


# ---------- group_discount: every if / elif / else outcome ----------

@pytest.mark.parametrize("tickets, student, expected", [
    (1, False, 0),     # below 5 -> else branch
    (4, False, 0),     # boundary just below 5
    (5, False, 10),    # elif (>= 5) branch True
    (9, False, 10),    # boundary just below 10
    (10, False, 15),   # if (>= 10) branch True
    (12, False, 15),
    (2, True, 0),      # student bonus skipped: discount is 0
    (4, True, 0),      # student bonus skipped: discount is 0 (boundary)
    (5, True, 15),     # student bonus applied: 10 + 5
    (10, True, 20),    # student bonus applied: 15 + 5
])
def test_group_discount_branches(tickets, student, expected):
    assert group_discount(tickets, student) == expected


@pytest.mark.parametrize("tickets", [0, -2])
def test_group_discount_no_tickets_raises(tickets):
    with pytest.raises(ValueError):
        group_discount(tickets, False)


# ---------- snack_combo: every size branch, with and without coupon ----------

@pytest.mark.parametrize("size, coupon, expected", [
    ("small", False, 120),   # small branch, coupon False
    ("small", True, 70),     # small branch, coupon True
    ("medium", False, 180),  # medium branch, coupon False
    ("medium", True, 130),   # medium branch, coupon True
    ("large", False, 250),   # else branch, coupon False
    ("large", True, 200),    # else branch, coupon True
    ("jumbo", False, 250),   # unknown size falls to else
])
def test_snack_combo_branches(size, coupon, expected):
    assert snack_combo(size, coupon) == expected
