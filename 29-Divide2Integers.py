class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0 # the quotient is intialized

        neg = (dividend < 0) ^ (divisor < 0) # Checking if one of the numbers is negative

        a = abs(dividend) # making sure both the numbers
        b = abs(divisor) # are positive

        if (a == 2147483648) and (b == 1):
            return -2147483648 if neg else 2147483647

        for i in range(31,-1,-1): # starting our loop

            if b << i <= a  : # checking if b multiplied by 2**i is <= a 
                a -= b << i   # subtracting b << i from a
                ans += 2 ** i # adding 2 power i to the answer

        # and finally checking if the output should be negative and returning it
        return (ans * -1) if neg else ans
            
