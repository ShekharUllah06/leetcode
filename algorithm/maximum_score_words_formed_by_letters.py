
# words = ["dog","cat","dad","good"]
# #words=["xxxz", "ax", "bx", "cx"]
# #words = ["leetcode"]
# #score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# #score=[4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 10]
# score = [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1,
#          0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# letterMap={
#     'a':0,
#     'b':1,
#     'c':2,
#     'd':3,
#     'e':4,
#     'f':5,
#     'g':6,
#     'h':7,
#     'i':8,
#     'j':9,
#     'k':10,
#     'l':11,
#     'm':12,
#     'n':13,
#     'o':14,
#     'p':15,
#     'q':16,
#     'r':17,
#     's':18,
#     't':19,
#     'u':20,
#     'v':21,
#     'w':22,
#     'x':23,
#     'y':24,
#     'z':25,
    
# }


# def makeSubset(A):
#    # store all the sublists
#    B = [[]]

#    # first loop
#    for i in range(len(A) + 1):
#       # second loop
#       for j in range(i + 1, len(A) + 1):
#          # slice the subarray
#          sub = A[i:j]
#          B.append(sub)
#    return B


# myWordSubSets = makeSubset(words)
# validSubSets=[]
# for wordSet in myWordSubSets:
#     #letters = ["z", "a", "b", "c", "x", "x", "x"]
#     letters = ["l", "e", "t", "c", "o", "d"]
#     err = 0
#     for word in wordSet:
#         for l in word:
#            try:
#                letters.remove(l)
#            except ValueError:
#                myWordSubSets.remove(wordSet)
#                err=1
#                break
#         if err == 1:
#             break
#     if err==0:
#         validSubSets.append(wordSet)
# total=0
# for wordSet in validSubSets:
#     count=0
#     for word in wordSet:
#         for l in word:
#             count = count+score[letterMap[l]]
#     if count>total:
#         total=count
# print(total)

class Solution(object):
    def makeSubset(self, A):
        B = [[]]
        for i in range(len(A) + 1):
            for j in range(i + 1, len(A) + 1):
                sub = A[i:j]
                B.append(sub)
        return B

    def maxScoreWords(self, words, letters, score):
        letterMap = {
            'a': 0,
            'b': 1,
            'c': 2,
            'd': 3,
            'e': 4,
            'f': 5,
            'g': 6,
            'h': 7,
            'i': 8,
            'j': 9,
            'k': 10,
            'l': 11,
            'm': 12,
            'n': 13,
            'o': 14,
            'p': 15,
            'q': 16,
            'r': 17,
            's': 18,
            't': 19,
            'u': 20,
            'v': 21,
            'w': 22,
            'x': 23,
            'y': 24,
            'z': 25,
        }
        myWordSubSets = self.makeSubset(words)
        validSubSets = []
        for wordSet in myWordSubSets:
            print(wordSet)
            ltrSet = letters[:]
            err = 0
            for word in wordSet:
                for l in word:
                    try:
                        ltrSet.remove(l)
                    except ValueError:
                        myWordSubSets.remove(wordSet)
                        err = 1
                        break
                if err == 1:
                    break
            if err == 0:
                validSubSets.append(wordSet)
                
        total = 0
        print(validSubSets)
        
        for wordSet in validSubSets:
            count = 0
            for word in wordSet:
                for l in word:
                    count = count+score[letterMap[l]]
            if count > total:
                total = count
        return (total)

obj= Solution()
result = obj.maxScoreWords(["get", "set"],
                           ["g", "s", "e", "t"],
                           [0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0,
                               0, 0, 0, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0]
                  )
print(result)
