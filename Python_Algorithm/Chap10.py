from Ch10_Deque import DesignCircularDeque as dcd
from Ch10_Deque import MergeKLists as mkl

# Question 26
if __name__ == '__main__':
  d = dcd.MyCircularDeque(3)
  print(d.insertFront(1))
  print(d.insertLast(2))
  print(d.deleteFront())
  print(d.deleteLast())
  print(d.getFront())
  print(d.getRear())
  print(d.isEmpty())
  print(d.isFull())

# Question 27
s = mkl.Solution()
l1 = mkl.ListNode(1)
l1.next = mkl.ListNode(4)
l1.next.next = mkl.ListNode(5)

l2 = mkl.ListNode(1)
l2.next = mkl.ListNode(3)
l2.next.next = mkl.ListNode(4)

l3 = mkl.ListNode(2)
l3.next = mkl.ListNode(6)
answer = s.mergeKLists([l1,l2,l3])
print("\n")
while answer is not None: # None에서 멈춤
  print(f'{answer.val}', end=" ") # f'{}' f-string는 문자열 포매팅
  answer = answer.next # 다음숫자 불러온다