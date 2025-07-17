from typing import List
# Create a function that determines the minimum number of bracket removals needed for a valid string.
def min_removals_to_balance(brackets: str) -> int:
    stack: List[str] = []
    count: int = 0
    
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                count += 1

    return count + len(stack)

#TODO: Create a function that determines the minimum number of any paranthesis removals needed for a valid string.