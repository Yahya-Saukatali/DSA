from collections import Counter

class Solution(object):
    def findEvenNumbers(self, digits):
        digit_count = Counter(digits)
        result = []

        for num in range(100, 1000, 2):  # Only even 3-digit numbers
            num_digits = list(map(int, str(num)))
            num_counter = Counter(num_digits)

            if all(num_counter[d] <= digit_count[d] for d in num_counter):
                result.append(num)

        return result
