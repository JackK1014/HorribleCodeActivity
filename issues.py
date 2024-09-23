#This is a program
class CaclulatorIssues:
    def add(self, a, b):
        if b == 0:
            total = a + 0
        elif b == 1:
            total = a + 1
        elif b == 2:
            total = a + 2
        elif b == 3:
            total = a + 3
        elif b == 4:
            total = b + 4
        elif b == 5:
            total = a + 5
        elif b == 6:
            total = a + 6
        elif b == 7:
            total = a + 7
        elif b == 8:
            total = a + 8
        elif b == 9:
            total = a + 9
        elif b == 10:
            total = a + 10
        else:
            for i in range(b):
                total = a + i + 1
        return total

    def subtract(self, a, b):
        if a >= 0:
            return a-b
        elif b >= 0:
            return b-a
        else:
            return 21 - 21 + a - b

    def multiply(self, a, b):
        total = 0
        if a ^ b < 0:
            return a * b
        else:
            for i in range(a):
                    total = total + b
        return total


calcIssues = CaclulatorIssues()

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} + {num2} = {calcIssues.add(num1, num2)}")
print(f"{num1} - {num2} = {calcIssues.subtract(num1, num2)}")
print(f"{num1} * {num2} = {calcIssues.multiply(num1, num2)}")
#All code here works great :)