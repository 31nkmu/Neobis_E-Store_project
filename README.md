# Neobis_E-Store_project
___
# Описание проекта
В проекте реализован интернет магазин.

Имеется полная работа с пользователем, отправка на почту через celery.
Создание продукта, заказа.
Лайки, рейтинги, избранное, комментарии

# Установка
* Склонируй репозиторий используя команду
```
git clone git@github.com:31nkmu/Neobis_E-Store_project.git
```
* Создай виртуальное окружение используя команду
```
python3 -m venv <name of your environment> 
```

* Активируй виртуальное окружение
``` 
source <name of your environment>/bin/activate 
```

* Установи зависимости
``` 
pip install -r requirements.txt 
```

* Создай .env файл
```
touch .env
```

* Запиши данные в файл .env (смотри пример в файле .evn.example)

* Сделай миграции
```
make migrate
```

* Запусти свой проект
``` 
make run
``` 
* Запусти Celery
```
make celery
```
---
