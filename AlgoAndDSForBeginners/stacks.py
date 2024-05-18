# Operations (push, pop, peek)
# Push O(1)
# Pop O(1)
# Peek/Top O(1)

class Stacks:
    
    # Push
    def push(self, n):
        # using the pushback function from dynamic arrays to add to the stack
        self.stack.append(n)
    
    # Pop
    def pop(self):
        return self.stack.pop()
    
    # Peek
    def peek(self):
        return self.stack[-1]
