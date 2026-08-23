class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        f1={}
        f2={}
        n1=len(s1)
        n2=len(s2)
        if n1>n2:
            return False

        for x in s1:
            f1[x]= f1.get(x, 0) +1
        for x in s2[:n1]:   

            f2[x] = f2.get(x, 0) +1

        if f1 == f2:
            return True

        for j in range(n1, n2):
            x= s2[j]
            f2[x]= f2.get(x, 0)+1

            i= s2[j-n1]
            f2[i] -=1

            if f2[i] == 0:
                del f2[i]
            if f2== f1:
                return True
        return False
                


