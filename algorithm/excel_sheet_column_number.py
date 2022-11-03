class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        cName=columnTitle
        cName2 = cName[::-1]
        length=len(cName2)
        dictionary={
            "A":1,
            "B":2,
            "C":3,
            "D":4,
            "E":5,
            "F":6,
            "G":7,
            "H":8,
            "I":9,
            "J":10,
            "K":11,
            "L":12,
            "M":13,
            "N":14,
            "O":15,
            "P":16,
            "Q":17,
            "R":18,
            "S":19,
            "T":20,
            "U":21,
            "V":22,
            "W":23,
            "X":24,
            "Y":25,
            "Z":26,
        }
        total=0
        count=1
        for x in cName2:
            temp=0
            if count==1:
                temp=dictionary[x]
            elif count==2:
                temp=dictionary[x]*26
            elif count==3:
                temp=dictionary[x]*26*26
            elif count==4:
                temp=dictionary[x]*26*26*26
            elif count==5:
                temp=dictionary[x]*26*26*26*26
            elif count==6:
                temp=dictionary[x]*26*26*26*26*26
            elif count==7:
                temp=dictionary[x]*26*26*26*26*26*26
            count=count+1
            total=total+temp
        return total    

        