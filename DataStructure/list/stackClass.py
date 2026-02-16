class stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item) 
    
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return None
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    

question = stack()

question.push('A')  
question.push('B')
question.push('C')
print("Stack: ", question.stack)
print("Peek: ", question.peek())
print("Pop: ", question.pop())
print("Stack after Pop: ", question.stack)  
print("isEmpty: ", question.isEmpty())
print("Size: ", question.size())
