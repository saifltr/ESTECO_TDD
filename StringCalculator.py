import re
import unittest
from termcolor import colored


class StringCalculator:
    DEFAULT_SEPARATOR = ","
    CUSTOM_SEPARATOR_REGEX = r"//(.+)\n(.*)"
    NEGATIVE_NUMBER_PATTERN = re.compile("-\\d+")

    @staticmethod
    def run_tests():
        # Create a test suite
        suite = unittest.TestSuite()
        suite.addTest(StringCalculatorTest("test_add_empty_string"))
        suite.addTest(StringCalculatorTest("test_add_one_number"))
        suite.addTest(StringCalculatorTest("test_add_two_numbers"))
        suite.addTest(StringCalculatorTest("test_multiply_empty_string"))
        suite.addTest(StringCalculatorTest("test_multiply_one_number"))
        suite.addTest(StringCalculatorTest("test_multiply_two_numbers"))
        # Add more test cases as needed

        # Run the test suite
        unittest.TextTestRunner().run(suite)

    @staticmethod
    def check_test_case(test_name, expected_output, actual_output):
        if expected_output == actual_output:
            result = colored("passed", "green")
        else:
            result = colored("failed", "red")

        print(f"Test Case {test_name}: {result}")

    @staticmethod
    def add(numbers):
        if not numbers:
            return "0"

        separator = StringCalculator.get_separator(numbers)
        if separator is None:
            separator = StringCalculator.DEFAULT_SEPARATOR

        number_tokens = StringCalculator.extract_number_tokens(numbers, separator)

        negatives = []
        total_sum = 0

        for token in number_tokens:
            if token:
                try:
                    number = float(token)
                except ValueError:
                    return f"Invalid number: {token}"
                if number < 0:
                    negatives.append(int(number))
                elif number <= 1000:
                    total_sum += number

        if negatives:
            return f"Negative not allowed: {negatives}"

        return str(total_sum)

    @staticmethod
    def multiply(numbers):
        if not numbers:
            return "0"

        separator = StringCalculator.get_separator(numbers)
        if separator is None:
            separator = StringCalculator.DEFAULT_SEPARATOR

        number_tokens = StringCalculator.extract_number_tokens(numbers, separator)

        negatives = []
        product = 1

        for token in number_tokens:
            if token:
                try:
                    number = float(token)
                except ValueError:
                    return f"Invalid number: {token}"
                if number < 0:
                    negatives.append(int(number))
                elif number <= 1000:
                    product *= number

        if negatives:
            return f"Negative not allowed: {negatives}"

        return str(product)

    @staticmethod
    def extract_number_tokens(numbers, separator):
        if separator == StringCalculator.DEFAULT_SEPARATOR:
            tokens = re.split(r"[,\n]", numbers)
        else:
            regex = re.escape(separator)
            tokens = re.split(regex, numbers)
        return tokens

    @staticmethod
    def get_separator(numbers):
        match = re.match(StringCalculator.CUSTOM_SEPARATOR_REGEX, numbers)
        if match:
            separator = match.group(1)
            if separator:
                return separator
        return None


class StringCalculatorTest(unittest.TestCase):
    def test_add_empty_string(self):
        input_str = ""
        expected_output = "0"
        actual_output = StringCalculator.add(input_str)
        StringCalculator.check_test_case(self._testMethodName, expected_output, actual_output)

    def test_add_one_number(self):
        input_str = "1"
        expected_output = "1"
        actual_output = StringCalculator.add(input_str)

    def test_add_one_number(self):
        input_str = "1"
        expected_output = "1"
        actual_output = StringCalculator.add(input_str)
        StringCalculator.check_test_case(self._testMethodName, expected_output, actual_output)

    def test_add_two_numbers(self):
        input_str = "1,2"
        expected_output = "3"
        actual_output = StringCalculator.add(input_str)
        StringCalculator.check_test_case(self._testMethodName, expected_output, actual_output)

    def test_multiply_empty_string(self):
        input_str = ""
        expected_output = "0"
        actual_output = StringCalculator.multiply(input_str)
        StringCalculator.check_test_case(self._testMethodName, expected_output, actual_output)

    def test_multiply_one_number(self):
        input_str = "2"
        expected_output = "2"
        actual_output = StringCalculator.multiply(input_str)
        StringCalculator.check_test_case(self._testMethodName, expected_output, actual_output)

    def test_multiply_two_numbers(self):
        input_str = "2,3"
        expected_output = "6"
        actual_output = StringCalculator.multiply(input_str)
        StringCalculator.check_test_case(self._testMethodName, expected_output, actual_output)

if __name__ == "__main__":
    StringCalculator.run_tests()
    print(StringCalculator.add(""))  # Expected output: 0
    print(StringCalculator.add("1"))  # Expected output: 1
    print(StringCalculator.add("1.1,2.2"))  # Expected output: 3.3
    print(StringCalculator.add("1\n2,3"))  # Expected output: 6
    print(StringCalculator.add("175.2,\n35"))  # Expected output: "Number expected but '\n' found at position 6."
    print(StringCalculator.add("1,3,"))  # Expected output: "Number expected but EOF found."
    print(StringCalculator.add("//;\n1;2"))  # Expected output: 3
    print(StringCalculator.add("//|\n1|2|3"))  # Expected output: 6
    print(StringCalculator.add("//sep\n2sep3"))  # Expected output: 5
    print(StringCalculator.add("//|\n1|2,3"))  # Expected output: "'|' expected but ',' found at position 3."
    print(StringCalculator.add("-1,2"))  # Expected output: "Negative not allowed: [-1, -2]"
    print(StringCalculator.multiply("1,9,8"))  # Expected output: "Number expected but EOF found."
