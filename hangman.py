import os
import string
import random
from faker import Faker


fake = Faker()

data = {
    "first name": [fake.first_name() for _ in range(5)],
    "city": [fake.city() for _ in range(5)],
    "country": [fake.country() for _ in range(5)]
}

lett = string.ascii_lowercase
letters = list(lett)
print(letters)

category, words = random.choice(list(data.items()))
word = random.choice(words)
word = f"{word}".lower()
word = word.replace(' ', '')
random_index = random.randint(0, len(word) - 1)
sep_word = list(word)                                             
masked_word = ["_" for _ in word] 
masked_word[random_index] = word[random_index]

CHANCES = 3
RED_PREFIX = "\033[41m"
GREEN_PREFIX = "\033[42m"
COLOR_SUFFIX = "\033[0m"

color_data = {
    "red": RED_PREFIX,
    "green": GREEN_PREFIX
}

death_road = {
    3: r"""
     
        
       ._.
       \O/
       / \
    """,
    2: r"""
    |
    |   
    |   o
    |  \O/
    |  / \
    """,
    1:
    r"""
    |====
    |
    |   o
    |  \O/
    |  / \
    """,
    0:
    r"""
    |====
    |   |
    |  x_x
    |  \O/
    |  / \
    """
}


while CHANCES > 0:
    os.system("cls")
    print(death_road[CHANCES])
    print(f"Category is '{category}'. You have {CHANCES} chances. Good luck!")
    print("".join(masked_word))
    for letter in letters:
        print(letter, end=" ")
    print()
    let = input(">> ")
    
    if not let:
        continue

    if let in word:
        c = word.count(let)
        
        for _ in range(c):
            try:
                idx = sep_word.index(let)
                masked_word[idx] = let
                sep_word[idx] = "*"
                indx_string = letters.index(let)
                letters[indx_string] = f"{color_data['green']}{let}{COLOR_SUFFIX}"
                
            except ValueError:
                input("You already input this letter. Try another one. :))")
                continue
        print("".join(masked_word))
    else:
        CHANCES -= 1
        indx_string = letters.index(let)
        letters[indx_string] = f"{color_data['red']}{let}{COLOR_SUFFIX}"
    guessed = all([ch=="*" for ch in sep_word])

    if guessed:
        exit("Perfect. You find the invisible word.!!!")

print(word)