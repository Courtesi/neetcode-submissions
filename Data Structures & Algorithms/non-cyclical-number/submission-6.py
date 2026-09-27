class Solution:
    def isHappy(self, n: int) -> bool:
        nodups = set()
        

        while n != 1 and n != 0:
            temp = 0
            length = len(str(n))
            print(n)
            for i in range(length):
                digit = abs(n) // (10 ** i) % 10
                digit *= digit
                print(f"{digit=}")
                temp += digit

            if temp in nodups:
                return False
            print(f"{temp=}")
            nodups.add(temp)
            n = temp

            print(f"{n=}")
        
        return True