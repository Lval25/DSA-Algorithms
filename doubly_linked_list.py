class DNode():
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev 

class doublelnk():
    def __init__(self):
        self.head = None
        self.tail = None


    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        if self.head is None:
            raise Exception("No data exist")
        
        curr = self.head
        curr_lst = []

        while curr:
            print(curr.data, end=' ')
            curr_lst += curr.data + '-->'
            curr = curr.next
        
        return curr_lst


    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            raise Exception("No data exist")
        
        last = self.get_last_node()
        curr = last
        curr_lst = []

        while curr:
            print(curr.data, end=' ')
            curr_lst += curr.data + '-->'
            curr = curr.prev
            
        return curr_lst

    def append(self, data):
        node = DNode(data)
        #if ther is no value at head its empty
        if self.head is None:
        #assuming there is no value in the list head and tail are the saame since there is only one value
            self.head = self.tail = node
        else:
        #Append new node
            #Link the new node to the current tail
            node.prev = self.tail
            #Link the current tail to the new node
            self.tail.next = node
            #Update the tail to be the new node
            self.tail = node

    
    def get_length(self):
        count = 0

        itr = self.head
        while itr:
            #Iterate and count the elements
            count += 1
            itr = itr.next

        return count
            

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr


    def insert_at_head(self, data):
        node = DNode(data, self.head, None)
        #self.head = node
        if not self.head:
            #node = DNode(data, self.head, None)
            #Since there is no node yet the head and tail are the same place since it will only be one node
            self.head = self.tail = node
        else:
            #node = DNode(data, self.head, None)
            self.head.prev = node
            
        self.head = node

    def insert_at_end(self, data):
        node = DNode(data)

        if self.head is None:
            self.head = self.tail = node

        last = self.get_last_node()


    def insert_at(self, index, data):
        #Check if the index exist
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")
        
        #Inserting at the first index
        if index == 0:
            self.insert_at_head(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            #If after the first up to the last link, insert the link to the next node of the PREVIOUS element to put give that node the current nodes next value
            if count == index - 1:
                node = DNode(data, itr.next, itr.prev)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
         if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")
        
         if index == 0:
            #If the index is at the beginning of the linked list move the first elements link to the next element which get's rid of the original first element
            self.head = self.head.next
            return
        
        #You have to manually keep the count of the links index
         count = 0
         itr = self.head

         while itr:
            #You need to be at the "PREVIOUS" link of the link you want to delete and reset it to the link after the one you want to delete
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
    

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        
        itr = self.head
        dllstr = ''

        while itr:
            if itr == self.head:
                dllstr += itr.data + '-->'
            else:
                dllstr += '<--' + itr.data + '-->'
            itr = itr.next

        print(dllstr)



if __name__ == '__main__':
    dl = doublelnk()
    #dl.insert_at_head("42")
    print(dl.insert_at_head("24"))
    dl.append("66")
    dl.append("67")
    dl.append("68")
    #dl.insert_at_head("24")
    #print(dl.get_last_node())
    dl.print_forward()
    print("/n")
    dl.print_backward()
    print("/n")
    dl.insert_at(2, "hello")
    dl.print_forward()
    print("/n")
    #dl.insert_at(2, "hello")
    dl.print_backward()
    print("/n")
    #dl.remove_at(3)
    dl.print()
    #dl.print()
