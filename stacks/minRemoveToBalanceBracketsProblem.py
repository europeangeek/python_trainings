from typing import List
# Create a function that determines the minimum number of c removals needed for a valid string.
def min_removals_to_balance(s: str) -> int:
    stack: List[str] = []
    count: int = 0
    closeToOpen = {
            "]": "[",
            "}": "{",
            ")": "("
    }
    for c in s:
        if c in closeToOpen.values():
            stack.append(c)
        elif c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                count += 1
                print(c)

    return count + len(stack)

#TODO: Create a function that determines the minimum number of any paranthesis removals needed for a valid string.

print(min_removals_to_balance("({{})))(())")) 