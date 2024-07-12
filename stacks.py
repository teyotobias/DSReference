"""
A stack is a linear data structure that follows the Last In First Out (LIFO) principle. The element
added last is the one to be removed first. Python's built-in list can be used as a stack, but the
'collections.deque' class is a more efficient choice for stack operations.
"""

stack = []

# using deque
from collections import deque
dstack = deque()

stack.append(10)
stack.append(20)

#using deque
dstack.append(10)
dstack.append(20)

last_element = stack.pop()
last_element = dstack.pop()

top_element = stack[-1]
top_element = dstack[-1]

# checking if stack is empty
is_empty = len(stack) == 0 # True if stack is empty
is_empty = len(dstack) == 0 # True if deque is empty


"""
        Balanced Parentheses:   Check if the parentheses in the expression are balanced
"""
def is_balanced(expression):

    parentheses = {
        '[': ']',
        '(': ')',
        '{': '}'
    }
    stack = []

    for char in expression:
        if char in parentheses:
            stack.append(char)
        
        elif char in parentheses.values():
            if not stack or char != parentheses[stack.pop()]:
                return False
    
    return stack == []

# Example usage:
expression = "{[()()]}"
print(is_balanced(expression))
counter_expression = "{{}"
print(is_balanced(counter_expression))

    


'''
Common Problems/Patterns
Balanced Parentheses: Checking if an expression has balanced parentheses or brackets.
Reverse a String: Using stack operations to reverse the order of characters in a string.
Function Call Simulation: Using stacks to simulate the function call stack in recursive algorithms.
Undo Mechanism: Implementing undo functionality in text editors or other applications.
Depth-First Search (DFS): Implementing DFS in graphs or trees using a stack.
Evaluate Expressions: Using stacks to evaluate postfix or prefix expressions.
'''