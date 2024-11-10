def separate_words_by_length(text):
    words = text.split() 
    even_length_words = []
    odd_length_words = []
    
    for word in words:
        if len(word) % 2 == 0:
            even_length_words.append(word)  
        else:
            odd_length_words.append(word)   

    
    print("Слова парної довжини:")
    for word in even_length_words:
        print(word)
    
    
    print("\n Слова непарної довжини:")
    for word in odd_length_words:
        print(word)


text = input("Введіть текст: ")
separate_words_by_length(text)
