#Time = O(n log(n)) and space = O(n)
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cityOne = [i for i, j in costs]
        diff = [j - i for i, j in costs]
        return sum(cityOne) + sum(sorted(diff)[0:len(costs)//2])
        