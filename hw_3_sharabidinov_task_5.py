import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n: int):
    if 0 < n <= len(nouns):
        jokes_list = []
        for index in range(n):
            jokes_list.append(random.choice(nouns) + ' ' + random.choice(adverbs) + ' ' + random.choice(adjectives))
        return jokes_list


print(get_jokes(3))
