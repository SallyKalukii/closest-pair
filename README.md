# Closest Pair of Points Algorithm

This Python script implements the **Closest Pair of Points** problem, which aims to find the closest pair of points in a set of 2D points. The algorithm utilizes a **divide-and-conquer** approach, improving the performance over the brute-force method, especially for large datasets.

## Overview

Given a set of 2D points, the task is to find the closest pair of points and return their Euclidean distance. The script uses the following key techniques:

- **Brute-force approach** for small datasets (when the number of points is less than or equal to 3).
- **Divide-and-conquer approach** (EfficientClosestPair) for larger datasets by recursively splitting the points into two halves and combining results.
- **Merge step** to consider points that lie near the dividing line and may form a closer pair.

The Euclidean distance between two points \((x_1, y_1)\) and \((x_2, y_2)\) is calculated as:

\[
\text{Distance} = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

## Code Explanation

### Key Functions:

1. **`brute_force(P)`**
   - Calculates the closest pair of points using the brute-force method. It checks every pair of points and returns the smallest distance.
   
2. **`euclidean_distance(p1, p2)`**
   - Computes the Euclidean distance between two points `p1` and `p2`.

3. **`EfficientClosestPair(P, Q)`**
   - The divide-and-conquer approach that splits the points into two halves and recursively finds the closest pair in each half. It also handles the merge step to consider points close to the dividing line.

4. **`closest_pair(P)`**
   - This is the main function that sorts the points by both the x and y coordinates and calls the `EfficientClosestPair` function to find the closest pair.

### Example Usage

```python
points = [(1, 2), (4, 4), (2, 5), (8, 8), (3, 1), (5, 7)]
min_distance = closest_pair(points)
print(f"The closest pair distance is: {min_distance}")
```
### Dependencies 
This script requires Python’s math module for calculating the square root of the distances. The math module is part of Python's standard library, so no external dependencies need to be installed.

### Conclusion
This implementation efficiently solves the Closest Pair of Points problem using a combination of brute-force and divide-and-conquer strategies. The algorithm is optimized for large sets of points, improving performance compared to the traditional brute-force method. For small datasets (<= 3 points), the brute-force method is used for simplicity, while the divide-and-conquer method is employed for larger datasets to ensure optimal performance.

This solution works well for sets of points with known constraints, such as when the input is sorted by both the x and y coordinates. For unsorted input, sorting steps are included at the beginning of the algorithm.
