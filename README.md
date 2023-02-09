# Тестовое задание OKKAM

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

Сделал простой веб-интерфейс для проверки результата: http://0.0.0.0/form/
