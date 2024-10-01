def digits():
    print("Enter 5 digits number:")
    digit = int(input())
    print(int(digit / 10000))
    print(int((digit % 10000) / 1000))
    print(int((digit % 1000) / 100))
    print(int((digit % 100) / 10))
    print(int((digit % 10)))

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

truncate()