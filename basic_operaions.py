import pdb

class BasicOperations:

    def __init__(self):
        return None

    def gcd(self, n1, n2):
        if(n2 == 0):
            return n1
        else:
            return self.gcd(n2, n1 % n2)

# d = int(input())
# n = int(input())
# print(BasicOperations().gcd(d, n))
    
