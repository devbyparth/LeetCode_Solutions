class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(string: str) -> bool:
            count = 0
            for ch in string:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        visited = {s}
        queue = deque([s])
        result = []
        found = False

        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()

                if is_valid(curr):
                    result.append(curr)
                    found = True   # mark found but still finish this level

                if found:
                    continue       # don't generate further removals once valid strings exist

                for i in range(len(curr)):
                    if curr[i] not in '()':
                        continue
                    next_str = curr[:i] + curr[i + 1:]
                    if next_str not in visited:
                        visited.add(next_str)
                        queue.append(next_str)

            if found:
                break

        return result