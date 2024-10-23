def wordsInPiecesExercise():
    word = input("Input word: ")
    
    for i in range(1,len(word)+1): # if word length is 3: i = 1 to 3
        for j in range(len(word)): # if word length is 3: j = 0 to 2
            if i+j <= len(word): # if word length is 3: i+j should not exceed 3
                print(word[j:i+j])

wordsInPiecesExercise()