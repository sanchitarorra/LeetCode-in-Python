def maxSubarraySumCircular(A):
        currentMax = A[0]
        maxSoFar = A[0]
        currentMin = A[0]
        minSoFar = A[0]
        for num in A[1:]:
            currentMax = max(num, currentMax + num)
            maxSoFar = max(currentMax, maxSoFar)
            currentMin = min(num, currentMin + num)
            minSoFar = min(currentMin, minSoFar)
        if sum(A) == minSoFar:
            return maxSoFar
        return max(maxSoFar, sum(A) - minSoFar)


#test case
# print(maxSubarraySumCircular([5, -3, 5])) output = 10
