import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        user_input = input("Choose Operator into +,-,* : ")
        self.assertTrue(if user_input = + or user_input = - or user_input = *)

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 1, '-', '8 - 1', 7),
                (6, 4, '*', '6 * 4', 24)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                if operator == '+': 
                    actual_problem = f'{num1} operator {num2}'
                    actual_answer = num1 + num2
                elif operator == '-': 
                    actual_problem = f'{num1} operator {num2}'
                    actual_answer = num1 - num2
                else: 
                    actual_problem = f'{num1} operator {num2}'
                    actual_answer = num1 * num2
                self.assertTrue(if actual_problem == expected_problem and actual_answer == expected_answer)

if __name__ == "__main__":
    unittest.main()