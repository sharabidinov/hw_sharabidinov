def thesaurus_adv(*args: str):
    full_names_data = {}
    for surname in sorted(list(args)):
        full_names_data.setdefault(surname.split()[1][0], {})
        full_names_data[surname.split()[1][0]].setdefault(surname.split()[0][0], [])
        full_names_data[surname.split()[1][0]][surname.split()[0][0]].append(surname)
    return full_names_data


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
