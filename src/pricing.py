
def apply_discount(price, percent):
    if price < 0:
        raise ValueError("Price cannot be negative")

    if not 0 <= percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    return round(price * (1 - percent / 100), 2)
