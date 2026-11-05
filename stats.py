def most_expensive(prices):
    """Price of the most expensive item,none for an empty cart"""
    if not prices:
        return None
    return max(prices)