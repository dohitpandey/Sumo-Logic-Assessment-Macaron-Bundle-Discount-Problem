# Sumo Logic Assessment – Macaron Bundle Discount Problem

This repository contains a solution to the **Macaron Bundle Discount Problem** using Python, asked in the **Sumo Logic coding assessment**.

---

## Problem Description

You are given a list of macarons, each represented by its **flavor**. All macarons have the same **unit price**.

You can form **bundles (sets)** of macarons with **up to 5 macarons per set**. Each bundle can contain **any number of macarons per flavor**, but the **discount is applied per bundle based on the number of distinct flavors** in that bundle:

| Unique Flavors in Bundle | Discount |
|---------------------------|----------|
| 1                         | 0%       |
| 2                         | 10%      |
| 3                         | 20%      |
| 4                         | 30%      |
| 5                         | 40%      |

Your goal is to **minimize the total price** by grouping macarons into bundles that maximize the discount.

### Function Signature

```python
def computeTotalPrice(unit_price: int, macarons: List[str]) -> Union[int, str]:
```

---

## Approach to Macaron Bundle Discount Problem

### Step-by-Step Breakdown

1. **Count the macarons by flavor**  
   Use `collections.Counter` to get the frequency of each flavor.

2. **Validate the input**  
   If there are more than 5 distinct flavors, return an error.

3. **Greedy bundling**  
   While there are macarons left:
   - Filter out flavors with zero count.
   - Count how many distinct flavors are available.
   - Find the minimum count among those flavors.
   - Form `least_count` bundles using all available distinct flavors.
   - Apply the corresponding discount for each bundle.
   - Subtract `least_count` from each flavor used.

4. **Accumulate the total price**  
   Multiply the number of macarons in each bundle by the unit price and apply the discount.

### Time & Space Complexity

**Overall Time Complexity:**

\[
O(n)
\]

**Overall Space Complexity:**  

\[
O(n)
\]

## Why This Works

- The greedy approach ensures that we always form the largest possible bundle of distinct flavors first, which yields the highest discount.
- Since the number of distinct flavors is capped at 5, operations on the flavor count dictionary are effectively constant time.
- The algorithm is efficient and scalable for large input sizes, as long as the flavor constraint is respected.

## Edge Cases Handled

- More than 5 distinct flavors → returns error
- Empty macaron list → returns 0
- All macarons of the same flavor → no discount
- Uneven distribution of flavors → bundles formed optimally

## Author

Written by Dohit Pandey for coding assessment of **Sumo Logic**.
