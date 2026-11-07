def parse_seat(seat):
    if not isinstance(seat, str):
        raise ValueError("seat must be a string such as H12")
    seat = seat.strip()
    if len(seat) < 2:
        raise ValueError(f"invalid seat: {seat!r} (expected a letter followed by a number, e.g. H12)")
    row, number = seat[0], seat[1:]
    if not (row.isascii() and row.isalpha()):
        raise ValueError(f"invalid seat row: {row!r}")
    if not (number.isascii() and number.isdigit()):
        raise ValueError(f"invalid seat number: {number!r}")
    return row.upper(), int(number)

def total_price(prices_csv):
    if not isinstance(prices_csv, str):
        raise ValueError("prices must be a comma-separated string such as 150,250,400")
    prices = []
    for p in prices_csv.split(','):
        p = p.strip()
        if not (p.isascii() and p.isdigit()):
            raise ValueError(f"invalid ticket price: {p!r}")
        prices.append(int(p))
    try:
        return round(sum(prices) * 1.18, 2)
    except OverflowError:
        raise ValueError("total price is too large to compute")

def average_rating(ratings):
    if not isinstance(ratings, str):
        raise ValueError("ratings must be a string such as 4 5 3")
    tokens = ratings.split()
    if not tokens:
        raise ValueError("no ratings given")
    values = []
    for r in tokens:
        if not (r.isascii() and r.isdigit()):
            raise ValueError(f"invalid rating: {r!r}")
        value = int(r)
        if not 1 <= value <= 5:
            raise ValueError(f"rating must be between 1 and 5, got {value}")
        values.append(value)
    return round(sum(values) / len(values), 1)

def main():
    try:
        print("==== Running parse_seat ====")
        user_input = input("Enter a seat number (e.g. H12): ")
        result = parse_seat(user_input)
        print("Row and Seat:", result)
    except ValueError as e:
        print("Error:", e)

    try:
        print("\n==== Running total_price ====")
        user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
        result = total_price(user_input)
        print("Total with GST:", result)
    except ValueError as e:
        print("Error:", e)

    try:
        print("\n==== Running average_rating ====")
        user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
        result = average_rating(user_input)
        print("Average Rating:", result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()