class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
def create(arr):
    head = Node(arr[0])
    temp = head

    for num in arr[1:]:
        temp.next = Node(num)
        temp = temp.next

    return head


# Remove duplicates
def remove_duplicates(head):
    visited = set()

    curr = head
    prev = None

    while curr:
        if curr.data in visited:
            prev.next = curr.next
        else:
            visited.add(curr.data)
            prev = curr

        curr = curr.next

    return head


# Reverse linked list
def reverse(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


# Print linked list
def display(head):
    while head:
        print(head.data, end=" ")
        head = head.next


arr = list(map(int, input().split()))

head = create(arr)
head = remove_duplicates(head)
head = reverse(head)

display(head)