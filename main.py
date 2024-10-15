def digits():
    print("Enter 5 digits number:")
    digit = int(input())
    print(digit // 10000)
    print((digit % 10000) // 1000)
    print((digit % 1000) // 100)
    print((digit % 100) // 10)
    print((digit % 10))

def truncate():
    print("Enter a text:")
    text = input()
    length = len(text)
    print("Text length:", length)
    if(length >= 6):
        print(text[0:3]+"..."+text[len(text)-3:len(text)])
    else:
        print(text)


def main():
    print("Enter first number:")
    a = int(input())
    print("Enter second number:")
    b = int(input())

    print("Choose an operation:\n1. Sum\n2. Difference\n3. Product\n4. Average\n5. Distance\n6. Maximum\n7. Minimum")
    menu = ['','sum','difference','product','average','distance','maximum','minimum']
    operation = menu[int(input())]
    
    print("The result is:")
    if(operation == 'sum'):
        print(a+b)
    elif(operation == 'difference'):
        print(a-b)
    elif(operation == 'product'):
        print(a*b)
    elif(operation == 'average'):
        print((a+b)/2)
    elif(operation == 'distance'):
        print(abs(a-b))
    elif(operation == 'maximum'):
        print(max([a, b]))
    elif(operation == 'minimum'):
        print(min([a, b]))
    else:
        print(a*b)

def tiles():
    totalWidth = 100
    tileWidth = 5

    totalWidthNew = totalWidth - tileWidth
    doubleTileWidth = tileWidth * 2
    numberOfTiles = totalWidthNew // doubleTileWidth
    gap = totalWidthNew % doubleTileWidth
    gap = gap / 2

    numberOfTiles = numberOfTiles * 2 + 1

    print()

def stringSlice():
    print("asda", end="no")

    digits()

    word = "abcd"
    print(word[0:4:2])
    print(word[4::-1])
    print(word[::-1])

    print(chr(8364))
    print(word.replace('bc', 'ad'))
    print(word)

def priceFormatting():
    price = 1.23456789

    print("Price: %f" % price)
    print("Price: %.2f" % price)
    print("Price: %10.2f" % price) # align right

    print("Price: %10.3f" % 2.345667)
    print("Price: %10.4f" % 3.456789)

    print("Test %d" % 5.432423)
    print("Test %1d" % 5.432423)
    print("Test %2d" % 5.432423)
    print("Test %3d" % 5.432423)
    print("Test %4d" % 5.432423)
    print("Test %5d" % 5.432423)
    print("Test %6d" % 5.432423)
    print("Test %7d" % 5.432423)
    print("Test %8d" % 5.432423)
    print("Test %9d" % 5.432423)
    print("Test %10d" % 5.432423)

def calculateCoupons(amount):
    winText = 'You win a discount coupon of $%.2f. (%d%% of your purchase)'
    if amount > 210:
        return winText % (0.14 * amount, 14)
    if amount > 150:
        return winText % (0.12 * amount, 12)
    if amount > 60:
        return winText % (0.1 * amount, 10)
    if amount >= 10:
        return winText % (0.08 * amount, 8)
    return 'You do not get any coupons'

def couponsExercise():
    amountSpent = float(input("Please enter the cost of your groceries: "))
    print(calculateCoupons(amountSpent))

def trends():
    a = int(input("first:"))
    b = int(input("second:"))
    c = int(input("third:"))
    
    # assistant solution
    # if a < b:
    #     if b < c:
    #         print('increasing')
    #     else:
    #         print('neither')
    # elif a > b:
    #     if b > c:
    #         print('decreasing')
    #     else:
    #         print('neither')
    # else:
    #     print('neither')

    if a < b and b < c:
            print('increasing')
    elif a > b and b > c:
            print('decreasing')
    else:
        print('neither')

def grades():
    grades = { 'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0 }
    extra = { '+': 0.3, '-': -0.3 }

    grade = input('Input your grade: ')
    finalGrade = grades.get(grade[0], 0)
    if(len(grade) == 2) and grade[0] != 'F' and grade != 'A+':
        finalGrade += extra.get(grade[1], 0)

    print(str(finalGrade))

grades()