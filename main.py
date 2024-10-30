import math

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

def duplicateNumbersExercise():
    inputString = input("Enter a line of numbers: ")
    temp = -1
    duplicates = []
    for num in inputString:
        num = int(num)
        if(temp == num and (num not in duplicates)):
            duplicates.append(num)
        temp = num

    print(' '.join([str(i) for i in duplicates]))

# duplicateNumbersExercise()
# 1334556663

def loops():
    print([i for i in range(5)])
    print([i for i in range(1,6)])
    print([i for i in range(1,11,2)])
    print([i for i in range(5,0,-1)])
    print([str(i)+name for (i,name) in enumerate(['sena', 'aji', 'buwana'])])
    print([str(i)+name for (i,name) in enumerate('ikomangsena')])

    # for i in range(1,5):
    #     print('x^%d' % i)
    #     for x in range(1,11):
    #         print(str(x**i))
    #     print('\t')
    
    for i in range(1,5):
        print('x^%d' %i, end='\t')

    for x in range(1,11): #row
        print('')
        for i in range(1,5): #column
            p = (x**i)
            print(str(p), end='\t')
    
    for x in range(4): 
        print('')
        for i in range(4):
            print('[]', end='')

def wordsInPiecesExercise():
    word = input("Input word: ")
    if not word.isalpha():
        print('Input alphabets only')
        return
    
    for i in range(1,len(word)+1):
        for j in range(len(word)):
            if i+j <= len(word):
                print(word[j:i+j])

def lineNumbersLab():
    terminated = False
    total = 0
    min = math.inf
    max = -math.inf
    even = 0
    odd = 0
    while(not terminated):
        inputString = input("Enter a number: ")
        if inputString.isnumeric():
            num = int(inputString)
            total += num
            min = num if num <= min else min
            max = num if num >= max else max
            even = even + 1 if num % 2 == 0 else even
            odd = odd + 1 if num % 2 != 0 else odd
            print('Total='+str(total), 'Min='+str(min), 'Max='+str(max), 'Even='+str(even), 'Odd='+str(odd))
        else:
            terminated = True

def parsingStringLab():
    sentence = input("Input a sentence: ")
    upper = ''
    even = ''
    noVowels = ''
    digits = 0
    vowelPosition = []
    for i,char in enumerate(sentence):
        if char.isupper():
            upper += char
        if i % 2 == 0:
            even += char
        if char in 'aiueoAIUEO':
            noVowels += '_'
            vowelPosition.append(i)
        else:
            noVowels += char
        if char.isdigit():
            digits += 1
    print('Upper='+upper)
    print('Even='+even)
    print('No Vowels='+noVowels)
    print('Digits=', digits) 
    print('Vowel Positions', vowelPosition)

from random import random, randint

def randomLesson():
    print(random())
    print(randint(1,6))

def atTheCinemaLab5():
    tickets = 10
    buyers = 0
    while tickets > 0:
        buyTickets = input("How many tickets are you going to buy? ")
        if not buyTickets.isdigit():
            print("Only input numbers")
            continue
        else:
            buyTickets = int(buyTickets)
        
        if buyTickets <= 4 and tickets >= buyTickets:
            tickets -= buyTickets
            buyers += 1
            print("Remaining tickets: %d, Buyers: %d" % (tickets, buyers))
        else:
            print("Not enough tickets or tickets cannot exceed 4")
            print("Remaining tickets: %d" % tickets)
    print("Sold out")

## Add an article to country names
# @param country {string} - the country word
# @return {string} - new string with an article before the country's word
def nomsDePays(country):
    if country in 'États-Unis Pays-Bas':
        return 'les ' + country
    if country in 'Belize Cambodge Mexique Mozambique Zaïre Zimbabwe':
        return 'le ' + country

    wordLength = len(country)
    lastChar = country[wordLength-1]
    if lastChar in 'eEèÈéÉ':
        return 'la ' + country
    
    firstChar = country[0]
    if firstChar in 'aiueoAIUEO':
        return 'l\'' + country
    
    return 'le ' + country

def Lab5_nomsDePaysExercise():
    countries = ['Afghanistan', 'Belize', 'Belgique', 'Cambodge', 'Canada', 'Mexique', 'Mozambique', 'Zaïre', 'Zimbabwe', 'États-Unis', 'Pays-Bas']
    for country in countries:
        print(nomsDePays(country))
    
def blackjack():
    computer = randint(1,10)
    user = randint(1,10) + randint(1,10)
    print('Your cards: %d' % user)
    
    isDeal = input('Deal? (y/n): ')
    while isDeal == 'y':
        newCard = randint(1,10)
        print('New card %d' % newCard) 
        user += newCard
        print('Your cards: %d' % user)
        if user > 21:
            print('You lose')
            return
        else:
            isDeal = input('Deal? (y/n): ')
    
    while computer < 17 and user < 21:
        newCard = randint(1,10)
        print('New card for computer %d' % newCard)
        computer += newCard
        print('Computer cards: %d' % computer)
        if computer > 21:
            print('Computer loses')
            return

    if user > computer:
        print('You win')
    else:
        print('Computer win')

blackjack()