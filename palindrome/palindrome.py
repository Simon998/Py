with open("words.txt") as file:
    for line in file:
        word = line.strip()  # remove space
        if word == word[::-1]:  # check if the word is equal to its reverse
            print(f"{word} is a palindrome")
        else:
            print(f"{word} is not a palindrome")


