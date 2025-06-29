from fractions import Fraction
import re
formula=input()
fractions=re.findall(r'[+-]?\d+/\d+',formula)
result=sum(Fraction(f) for f in fractions)
print(f"{result.numerator}/{result.denominator}")