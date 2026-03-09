class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def add_new_node(head, num):
    return Node(num, head)

def add_at_end(head, num):
    new_node = Node(num)

    if head is None:
        return new_node

    ptr = head
    while ptr.link is not None:
        ptr = ptr.link

    ptr.link = new_node
    return head

def print_list(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end=" -> ")
        ptr = ptr.link
    print("None")

def free_list(head):
    # Not needed in Python, but shown for symmetry with C.
    # Python's garbage collector cleans up when references are gone.
    head = None
    return head

def main():
    head = Node(10)
    current = Node(20)
    head.link = current

    print("Initial:")
    print_list(head)

    head = add_new_node(head, 5)
    print("\nAfter add_new_node(head, 5):")
    print_list(head)

    head = add_at_end(head, 98)
    print("\nAfter add_at_end(head, 98):")
    print_list(head)

    head = free_list(head)

if __name__ == "__main__":
    main()
