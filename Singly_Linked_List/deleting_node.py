class Node:
    
    def __init__(self,data,link = None):
        self.data = data
        self.link = link

def delete_node(head,position):
    if position < 1 or head is None:
        print("Invalid Position")
        return head
    if position == 1:
        return head.link
    temp = head
    if position > 2:
        for _ in range(position-2):
            if temp.link is None:
             print("Out of Bound")
             return head
            temp = temp.link
    if temp.link is None:
        print("Out of Bound")
        return head

    temp.link = (temp.link).link
    return head


def main():
    head = Node(10)
    second = Node(20)
    head.link = second
    third = Node(30)
    second.link = third
    head = delete_node(head,2)

main()