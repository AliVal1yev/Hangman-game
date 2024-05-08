import os
import random
from faker import Faker


fake = Faker()

data = {
    "first name": [fake.first_name() for _ in range(5)],
    "city name": [fake.city() for _ in range(5)],
    "country": [fake.country() for _ in range(5)]
}

category, words = random.choice(list(data.items()))
word = random.choice(words)
word = f"{word}".lower()
random_index = random.randint(0, len(word) - 1)
sep_word = list(word)                                             
masked_word = ["_" for _ in word] 
masked_word[random_index] = word[random_index]
CHANCES = 3

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
            except ValueError:
                input("You already input this letter. Try another one. :))")
                continue
        print("".join(masked_word))
    else:
        CHANCES -= 1
    guessed = all([ch=="*" for ch in sep_word])

    if guessed:
        exit("Perfect. You find the missing word.!!!")

print(word)