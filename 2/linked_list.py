class LinkedList:
    def __init__(self, data: int) -> None:
        self.value = data
        self.next = None

    def add(self, data: int):
        new_node = LinkedList(data)
        if self.next:
            new_node.next = self.next
        self.next = new_node

    def __del__(self):
        self.next = None


def create_list_from_array(arr):
    if not arr:
        return None
    head = LinkedList(arr[0])
    current = head
    for value in arr[1:]:
        current.add(value)
        current = current.next
    return head

def list_to_array(head):
    arr = []
    current = head
    while current:
        arr.append(current.value)
        current = current.next
    return arr