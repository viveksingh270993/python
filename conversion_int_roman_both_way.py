class RomanConverter:
    def __init__(self):
        self.roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        self.int_vals = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        self.roman_syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]

    def roman_to_int(self, s: str) -> int:
        total = 0
        prev_value = 0
        for char in reversed(s.upper()):
            value = self.roman_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

    def int_to_roman(self, num: int) -> str:
        roman = ""
        i = 0
        while num > 0:
            count = num // self.int_vals[i]
            roman += self.roman_syms[i] * count
            num -= self.int_vals[i] * count
            i += 1
        return roman


if __name__ == "__main__":
    converter = RomanConverter()

    # Roman → Integer
    print(converter.roman_to_int("MCMXCIV"))  # 1994
    print(converter.roman_to_int("LVIII"))    # 58

    # Integer → Roman
    print(converter.int_to_roman(1994)       # MCMXCIV
    print(converter.int_to_roman(58))         # LVIII
