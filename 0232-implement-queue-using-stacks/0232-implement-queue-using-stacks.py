class MyQueue:

    def __init__(self):
        self.in_stack = []  # Stack for push operations
        self.out_stack = []  # Stack for pop/peek operations

    def push(self, x: int) -> None:
        self.in_stack.append(x)  # Push element onto the in_stack

    def pop(self) -> int:
        self._move_in_to_out()
        return self.out_stack.pop() if self.out_stack else None  # Pop from the out_stack

    def peek(self) -> int:
        self._move_in_to_out()
        return self.out_stack[-1] if self.out_stack else None  # Return the top element of out_stack

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack  # Check if both stacks are empty

    def _move_in_to_out(self):
        # Transfer elements from in_stack to out_stack if out_stack is empty
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
