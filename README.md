# Тестовое задание OKKAM

<div align="center">

[![CodeFactor](https://www.codefactor.io/repository/github/nikitadushakov/okkam_test_assignment/badge)](https://www.codefactor.io/repository/github/nikitadushakov/okkam_test_assignment)

</div>


```
Имеется дамп базы data.csv со следующими полями:
•	Date – дата в формате yyyymmdd
•	respondent – уникальный номер респондента
•	Sex – пол респондента (1=М, 2=Ж)
•	Age – возраст респондента
•	Weight – Некая статистика респондента для этого дня
Необходимо:
1.	Загрузить данные в таблицу СУБД SQL на ваш выбор (но не SQLlite)
2.	Разработать API с одним GET эндпоинтом /getPercent который будет выполнять следующий алгоритм:
a.	На вход эндпоинта приходят 2 параметра: audience1 и audience2.
i.	Аудитории будут приходить в формате SQL синтаксиса, например “Age BETWEEN 18 AND 35” или “Sex = 2 AND Age >= 18”
b.	Для каждой из аудиторий отобрать из таблицы всех респондентов, подходящих под параметры
c.	Для каждой из аудиторий взять средний Weight респондента этой аудиторий, сгруппировав по их уникальному номеру
d.	Далее вычислить процент вхождения второй аудитории в первую, основываясь на среднем Weight. Пример:
i.	Имеем первую аудиторию, в которую входят 
resp1 с avg(Weight)=1, resp2 с avg(Weight)=2 и resp3 с avg(Weight)=3
ii.	Имеем вторую аудиторию, в которую входят
resp2, resp3 и resp4 с avg(Weight) = 2,3,4 соответственно
iii.	Видим, что аудитории пересекаются респондентами resp2 и resp3, у которых avg(Weight) равен 2 и 3 (Средний Weight не может быть разным у одного и того же респондента).
Значит процент вхождения второй аудитории в первую 
будет равен (2+3) / (1+2+3) = 0.8(3)
e.	Предусмотреть варианты:
i.	Аудитории могут быть идентичными
ii.	Аудитории могут не пересекаться вообще
iii.	Вторая аудитория может быть подмножеством первой
iv.	Первая аудитория может быть подмножеством второй 
f.	Отдать респонс в формате {‘percent’: результат} 
3.	Обернуть API в Docker контейнер
4.	Подготовить docker-compose конфиг для связки API+СУБД
a.	База данных должна быть создана и наполнена
b.	API слушает 80 порт
5.	Опционально:
a.	Позаботиться об отказоустойчивости
b.	Позаботиться о быстродействии (учитывая, что данные не будут изменены ретроспективно)
c.	Порядок в коде – pep8, докстринги, тайпинг, структура проекта
```


## Структура проекта

```
├── README.md
├── api
│   ├── Dockerfile
│   ├── core
│   │   ├── __init__.py
│   │   ├── __main__.py
│   │   ├── action.py
│   │   ├── db.py
│   │   ├── endpoint.py
│   │   ├── models.py
│   │   └── queries.py
│   ├── requirements.txt
│   └── static
│       ├── fonts
│       │   ├── Menlo-Regular.ttf
│       │   └── Montserrat-Regular.ttf
│       ├── index.html
│       ├── main.js
│       └── style.css
├── database
│   ├── OKKAM_Middle Python Developer_data.csv
│   └── db.sql
└── docker-compose.yml
```

## Запуск

```bash
docker compose up -d
```

Сделал простой веб-интерфейс для проверки результата: http://localhost/form/
