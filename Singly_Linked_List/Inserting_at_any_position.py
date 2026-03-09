class Node:
    def __init__ (self,data,link=None):
        self.data = data
        self.link = link

def add_new_node(head,data,position):
    if position < 0:
         print("Invalid position")
         return head
    
    
    new_node = Node(data)

    if position == 0:
        new_node.link = head
        return new_node

    if head == None:
        return new_node
    
    head_copy = head
    
    for _ in range(1,position - 1,1):
         if head_copy == None:
              print("Out of Bound")
              return head
         head_copy = head_copy.link

    if head_copy is None:
        print("Out of Bound")
        return head
    
    new_node.link = head_copy.link
    head_copy.link = new_node

    return head

def main():
        head = Node(10)
        second = Node(20)
        head.link = second
        third = Node(30)
        second.link = third

        head = add_new_node(head,25,3)
    
        current = head
        while current:
            print(current.data, end = " -> ")
            current = current.link
        print("None")
          
main()