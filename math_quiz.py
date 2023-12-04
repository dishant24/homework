import random

def random_number_generator(min, max):
    
    """
    Random number between minimum and maximum values.

    Parameters:
    min: int Minimum Value
    max :int Maximum Value

    Returns:
        _type_: int Number
    """
    return random.randint(min, max)


def random_operator_generator():
    """
    Make random choice in the mathamatic operator +,-,*

    Returns:
        _type_: mathamatical oprator
    """
    return random.choice(['+', '-', '*'])


def random_math_calculation(number1, number2, operator):
    
    """
    Take random number and perfom oprator which randomly choose random_operator

    Parameter:
    n1: int Random Number1
    n2:int Random Number2
    o: operator


    Returns:
        _type_: reult and a
    """
    result = f"{number1} {operator} {number2}"
    if operator == '-': a = number1 - number2
    elif operator == '+': a = number2 + number2
    else: a = number1 * number2
    return result, a

def math_quiz():
    """
    This is Math quiz Game which perfom math and ask for our answer and compare with actual calculation. IF it correct then print Correct else Wrong Answer.
    
    There is 3 chance to try and calculate the correct answer.

    """
    step = 0
    max_try = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(max_try):
        number1 = random_number_generator(1, 10); number2 = random_number_generator(1, 5); operator = random_operator_generator()

        PROBLEM, ANSWER = random_math_calculation(number1, number2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
            
        except ValueError:
            print("Oops!  That was no valid number.  Try again...") 
            
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            step += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {step}/{max_try}")

if __name__ == "__main__":
    math_quiz()