class Node:

    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

def add_at_beginning(head,data):
    new_node = Node(data)
    if head is not None:
        new_node.next = head
        head.prev = new_node
    return new_node

def add_at_end(new_node,temp):
    new_node.next = None
    new_node.prev = temp
    temp.next = new_node


def insert(head,position,data):

    if position < 1:
        return head

    if position == 1:
        return add_at_beginning(head, data)

    if head is None:
        return head

    new_node = Node(data)
    temp = head

    for _ in range(position-2):
        if temp.next == None:
            return head
        temp = temp.next


    temp2 = temp.next

    if temp2 == None:
        add_at_end(new_node,temp)
        return head

    new_node.next = temp2
    temp2.prev = new_node
    temp.next = new_node
    new_node.prev = temp

    return head



def main():
    head = None
    head = insert(head,3,15)
    head = insert(head,4,20)
    head = insert(head,1,5)
    head = insert(head,2,10)

main()
