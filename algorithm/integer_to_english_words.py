class Solution(object):
    dictionary={
        0:"Zero",
        1:"One",
        2:"Two",
        3:"Three",
        4:"Four",
        5:"Five",
        6:"Six",
        7:"Seven",
        8:"Eight",
        9:"Nine",
        10:"Ten",
        11:"Eleven",
        12:"Twelve",
        13:"Thirteen",
        14:"Fourteen",
        15:"Fifteen",
        16:"Sixteen",
        17:"Seventeen",
        18:"Eighteen",
        19:"Nineteen",
    }
    dictionary2={
        0:"zero",
        1:"Ten",
        2:"Twenty",
        3:"Thirty",
        4:"Forty",
        5:"Fifty",
        6:"Sixty",
        7:"Seventy",
        8:"Eighty",
        9:"Ninety",

    }
    def helper(self,number):
        str2=""
        str3=""
        str4=""
        strNumber= str(number)

        if number<20:
            return self.dictionary[number]
        else:
            count=1
            while number>0:
                rem=0
                if count==1:
                    rem=number%10
                    if rem!=0:
                        str2=self.dictionary[rem]
                elif count==2:
                    rem=number%10
                    if rem!=0:
                        str3=self.dictionary2[rem]
                elif count==3:
                    rem=number%10
                    if rem!=0:
                        str4=self.dictionary[rem] + " Hundred"
                number=number//10
                count=count+1

            if(len(strNumber)==3):
                lastTwo=strNumber[1:3]
                lastTwo=int(lastTwo)
                if lastTwo !=0:
                    if lastTwo in self.dictionary:
                        str3=self.dictionary[lastTwo]
                        str2=""

            return (str4+" "+str3+" "+str2).strip() 
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        part1=part2=part3=part4=""
        flag=0
        myNumber=num
        if myNumber==0:
            return self.helper(myNumber)
        while myNumber>0:
            rem=myNumber%1000
            if flag==0 and rem!=0:
                part1=self.helper(rem)
            elif flag==1 and rem!=0:
                part2=self.helper(rem)+" Thousand"
            elif flag==2 and rem!=0:
                part3=self.helper(rem)+" Million"
            elif flag==3 and rem!=0:
                part4=self.helper(rem)+" Billion"
            flag=flag+1
            myNumber=myNumber//1000
        myReturn=(part4+" "+part3+" "+part2+" "+part1).replace("  ",' ')
        myReturn=myReturn.replace("  ",' ')
        return(myReturn).strip()
        