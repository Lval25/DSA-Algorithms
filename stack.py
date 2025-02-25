from collections import deque

class Stack:
    def __init__(self):
        self.list = deque()
    
    def push(self, val):
        self.list.append(val)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def is_empty(self):
        return len(self.list) == 0
    
    def size(self):
        return len(self.list)
    
    def rev(self):
        #Reverse the entire list
        self.list.reverse()
        #self.list = deque(element[::-1] for element in self.list)
         # Reverse each element in the deque
        reversed_elements = []
        for element in self.list:
            if isinstance(element, int):
                # Convert int to string, reverse the string, and convert back to int
                reversed_element = int(str(element)[::-1])
            else:
                # Reverse the element assuming it's a sequence (like string or list)
                reversed_element = element[::-1]
            reversed_elements.append(reversed_element)
        
        # Create a new deque with the reversed elements
        self.list = deque(reversed_elements)
    
    def is_blnc(self, val):
        #check string for occurences of paranthesis "{}',"()" or "[]". and pop those values to check the accurately (or check both sides at once)
        pairs = {')': '(', ']': '[', '}': '{'}
        opening = set(pairs.values())
        closing = set(pairs.keys())
        check = []

        for i in val:
            if i in opening:
                check.append(i)
                print(check)
            elif i in closing:
                #print(i)
                #print(check[-1])
                #print(f"PAir: {pairs[i]}")
                #if the list is empty or the most recent element is not equal to the correspoonding value (other bracket "}")
                if not check or check[-1] != pairs[i]:
                    return False
                check.pop()

        return not check







s = Stack()

s.push(11121134)
s.push("Salami kush")
print(s.size())
print(s.peek())
print(s.list)
#s.pop()
s.rev()
print(s.list)

print(s.is_blnc("{} ()"))
print(s.is_blnc("({a+b})"))
print(s.is_blnc("))((a+b}{"))