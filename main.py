def replace_last_letter_with_underscore(text):

    words = text.split()
    
    modified_words = []
    for word in words:
        if word.isalpha():  
            modified_word = word[:-1] + "_"
        else:
            modified_word = word
        
        modified_words.append(modified_word)

    return " ".join(modified_words)

if __name__ == "__main__":
    input_text = input("Введіть слова: ")
    output_text = replace_last_letter_with_underscore(input_text)
    print("Результат:", output_text)
