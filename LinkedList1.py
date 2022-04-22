

from multiprocessing.dummy import current_process
from requests import head


class LL:
    def __init__(self):
        self.head = None
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    # add first
    def addFirst(self,data):
        new_node = self.Node(data)
        if self.head == None:
            self.head = self.Node(data)
            return
        new_node.next = self.head
        self.head = new_node
    
    # print list
    def printList(self):
        if head is None:
            print("List is empty")
            return
        currentNode = self.head
        while(currentNode != None):
            print(currentNode.data+" ->")
            currentNode = currentNode.next


if __name__ == '__main__':
    list = LL()
    list.addFirst("is")
    list.addFirst("a")
    list.printList()

