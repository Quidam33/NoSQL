Итоговое задание по модулю 3

Предмет: Нереляционные базы данных

Выполнила: Новикова Алина Олеговна

## Отчет и описание 
report/report.md

## Структура проекта

app/ - консольный интерфейс  
scripts/ - скрипты и тестирование  
report/ - отчет  
results/ - результаты тестирования

### Установка и запуск

- pip install -r requirements.txt
- Запуск MongoDB:
	- mongo scripts/init_db.js  
	- mongo scripts/shard_setup.js
- Запуск интерфейса:
	- python app/main.py
- Нагрузочное тестирование:
	- python scripts/load_test.py
