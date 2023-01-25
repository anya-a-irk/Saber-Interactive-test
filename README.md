# Saber-Interactive-test
## SQL
Таблица history находится в прикреплённом файле test.db (SQLite)
- issue_key – уникальный ключ задачи
- status – статус задачи
- minutes_in_status – количество минут, которое задача находилась в статусе
- previous_status – предыдущий статус задачи
- started_at – время создания статуса задачи, unix миллисекунды 
- ended_at – время перехода задачи в другой статус, unix миллисекунды 

####  SQL 1
Напишите запрос, который выведет, сколько времени в среднем задачи каждой группы находятся в статусе “Open” 
Условия:
Под группой подразумевается первый символ в ключе задачи. Например, для ключа “C-40460” группой будет “C”
Задача может переходить в один и тот же статус несколько раз.
Переведите время в часы с округлением до двух знаков после запятой.

Решение:
```sql
SELECT substr(issue_key,1,1) as task_group, round(avg(sum_minuts), 2) as mean_group_minutes FROM
(SELECT issue_key, status, sum(minutes_in_status) as sum_minuts FROM history
WHERE status = 'Open'
GROUP BY issue_key)
GROUP BY substr(issue_key,1,1);
```


####  SQL 2 
Напишите запрос, который выведет ключ задачи, последний статус и его время создания для задач, которые открыты на данный момент времени.
Условия:
Открытыми считаются задачи, у которых последний статус в момент времени не “Closed” и не “Resolved”
Задача может переходить в один и тот же статус несколько раз.
Оформите запрос таким образом, чтобы, изменив дату, его можно было использовать для поиска открытых задач в любой момент времени в прошлом
Переведите время в текстовое представление

Решение:
```sql
SELECT issue_key, status, CAST(MAX(started_at) as varchar) as started_at
FROM history
WHERE started_at < '16000000000000'
GROUP BY issue_key
HAVING status not in ('Closed', 'Resolved');
```

## PYTHON
Создайте интерактивное приложение с помощью одного из веб фреймворков (streamlit/dash/panel)
Исторические данные и список активов необходимо получить с помощью апи:  https://docs.coincap.io/ 

Для запуска приложения необходимо скачать репозиторий и запустить скрипт:
```sh
python viewer.py 
```
