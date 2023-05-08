def update_geo_logs():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]

    new_geo_logs = []
    for visit in geo_logs:
        for v in visit.values():
            if "Россия" in v:
                new_geo_logs.append(visit)
    return new_geo_logs


def unique_numbers():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    unique_ids = []
    for value in ids.values():
        unique_ids.extend(value)
    return sorted(list(set(unique_ids)))

def query_percent():
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
    total_request_quantity = len(queries)
    temporary_dictionary = {}
    result = []
    for query in queries:
        count = len(query.split())
        temporary_dictionary[count] = temporary_dictionary.get(count, 0) + 1
    for key in temporary_dictionary:
        percent_of_queries = round(
            temporary_dictionary[key] / total_request_quantity * 100, 1
        )
        res = str(key), str(percent_of_queries)
        result.append(res)
    return sorted(result)

