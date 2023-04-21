class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
    def __getitem__(self, index):
        temp = self.head
        if isinstance(index, slice):
            k = []
            for i in range(index.start, index.stop, index.step):
                k.append(temp.data)
                temp = temp.next
            return k
        else:
            for i in range(index):
                temp = temp.next
            return temp.data
    def length(self):
        temp = self.head
        length = 0
        while temp:
            length += 1
            temp = temp.next
        return length





f = LinkedList()
f.push(6)
f.push(5)
f.push(4)
print(id(f[0]), id(f[1]), id(f[2]))
print(f.length())
k = [1, 2, 3]
print(id(k[0]), id(k[1]), id(k[2]))
f.print_list()

