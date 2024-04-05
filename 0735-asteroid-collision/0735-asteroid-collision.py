class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Use stack, if new element is negative and not first element, remove smaller one/both
        stack = []
        for a in asteroids:
            # Non-empty and there is collision
            while stack and a < 0 < stack[-1]:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)
        return stack