import collections


# Definition for singly-linked list.
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000    # 크기 설정
        self.table = collections.defaultdict(ListNode)    # key 값이 없을 경우 미리 지정해 놓은 초기값을 반환

    # 삽입
    def put(self, key: int, value: int) -> None:
        index = key % self.size   # key가 1000 이 넘어갈 경우 1000으로 나눈뒤 나머지 값을 인덱스로 설정 ex) 1001 -> 1
        # 인덱스에 노드가 없다면 삽입 후 종료
        if self.table[index].value is None:   # 해당 인덱스에서 테이블 값이 비어있다면
            self.table[index] = ListNode(key, value)    # key, value 삽입
            return

        # 인덱스에 노드가 존재하는 경우 연결 리스트 처리
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1

        # 노드가 존재할때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스의 첫 번째 노드일때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next