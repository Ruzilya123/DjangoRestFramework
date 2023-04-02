from rest_framework import authentication

class BearerAuthentication(authentication.TokenAuthentication):
    keyword = 'Bearer' # Переопределение ключевого слова для токена

# Проверка на валидность токена, и возврат объекта пользователя по токену