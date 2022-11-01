# 66
"""
You are given a large integer represented as an integer array digits, 
where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""
class PlusOne(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strNumber=''
        for x in digits:
            strNumber=strNumber+str(x)
        
        number= int(strNumber)+1
        strNumber=str(number)
        return list(strNumber)