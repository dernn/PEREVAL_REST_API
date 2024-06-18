# PEREVAL REST API
## Спринт 2
### Задача 1. Новые методы для _REST API_

Реализация:

* **_GET `/submitData/<id>`_** — получает одну запись (перевал) по её id.
Выводит всю информацию об объекте, в том числе статус модерации.
* **_PATCH `/submitData/<id>`_** — редактирование существующей записи _(partial_update)_, если она в статусе _new_.
Редактировать можно все поля, кроме _данных пользователя, статуса модерации и времени создания записи_.
Метод принимает тот же самый json, что и метод _submitData_.
<br><br>
В качестве результата меотд **_PATCH_** возвращает два значения:
  * _**state**_:
    * 1 — если успешно удалось отредактировать запись;
    * 0 — в противном случае,
  * _**message**_ — сообщение, если обновить запись не удалось.


* **_GET `/submitData/?user__email=<email>`_** — список данных обо всех объектах, которые пользователь с почтой `<email>` отправил на сервер.


### Задача 2. Деплой

Публикация API на хостинге **pythonanywhere**.

_Реализация доступна по адресу_:
```
https://dernn.pythonanywhere.com/api/
```
