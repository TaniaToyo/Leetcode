class Solution:
    def isPalindrome(self, x: int) -> bool:
        sum=0
        y=x
        while x > 0:
            digit = x % 10
            sum = sum * 10 + digit
            x = x //10
            print(x)
        if y==sum:
            print("True")
        else:
            print('False')

x = Solution()
x.isPalindrome(123)
