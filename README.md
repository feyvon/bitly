# Обрезка ссылок с помощью Битли

Обрезает ссылку и превращает в битлинк. Если ввести битлинк, то выведется кол-во кликов по нему.

### Как установить

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

После установки вам надо будет создать .env файл в котором следует указать ваш токен:
```
BITLY_TOKEN = "ваш токен"
```

### Как запустить

Для запуска программы вы должны указать аргумент ссылки.

Для сокращения ссылки введите её в полном виде:
```
python main.py https://www.google.ru
Короткая ссылка:  https://bit.ly/4aveLC1
```
Для вывода кол-ва кликов достаточно ввести битлинк:
```
python main.py https://bit.ly/4aveLC1
Количество кликов: 0
```
### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](htttps://dvmn.org).
