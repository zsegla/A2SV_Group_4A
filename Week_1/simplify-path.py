# https://leetcode.com/problems/simplify-path/description/




class Solution:
    def simplifyPath(self, path: str) -> str:
        path_elements = path.split("/")
        stack = []+

        for item in path_elements:
            if item == "..":
                if stack:
                    stack.pop()
            elif item and item != ".":
                stack.append(item)
        return "/" + "/".join(stack)
