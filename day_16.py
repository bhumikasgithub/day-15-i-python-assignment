#1
def stutter(word):
    # Take the first two letters
    first_two = word[:2]
    # Create the stuttered format
    result = f"{first_two}... {first_two}... {word}?"
    return result

# Test cases
print(stutter("incredible"))     # ➞ "in... in... incredible?"
print(stutter("enthusiastic"))   # ➞ "en... en... enthusiastic?"
print(stutter("outstanding"))    # ➞ "ou... ou... outstanding?"

#2
import math  # to use math.pi

def radians_to_degrees(radian):
    degrees = radian * (180 / math.pi)  # use formula
    return round(degrees, 1)  # round to 1 decimal place

# Test cases
print(radians_to_degrees(1))    # ➞ 57.3
print(radians_to_degrees(20))   # ➞ 1145.9
print(radians_to_degrees(50))   # ➞ 2864.8
