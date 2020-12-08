class Solution:
    def romanToInt(self, s: str) -> int:
        roman=[]
        j=0
        sum=0
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        print(dict)
        for i in s:
            roman.append(i)
        for i in range(0,len(roman)):
            if i+1!=len(roman):
                p=roman[i]
                q=roman[i+1]
                if dict[p]<dict[q]:
                    sum = sum + dict[p]

                else:
                    continue
        sum=sum+dict[q]

        print(sum)




test=Solution()
test.romanToInt('XL')
