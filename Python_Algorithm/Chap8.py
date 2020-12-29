from Ch8_Linked_List import PalindromeList as pll
from Ch8_Linked_List import MergeTwoLists as mtl
from Ch8_Linked_List import ReverseList as rll
from Ch8_Linked_List import AddTwoNumbers as atn
from Ch8_Linked_List import SwapPairs as snp
from Ch8_Linked_List import OddEvenList as oel
from Ch8_Linked_List import ReverseBetween as rbw

# Question 13
if __name__ == '__main__':
  s = pll.Solution()
  li = pll.ListNode(1) # li = [1]
  li.next = pll.ListNode(2) # li = [1,2]
  print(s.isPalindrome1(li))

  li.next.next = pll.ListNode(2) # li = [1,2,2]
  li.next.next.next = pll.ListNode(1) # li = [1,2,2,1]
  print(s.isPalindrome1(li))

# Question 14
if __name__ == '__main__':
  s = mtl.Solution()
  l1 = mtl.ListNode(1)
  l1.next = mtl.ListNode(2)
  l1.next.next = mtl.ListNode(4)

  l2 = mtl.ListNode(1)
  l2.next = mtl.ListNode(3)
  l2.next.next = mtl.ListNode(4)
  answer = s.mergeTwoLists(l1, l2)
  while answer is not None:
    print(f'{answer.val}', end=" ")
    answer = answer.next

# Question 15
s = rll.Solution()
l1 = rll.ListNode(1)
l1.next = rll.ListNode(2)
l1.next.next = rll.ListNode(3)
l1.next.next.next = rll.ListNode(4)
l1.next.next.next.next= rll.ListNode(5)

answer = s.reverseList1(l1)
while answer is not None:
  print(f'{answer.val}', end=" ")
  answer = answer.next

# Question 16
s = atn.Solution()
l1 = atn.ListNode(2)
l1.next = atn.ListNode(4)
l1.next.next = atn.ListNode(3)


l2 = atn.ListNode(5)
l2.next = atn.ListNode(6)
l2.next.next = atn.ListNode(4)

answer = s.addTwoNumbers1(l1,l2)
print("\n")
while answer is not None:
  print(f'{answer.val}', end=" ")
  answer = answer.next

# Question 17
s = snp.Solution()
l1 = snp.ListNode(1)
l1.next = snp.ListNode(2)
l1.next.next = snp.ListNode(3)
l1.next.next.next = snp.ListNode(4)
answer = s.swapPairs3(l1)
print("\n")
while answer is not None:
  print(f'{answer.val}', end=" ")
  answer = answer.next

# Question 18
s = oel.Solution()
l1 = oel.ListNode(1)
l1.next = oel.ListNode(2)
l1.next.next = oel.ListNode(3)
l1.next.next.next = oel.ListNode(4)
l1.next.next.next.next= oel.ListNode(5)
answer = s.oddEvenList(l1)
print("\n")
while answer is not None:
  print(f'{answer.val}', end=" ")
  answer = answer.next

# Question 19
s = rbw.Solution()
l1 = rbw.ListNode(1)
l1.next = rbw.ListNode(2)
l1.next.next = rbw.ListNode(3)
l1.next.next.next = rbw.ListNode(4)
l1.next.next.next.next= rbw.ListNode(5)
answer = s.reverseBetween(l1,2,4)
print("\n")
while answer is not None:
  print(f'{answer.val}', end=" ")
  answer = answer.next