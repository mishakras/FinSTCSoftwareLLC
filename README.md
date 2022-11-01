# FinSTCSoftwareLLC
Тестовое задание для компании FinSTC Software LLC.

Описание установки зависимостей:
  1) в командной строке в папке flask_server выполнить команду pip install Flask-Cors
  2) в командной строке в папке client выполнить команду npm install

Описание запуска программы:
  1) Бек запускается через командную строку в папке flask_server командой python __init__.py 
  2) Фронт запускается через командную строку в папке client командой npm run serve
Результат работы виден по адресу выведенному в консоли после выполнения команды npm run serve, у меня это http://localhost:8080/

Описание тестового задания:
Разработать приложение, в котором реализовать todo-list (план дел на ближайшее время) со следующими простыми возможностями:
1) добавление новой задачи
2) удаление задачи
3) отметка задачи как выполненной/не выполненной
4) синхронизация состояния задач с базой данных (чтобы после перезагрузки страницы данные не пропадали)
Основные требования:
1) адаптивная верстка;
2) кросс-браузерность.
Верстка должна быть выполнена с использованием препроцессора scss или sass. Желательно использовать сетку bootstrap 4(5). Дизайн и остальные технологии остаются на усмотрение кандидата. Составные части приложения должны быть в компонентах.
Задачи нельзя поставить на «вчерашний» день.
