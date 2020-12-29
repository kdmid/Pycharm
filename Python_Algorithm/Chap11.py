from Ch11_HashTable import DesignHashMap
from Ch11_HashTable import JewelsInStone
from Ch11_HashTable import LongestSubstring
from Ch11_HashTable import TopKFrequent

dhm = DesignHashMap.MyHashMap()
jis = JewelsInStone.Solution()
lss = LongestSubstring.Solution()
tkf = TopKFrequent.Solution()

# Question 28
if __name__ == '__main__':
    dhm.put(1,1)
    dhm.put(2,2)
    print(dhm.get(1))
    print(dhm.get(3))
    dhm.put(2,1)
    print(dhm.get(2))
    dhm.remove(2)
    print(dhm.get(1))

# Question 29
if __name__ == '__main__':
    print("Q29:",jis.numJewelsInStones3("aA", "aAAbbbb"))

# Question 30
if __name__ == '__main__':
    print(lss.lengthOfLongestSubstring("abcabcbb"))
    print(lss.lengthOfLongestSubstring("bbbbb"))
    print("Q:30",lss.lengthOfLongestSubstring("pwwkew"))

# Question 31
if __name__ == '__main__':
    print(tkf.topKFrequent1([1,1,1,2,2,3],2))