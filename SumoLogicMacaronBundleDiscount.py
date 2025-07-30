from collections import Counter


def computeTotalPrice(unit_price: int, macarons: list):
    # Discount mapping based on number of distinct flavors in a set
    discounts = {
        1: 1.0,  # no discount
        2: 0.9,  # 10% discount
        3: 0.8,  # 20% discount
        4: 0.7,  # 30% discount
        5: 0.6  # 40% discount
    }

    # Count how many macarons of each flavor are present
    distinct_macarons_counts = Counter(macarons)  # both time and space complexity O(n)

    # Validate input: no more than 5 distinct flavors allowed
    if len(distinct_macarons_counts) > 5:
        return "wrong input, can't have more than 5 distinct flavours of macarons"

    total_price = 0

    # Continue grouping until all macarons are processed
    while len(distinct_macarons_counts) != 0:  # <O(n)

        # Remove flavors with zero count (already used up)
        distinct_macarons_counts = {key: value for key, value in distinct_macarons_counts.items() if value > 0}  # O(5)

        # If all counts are zero, break the loop
        if len(distinct_macarons_counts) == 0:
            break

        # Number of distinct flavors in the current bundle
        distinct_macarons = len(distinct_macarons_counts)

        # Find the smallest count among the available flavors
        # This determines how many full sets we can make with these distinct flavours
        least_count = min(distinct_macarons_counts.values())  # O(5)

        # if distinct_macarons == 1 and least_count >= 5:
        #     return "wrong input, can't have more than 5 macarons of the same flavour in a set"

        # Calculate subtotal for these sets with applicable discount
        sub_total = (least_count * unit_price * distinct_macarons *
                     discounts[distinct_macarons])

        total_price += sub_total

        # Reduce the count of each flavor used in the current bundle
        for macaron in distinct_macarons_counts:  # O(5)
            distinct_macarons_counts[macaron] -= least_count
    return total_price


# Test cases to validate the function
if __name__ == '__main__':
    print(computeTotalPrice(10, ['a', 'b', 'c', 'd', 'e', 'f', 'g']))  # Invalid: >5 flavors
    print(computeTotalPrice(10, ['a', 'b', 'c', 'd', 'e']))  # One set of 5 → 40% off
    print(computeTotalPrice(10, ['a', 'b', 'c']))  # One set of 3 → 20% off
    print(computeTotalPrice(10, ['a', 'b']))  # One set of 2 → 10% off
    print(computeTotalPrice(10, ['a']))  # One macaron → no discount
    print(computeTotalPrice(10, []))  # No macarons → total = 0
    print(computeTotalPrice(10, ['a', 'b', 'c', 'd', 'e', 'e', 'c']))  # One set of 5, one of 2
    print(computeTotalPrice(10, ['a', 'a', 'a']))  # One flavor only → no discount
    print(computeTotalPrice(10, ['a', 'b', 'c', 'd', 'f', 'b', 'b', 'b', 'b', 'b']))  # Multiple sets
