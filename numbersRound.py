from numpy import random

largeNumbersOne = [25, 50, 75, 100]
largeNumbersTwo = [12, 37, 62, 87]

def generateNumbers(largeNumbers, largeNumCount):
    smallNumbers = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
    numberCount = 6
    numbers = []
    response = largeNumCount
    for i in range(response):
        num = random.randint(0, len(largeNumbers))
        numbers.append(largeNumbers.pop(num))
    for i in range(numberCount - len(numbers)):
        num = random.randint(0, len(smallNumbers))
        numbers.append((smallNumbers.pop(num)))
    return numbers

def generateValues(numbers):
    numOfOperations = random.randint(3,6)
    operations = random.choice(4, numOfOperations, p=[0.3, 0.2, 0.4, 0.1])
    running_total = 0
    calculations = []
    for i in range(numOfOperations + 1):
        if(running_total == 0):
            running_total += numbers.pop(random.randint(len(numbers)))
        else:
            if(operations[i-1] == 0):
                val = numbers.pop(random.randint(len(numbers)))
                calculations.append(str(running_total) + " + " + str(val))
                running_total += val
            elif(operations[i-1] == 1):
                val = numbers.pop(random.randint(len(numbers)))
                if(running_total - val == 0):
                    numbers.append(val)
                    i -= 1
                elif(running_total - val < 0):
                    calculations.append(str(val) + " - " + str(running_total))
                    running_total = val - running_total
                else:
                    calculations.append(str(running_total) + " - " + str(val))
                    running_total -= val
            elif(operations[i-1] == 2):
                val = numbers.pop(random.randint(len(numbers)))
                calculations.append(str(running_total) + " * " + str(val))
                running_total *= val
            elif(operations[i-1] == 3):
                val = numbers.pop(random.randint(len(numbers)))
                if(running_total % val != 0 and val % running_total != 0):
                    numbers.append(val)
                elif(running_total % val == 0):
                    val = numbers.pop(random.randint(len(numbers)))
                    calculations.append(str(running_total) + " / " + str(val))
                    running_total = running_total / val
                elif(val % running_total == 0):
                    val = numbers.pop(random.randint(len(numbers)))
                    calculations.append(str(val) + " / " + str(running_total))
                    running_total = val / running_total
        print(calculations)
    return running_total
                

print(generateValues(generateNumbers(largeNumbersOne, 3)))
    