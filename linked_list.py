class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
        
class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head # self.head is a Node 
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
    
        itr = self.head
        # itr had some value
        while itr.next:
            #iterate to last element
            itr = itr.next

        itr.next = Node(data, None)

    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        
        return count


    def remove_at(self, index):
        if index < 0 or index>=self.get_length():
            raise Exception("Invalid index.")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = self.head
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index>=self.get_length():
            raise Exception("Invalid index.")
        
        if index == 0:
            self.insert_at_beg(data)
            return
        
        count = 0
        itr = self.head
        print(itr)
        print(itr.next)
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

    
    def insert_after_value(self, data_after, data_to_insert):
        pass
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
    itr =.data

    while itr:
            if  == :
                node = Node(data, itr.next)
                itr.next = node
                break

    def remove_by_value(self, data):
        pass
    # Remove first node that contains data
    while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break


if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_at_beg(5)
    ll.insert_at_beg(42)
    ll.insert_at_end(789)
    ll.insert_at_end(89)
    ll.inset_value(["banana", "mango", "apple", "grapes"])
    ll.remove_at(2)
    ll.insert_at(1, "hammer")
    ll.print()
    print(ll.get_length())