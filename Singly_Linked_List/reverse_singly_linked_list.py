class Node:
    
    def __init__(self,data,link = None):
        self.data = data
        self.link = link

def reverse(head):
    if head == None:
        return None
    previous = head

    if head.link == None:
        return head
    
    current = previous.link
    next = current.link
    previous.link = None
    while next!= None:
        current.link = previous
        previous = current
        current = next
        next = next.link
    current.next = previous
    head = current
    return head

def main():
    head = Node(10)
    second = Node(20)
    head.link = second
    third = Node(30)
    second.link = third
    head = reverse(head)

main()