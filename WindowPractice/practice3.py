class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total+=1
            cur = cur.next
        return total

    def display(self):
        elem=[]
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print(elem)

    def get(self,index):
        if index >= self.lenght():
            print('Error: "get" index out of range')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx+=1

    def erase(self,index):
        if index >= self.lenght():
            print('Error: "erase" index out of range')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next = cur_node.next
                return
            cur_idx+=1

my_list = linked_list()

my_list.display()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)

my_list.display()

print("Element at 2nd index: %d" % my_list.get(2))

a = input("Enter an index to be erased: ")
print("deleting %d" % my_list.get(a) + " at index %d" % a)
my_list.erase(a)
my_list.display()