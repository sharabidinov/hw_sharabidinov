def thesaurus(*args: str):
    names_data = {}
    for name in sorted(args):
        names_data.setdefault(name[0], [])
        names_data[name[0]].append(name)
    return names_data


print(thesaurus('Илья', 'Иван', 'Алексей'))
