import datetime
import requests

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()


def currency_rate(currency: str):
    if currency.upper() not in response['Valute']:
        return None
    date_time = datetime.datetime.now().strftime('%x %X')
    value = response['Valute'][currency.upper()]['Value']
    result = f'Курс {currency.upper()} к RUB на  момент {date_time} составляет {value}'
    return result


'''Я не стал возиться с получением даты из ответа сервера, просто импортировал билиотеку datetime и через нее вывел 
время. Также если проверить тип данных, то программа выведет тип данных str, из-за того что использовали 
форматирование. Опять же это можно решить, но мне было лень с этим ввозиться, так как в условии этого задания ничего 
не было написано про это. А во втором задании я сделал все как написано в тз) '''
