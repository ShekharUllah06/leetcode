class Solution(object):
    def countX(self, n):
        count = 0
        d = n//10
        rem = n % 10
        if d > 0:
            while d > 0:
                d = n//10
                rem1 = n % 10
                n = n//10
                if n == 0 and rem1 > 0:
                    count = count+1
                elif n == 1 and rem1 == 0:
                    count = count+1
                elif n == 1 and rem1 > 0:
                    count = count+1+rem1
                elif n == 2 and rem1 == 0:
                    count = count+11
                elif n == 2 and rem1 > 0:
                    count = count+10+1
                elif n == 3 and rem1 == 0:
                    count = count+12
                elif n == 3 and rem1 > 0:
                    count = count+11+1
                elif n == 4 and rem1 == 0:
                    count = count+13
                elif n == 4 and rem1 > 0:
                    count = count+12+1
                elif n == 5 and rem1 == 0:
                    count = count+14
                elif n == 5 and rem1 > 0:
                    count = count+13+1
                elif n == 6 and rem1 == 0:
                    count = count+15
                elif n == 6 and rem1 > 0:
                    count = count+14+1
                elif n == 7 and rem1 == 0:
                    count = count+16
                elif n == 7 and rem1 > 0:
                    count = count+15+1
                elif n == 8 and rem1 == 0:
                    count = count+17
                elif n == 8 and rem1 > 0:
                    count = count+16+1
                elif n == 9 and rem1 == 0:
                    count = count+18
                elif n == 9 and rem1 > 0:
                    count = count+17+1

        if d == 0 and rem > 0:
            count = count+1

        return count

    def countXX(self, n):
        count = 0
        if n <= 99:
            count = self.countX(n)
        elif n > 99 and n < 1000:
            rem = n % 100
            d = n//100
            extra = 0
            if d > 1:
                extra = 100
            else:
                extra = rem+1
            count = (self.countX(99)*d)+self.countX(rem)+extra

        return count

    def countXXX(self, n):
        count = 0
        if n <= 999:
            count = self.countXX(n)
        elif n > 999 and n < 10000:
            rem = n % 1000
            d = n//1000
            extra = 0
            if d > 1:
                extra = 1000
            else:
                extra = rem+1
            count = (self.countXX(999)*d)+self.countXX(rem)+extra

        return count

    def countXXXX(self, n):
        count = 0
        if n <= 9999:
            count = self.countXXX(n)
        elif n > 9999 and n < 100000:
            rem = n % 10000
            d = n//10000
            extra = 0
            if d > 1:
                extra = 10000
            else:
                extra = rem+1
            count = (self.countXXX(9999)*d)+self.countXXX(rem)+extra

        return count

    def countXXXXX(self, n):
        count = 0
        if n <= 99999:
            count = self.countXXXX(n)
        elif n > 99999 and n < 1000000:
            rem = n % 100000
            d = n//100000
            extra = 0
            if d > 1:
                extra = 100000
            else:
                extra = rem+1
            count = (self.countXXXX(99999)*d)+self.countXXXX(rem)+extra

        return count

    def count6X(self, n):
        count = 0
        if n <= 999999:
            count = self.countXXXXX(n)
        elif n > 999999 and n < 10000000:
            rem = n % 1000000
            d = n//1000000
            extra = 0
            if d > 1:
                extra = 1000000
            else:
                extra = rem+1
            count = (self.countXXXXX(999999)*d)+self.countXXXXX(rem)+extra

        return count

    def count7X(self, n):
        count = 0
        if n <= 9999999:
            count = self.count6X(n)
        elif n > 9999999 and n < 100000000:
            rem = n % 10000000
            d = n//10000000
            extra = 0
            if d > 1:
                extra = 10000000
            else:
                extra = rem+1
            count = (self.count6X(9999999)*d)+self.count6X(rem)+extra

        return count

    def count8X(self, n):
        count = 0
        if n <= 99999999:
            count = self.count7X(n)
        elif n > 99999999 and n < 1000000000:
            rem = n % 100000000
            d = n//100000000
            extra = 0
            if d > 1:
                extra = 100000000
            else:
                extra = rem+1
            count = (self.count7X(99999999)*d)+self.count7X(rem)+extra

        return count

    def count9X(self, n):
        count = 0
        if n <= 999999999:
            count = self.count8X(n)
        elif n > 999999999 and n < 10000000000:
            rem = n % 1000000000
            d = n//1000000000
            extra = 0
            if d > 1:
                extra = 1000000000
            else:
                extra = rem+1
            count = (self.count8X(999999999)*d)+self.count8X(rem)+extra

        return count

    def countDigitOne(self, n):
        return self.count9X(n)
