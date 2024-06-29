from fractions import Fraction
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        # simplified_fractions = set()
        # for denominator in range(2, n+1):
        #     for numerator in range(1, denominator):
        #         simplified_fractions.add(Fraction(numerator, denominator).__str__())
        # return list(simplified_fractions)

        simplified_fractions = list()
        for denominator in range(2, n+1):
            for numerator in range(1, denominator):
                if math.gcd(numerator, denominator) == 1:
                    simplified_fractions.append(f"{numerator}/{denominator}")
        return simplified_fractions
