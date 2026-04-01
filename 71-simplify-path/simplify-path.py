class Solution:
    def simplifyPath(self, path: str) -> str:
        
        dir_stack = []

        elements = path.split("/")

        aboslute_path = []

        for element in elements:
            if len(element) == 0:
                continue
            
            if element == "..":  # Go up the root directory.
                if len(dir_stack) > 0:
                    dir_stack.pop(-1)

            elif element == ".": # We stay in the current directory. we dont do anything. 
                continue
            else: # Valid name of a directory. 
                dir_stack.append(element)

        # End, we join the dir_stack. 
        res = "/" + "/".join(dir_stack)

        return res
        