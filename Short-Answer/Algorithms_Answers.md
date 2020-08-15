#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The while loop is O(n^3) complexity, but the inside is O(n^2). Since the inside controls how much each loop iterates through, we have to divide the complexities.
So our TOTAL complexity is O(n^3/n^2) = O(n)

if n = 1; we iterate once. If n = 10; we iterate 10 times. If n = 100; we iterate 100 times. Etc.

b) O(n^2) complexity. The while loop is O(n/2) complexity, but is nested inside a for loop that has O(n) complexity. Therefore it's O(n^2)
*We ignore the denominator in n/2

c) O(n) complexity. Every recursion loop the value of the input (aka bunnies) is decreasing by 1. So no matter how many inputs there are, the recursion loop will grow by n.

## Exercise II

givens:
- n = story building
- "plenty of eggs" -> question: how many is plenty? enough for each floor, or more than we'd need?
- Egg is broken if thrown off floor "f" or higher. floors under "f" won't break
- Find "f", so that we minimize dropped + broken eggs.

Strategy 1 (minimize dropped eggs):
- Start at floor 1 and drop an egg.
- If the egg DOES NOT break, go up a floor.
- Continue until the dropped egg breaks.
- Return current floor number as "f"
- Complexity: O(n). If "f" is low then we'd find it quickly, but if "f" was high then it would take awhile. Benefit is we only break 1 egg on the first floor that the egg breaks.

Strategy 2 (minimize time/iterations):
- Find the middle floor (aka n/2). IF there are odd number of floors middle is rounded up.
- Drop an egg from this floor (we will call it the "test floor").
    - If egg breaks, go DOWN half the distance (test floor - bottom floor)
        - Maximum floor becomes the test floor
        - Bottom floor is still bottom floor
        - aka: testing within [0 : n/2]
    - If egg DOES NOT break, go UP half the distance (maximum floor - test floor)
        - Maximum floor stays as the maximum floor
        - Bottom floor becomes the test floor
        - aka: testing within [n/2 : n]
- Repeat this process until the Bottom Floor and the Maximum Floor are within 1 floor of each other, and the egg breaks on one and not the other.
- Complexity is O(n/2). If "f" is low or high, it will cut the iterations down by half to find it. But we would break a few eggs to test this out.

Benefits of 1 vs. 2:
- Strategy 1 is better than 2 when n is very large, and the floor "f" is very small. Ie: breaks on floor 2, but it's a 100 story building.
- Strategy 2 is better than 1 when the floor "f" is fairly high up, and significantly better than 1 if "f" is more than half of n.

- Strategy 1 breaks 1 egg.
- Strategy 2 will break multiple eggs.
