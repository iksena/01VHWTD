# Author: S336282
# Computer Programming in Python, A.A. 2024/25
# Lab Practice 04, Part 1 Basic Cycles, 04.1.7 Words in pieces

def wordsInPieces_s336282():
    word = input("Input word: ")
    
    for i in range(1,len(word)+1): # if word length is 3: i = 1 to 3
        for j in range(len(word)): # if word length is 3: j = 0 to 2
            if i+j <= len(word): # if word length is 3: i+j should not exceed 3
                print(word[j:i+j]) # if word length is 3: print 0:1, 1:2, 2:3, 0:2, 1:3, 0:3

wordsInPieces_s336282()