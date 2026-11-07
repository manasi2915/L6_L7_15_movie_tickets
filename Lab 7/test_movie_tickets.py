from hypothesis import given, strategies as st
from movie_tickets import parse_seat, total_price, average_rating

# A ValueError is an intentional, controlled rejection of bad input, so it passes.
# Any other exception (TypeError, IndexError, ZeroDivisionError, ...) is a bug.

@given(st.text() | st.none())
def test_parse_seat_no_crash(s):
    try:
        parse_seat(s)
    except ValueError:
        pass
    except Exception as e:
        assert False, f"parse_seat crashed with {type(e).__name__}: {e} on input {s!r}"

@given(st.text() | st.none())
def test_total_price_no_crash(s):
    try:
        total_price(s)
    except ValueError:
        pass
    except Exception as e:
        assert False, f"total_price crashed with {type(e).__name__}: {e} on input {s!r}"

@given(st.text() | st.none())
def test_average_rating_no_crash(s):
    try:
        average_rating(s)
    except ValueError:
        pass
    except Exception as e:
        assert False, f"average_rating crashed with {type(e).__name__}: {e} on input {s!r}"
