class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        components = path.split('/')

        for part in components:
            if part == '' or part == '.':
                continue
            elif part =='..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)