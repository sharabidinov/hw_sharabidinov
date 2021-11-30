import re

EMAIL_PARSE = re.compile(r'^(?P<name>\w+)@(?P<domain>\w+\.\w+)$')


def mail_parse(email: str):
    if not EMAIL_PARSE.match(email):
        raise ValueError('invalid mail', email)
    return EMAIL_PARSE.match(email).groupdict()


print(mail_parse('hello12@mail.ru'))
print(mail_parse('hello12@gmail.com'))
print(mail_parse('hello1_mail.ru'))
