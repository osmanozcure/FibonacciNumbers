firstNumber = 1
secondNumber = 2
count = 1
fibonacciNumberResults = []
step = int(input("Please enter how many times do you want to calculate fibonacci numbers: "))

while count <= step:
    # 1, 2, 3, 4, 5
    # 1, 2 ==> 1 + 2, 3 = secondNumber, 2 = firstNumber
    # 2, 3 ==> 2 + 3, 5 = secondNumber, 3 = firstNumber
    

    print("Currently, first number: " ,firstNumber, " and second number: " ,secondNumber)
    result = firstNumber + secondNumber # 3 = 1 + 2
    print("Fibonacci number: " ,result)
    fibonacciNumberResults.append(result)
    firstNumber = secondNumber # 2 ==> firstNumber
    secondNumber = result # 3 ==> secondNumber

    # update count value
    count += 1

for i in range(0, len(fibonacciNumberResults), 1):
    print(fibonacciNumberResults[i])
    


