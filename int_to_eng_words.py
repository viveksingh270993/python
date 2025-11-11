class NumberToWordsConverter:
    def __init__(self):
        self.less_than_20 = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
            "Sixteen", "Seventeen", "Eighteen", "Nineteen"
        ]
        self.tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty",
            "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def number_to_words(self, num: int) -> str:
        if num == 0:
            return "Zero"

        res = ""
        i = 0
        while num > 0:
            if num % 1000 != 0:
                res = self._helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000
            i += 1

        return res.strip()

    def _helper(self, num: int) -> str:
        if num == 0:
            return ""
        elif num < 20:
            return self.less_than_20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self._helper(num % 10)
        else:
            return self.less_than_20[num // 100] + " Hundred " + self._helper(num % 100)


if __name__ == "__main__":
    converter = NumberToWordsConverter()

    test_cases = [0, 5, 13, 85, 123, 1005, 12345, 1000010, 987654321]
    for num in test_cases:
        print(f"{num} → {converter.number_to_words(num)}")
