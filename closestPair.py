import math

def brute_force(P):
    min_distance = float('inf')
    closest_pair = None
    for i in range(len(P)):
        for j in range(i + 1, len(P)):
            dist = euclidean_distance(P[i], P[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (P[i], P[j])
    return min_distance, closest_pair

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def EfficientClosestPair(P, Q):
    n = len(P) #P is list of points sorted by x-coordinate
    
    # Base case
    if n <= 3:
        return brute_force(P)
    
    #recursive case 
    # Step 1: Split P and Q into left and right halves
    mid = n // 2
    Pleft = P[:mid]  # Left half for x
    Pright = P[mid:]  # Right half for x
    Qleft = [p for p in Q if p[0] <= Pleft[-1][0]]  # Left half for y
    Qright = [p for p in Q if p[0] > Pleft[-1][0]]  # Right half for y
    
    #Recursive step which is calling the functions in the function 
    dleft, left_pair = EfficientClosestPair(Pleft, Qleft)
    dright, right_pair = EfficientClosestPair(Pright, Qright)
    
    # taking the minimum distance from the two halves
    d = min(dleft, dright)
    
    # creating a strip of points in Q that are within distance d from the middle line
    m = Pleft[-1][0]  # mid point in p
    S = [p for p in Q if abs(p[0] - m) < d]
    
    # checking the points in the strip for a closer pair
    dminsq = d ** 2
    for i in range(len(S) - 1):
        k = i + 1
        while k < len(S) and (S[k][1] - S[i][1]) ** 2 < dminsq:
            dist = euclidean_distance(S[i], S[k])
            dminsq = min(dist ** 2, dminsq)
            k += 1
    
    # returning the closest pair distance 
    return math.sqrt(dminsq)

def closest_pair(P):
    # Sorting P by x and y coordinates
    P_sorted_by_x = sorted(P, key=lambda p: p[0])
    P_sorted_by_y = sorted(P, key=lambda p: p[1])
    
    return EfficientClosestPair(P_sorted_by_x, P_sorted_by_y)


points = [(1, 2), (4, 4), (2, 5), (8, 8), (3, 1), (5, 7)]
min_distance = closest_pair(points)
print(f"The closest pair distance is: {min_distance}")
