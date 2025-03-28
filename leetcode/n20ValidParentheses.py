class Solution:
    def isValid(self, s:str) -> bool:
        '''
        Test case:
        # 1: (), True
        # 2: ({)}, False
        # 3: [({})], True
        # 4: [), False
        # 5: [(, False
        # 6" })

        condition:
        open bracket must be closed
        closed in order -> test case 2

        pseudocode

        for elem in s:
            if elem is open then push
            else pop
        '''
        #only contain open brackets/parentheses
        stack = []
        # len(s) % 2 == 0 : true? No
        # mapping = {"{":"}", "[":"]", "(":")"}
        mapping = {"}":"{", "]":"[", ")":"("}
        for elem in s:
            if elem not in mapping:
                stack.append()
            elif stack and stack[-1] == mapping[elem] : # this can not filter out case 4
                # curr_stack: [
                # elem ), (
                stack.pop()
            else:
                return False
        return len(stack) == 0 # stack is empty then parenthese matched
            