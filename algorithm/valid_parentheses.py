class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk=[]
        for char in s:
            if char=='(':
                stk.append(')')
            elif char=='{':
                stk.append('}')
            elif char=='[':
                stk.append(']')
            elif len(stk)==0 or stk.pop()!=char:
                return False
        if stk==[]:
            return True
        return False


