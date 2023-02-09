# Тестовое задание OKKAM

## Структура проекта

```
├── Readme.md
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
│   └── requirements.txt
├── database
│   ├── OKKAM_Middle Python Developer_data.csv
│   └── db.sql
└── docker-compose.yml
```

## Запуск

```bash
docker compose up
```

Сделал простой веб-интерфейс для проверки результата: http://0.0.0.0/form/
