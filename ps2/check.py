def is_word_guessed(secret_word, letters_guessed):
    count = len(secret_word)
    for i in secret_word:
        for j in letters_guessed:
            if i == j:
                count-=1
                if count == 0:
                    return True
                else:
                    return False

secret_word = input("enter sec word: ")
letters_guessed = ['a','k','s']

is_word_guessed(secret_word,letters_guessed)
