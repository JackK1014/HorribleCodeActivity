class CalculatorFixes:
    # Adds the two numbers passed in as parameters and returns the result.
    def add(self, firstNumber, secondNumber):
        return firstNumber + secondNumber

    # Subtracts secondNumber from firstNumber and returns the result.
    def subtract(self, firstNumber, secondNumber):
        return firstNumber - secondNumber

    # Multiplies the two numbers passed in as parameters and returns the result.
    def multiply(self, firstNumber, secondNumber):
        return firstNumber * secondNumber


# Actually creates the fixed calculator to be used later on.
fixedCalculator = CalculatorFixes()

# Gets two numbers as input from the user.
firstNumInput = int(input("Enter the first number (integer): "))
secondNumInput = int(input("Enter the second number (integer): "))

# All three functions are used and the result from each is stored in separate variables.
additionResult = fixedCalculator.add(firstNumInput, secondNumInput)
subtractionResult = fixedCalculator.subtract(firstNumInput, secondNumInput)
multiplicationResult = fixedCalculator.multiply(firstNumInput, secondNumInput)

# Prints out the results from adding, subtracting, and multiplying the two numbers input by the user.
print(f"Addition: {firstNumInput} + {secondNumInput} = {additionResult}")
print(f"Subtraction: {firstNumInput} - {secondNumInput} = {subtractionResult}")
print(f"Multiplication: {firstNumInput} * {secondNumInput} = {multiplicationResult}")
