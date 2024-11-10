def count_first_letter_occurrences(text):
    if not text:
        return 0

    first_letter = text[0].lower()
    count = sum(1 for char in text.lower() if char == first_letter)
    
    return count

if __name__ == "__main__":
    input_text = input("Введіть текст: ")
    occurrences = count_first_letter_occurrences(input_text)
    print(f"Перша літера '{input_text[0]}' зустрічається {occurrences} разів.")
