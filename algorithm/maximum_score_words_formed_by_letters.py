import itertools
class Solution(object):
    def findsubsets(self,s, n):
        return list(itertools.combinations(s, n))
    
    def makeallsubsets(self, s):
        length=len(s)
        SUBSETS=[[]]
        for i in range(1,length+1):
            sub = self.findsubsets(s,i)
            for x in sub:
                SUBSETS.append(list(x))
        return SUBSETS
        

    def maxScoreWords(self, words, letters, score):
        myWordSubSets = self.makeallsubsets(words)
        validSubSets = []
        for wordSet in myWordSubSets:
            ltrSet = letters[:]
            err = 0
            for word in wordSet:
                for l in word:
                    try:
                        ltrSet.remove(l)
                    except ValueError:
                        err = 1
                        break
                if err == 1:
                    break
            if err == 0:
                validSubSets.append(wordSet)
                
        total = 0
        
        for wordSet in validSubSets:
            count = 0
            for word in wordSet:
                for l in word:
                    pos = ord(l)-97
                    count = count+score[pos]
            if count > total:
                total = count
        return (total)

obj= Solution()
result = obj.maxScoreWords(["baaa", "aacc", "ccbc", "da", "dbbc"],
                           ["a", "a", "a", "c", "c", "c", "c", "c", "d", "d", "d"],
                           [9, 4, 10, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                  )
print(result)


