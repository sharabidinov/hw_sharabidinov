import requests

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()


def currency_rate(currency: str):
    if currency.upper() not in response['Valute']:
        return None
    result = response['Valute'][currency.upper()]['Value']
    return result


'''Я не стал использовать Decimal, так как при заупске программы вы можете увидеть что тип float (спасибо json :) )'''

print(type(currency_rate('USD')))
print(currency_rate('USD'))
print(currency_rate('UsD'))
print(currency_rate('USfhD'))
