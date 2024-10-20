class RomanConverter:
    def __init__(self):
        self.roman_map = {                                      # Key: 1 - 100
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL',
            50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC',
            300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC',
            900: 'CM', 1000: 'M'
        }
        self.sorted_keys = sorted(self.roman_map.keys(), reverse=True)

    def int_to_roman(self, num):
        result = ''
        for key in self.sorted_keys:
            while num >= key:
                result = result + self.roman_map[key]
                num = num - key
        return result

# Ask user
num = int(input("Enter a number(1 - 1000): "))
converter = RomanConverter()
print(f"The Roman numeral for {num} is {converter.int_to_roman(num)}")