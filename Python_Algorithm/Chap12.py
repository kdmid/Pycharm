from Ch12_Graph import NumIslands
from Ch12_Graph import LetterCombinations
from Ch12_Graph import Permulations
from Ch12_Graph import Combinations
from Ch12_Graph import CombinationSum
from Ch12_Graph import Subsets
from Ch12_Graph import ReconstructItinerary
from Ch12_Graph import CourseSchedule

nil = NumIslands.Solution()
lcp = LetterCombinations.Solution()
pml = Permulations.Solution()
cbn = Combinations.Solution()
cbs = CombinationSum.Solution()
sub = Subsets.Solution()
rci = ReconstructItinerary.Solution()
csd = CourseSchedule.Solution()

# Question 32
if __name__ == '__main__':
    print(nil.numIslands([["1","1","0","0","0"],
                          ["1","1","0","0","0"],
                          ["0","0","1","0","0"],
                          ["0","0","0","1","1"]]))

# Question 33
if __name__ == '__main__':
    print(lcp.letterCombinations("23"))

# Question 34
if __name__ == '__main__':
    print(pml.permute1([1,2,3]))

# Question 35
if __name__ == '__main__':
    print(cbn.combine1(4,2))

# Question 36
if __name__ == '__main__':
    print(cbs.combinationSum([2, 3, 6, 7],7))
    print(cbs.combinationSum([2, 3, 5], 8))

# Question 37
if __name__ == '__main__':
    print(sub.subsets([1,2,3]))

# Question 38
if __name__ == '__main__':
    print(rci.findItinerary1([["MUC","LHR"],
                              ["JFK","MUC"],
                              ["SFO","SJC"],
                              ["LHR","SFO"]]))
    print(rci.findItinerary2([["JFK", "SFO"],
                              ["JFK", "ATL"],
                              ["SFO", "ATL"],
                              ["ATL", "JFK"],
                              ["ATL","SFO"]]))

# Question 39
if __name__ == '__main__':
    print(csd.canFinish1(2,[[0,1]]))
    print(csd.canFinish2(2,[[1,0],[0,1]]))