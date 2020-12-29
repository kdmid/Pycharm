from Ch6_String import Palindrome
from Ch6_String import ReverseString
from Ch6_String import RecorderLogFiles
from Ch6_String import MostCommonWord
from Ch6_String import GroupAnagrams
from Ch6_String import LongestPalindrome

pds = Palindrome.Solution()
rvs = ReverseString.Solution()
rlf = RecorderLogFiles.Solution()
mcw = MostCommonWord.Solution()
gag = GroupAnagrams.Solution()
lpd = LongestPalindrome.Solution()

# Question 1
if __name__ == '__main__':
  print(pds.isPalindrome1("A man, a plan, a canal: Panama"))
  print(pds.isPalindrome2("race a car"))

# Question 2
if __name__ == '__main__':
  print(rvs.reverseString1(["h", "e", "l", "l", "o"]))
  print(rvs.reverseString1(["H", "a", "n", "n", "a", "H"]))

# Question 3
if __name__ == '__main__':
  print(rlf.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))

# Question 4
if __name__ == '__main__':
    print(mcw.mostCommonWord(paragraph="Bob hit a ball, the hit BALL flew far after it was hit.",
                                   banned=["hit"]))

# Question 5
if __name__ == '__main__':
    print(gag.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Question 6
if __name__ == '__main__':
    print(lpd.longestPalindrome("babad"))
    print(lpd.longestPalindrome("cbbd"))
    print(lpd.longestPalindrome("gfioabaoidt"))