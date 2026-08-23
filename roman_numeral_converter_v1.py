# Basic Roman Numeral Converter

num = int(input("Give a number 1-100: "))

tens = num // 10
ones = num % 10

if tens == 0:
    romtens = ""
elif tens == 1:
    romtens = "X"
elif tens == 2:
    romtens = "XX"
elif tens == 3:
    romtens = "XXX"
elif tens == 4:
    romtens = "XL"
elif tens == 5:
    romtens = "L"
elif tens == 6:
    romtens = "LX"
elif tens == 7:
    romtens = "LXX"
elif tens == 8:
    romtens = "LXXX"
elif tens == 9:
    romtens = "XC"

if ones == 0:
    romones = ""
elif ones == 1:
    romones = "I"
elif ones == 2:
    romones = "II"
elif ones == 3:
    romones = "III"
elif ones == 4:
    romones = "IV"
elif ones == 5:
    romones = "V"
elif ones == 6:
    romones = "VI"
elif ones == 7:
    romones = "VII"
elif ones == 8:
    romones = "VIII"
elif ones == 9:
    romones = "IX"

if num == 100:
    romnum = "C"
else:
    romnum = romtens + romones

print(f"The number {num} is {romnum} in roman numerals.")






