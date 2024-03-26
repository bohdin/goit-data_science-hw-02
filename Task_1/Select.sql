-- Отримати всі завдання певного користувача.
select *
from tasks t 
where user_id = 15

-- Вибрати завдання за певним статусом.
select *
from tasks t 
where status_id = (select id
				   from status s
				   where name like 'new')

-- Оновити статус конкретного завдання.
update tasks 
set status_id = 2
where id  = 79

-- Отримати список користувачів, які не мають жодного завдання. 
select *
from users u 
where id not in (select user_id
                 from tasks t)

-- Додати нове завдання для конкретного користувача.
insert into tasks(title, status_id, user_id)
values ('TEST', 1, 48)

-- Отримати всі завдання, які ще не завершено.
select *
from tasks t 
where status_id != 3

-- Видалити конкретне завдання.
delete 
from tasks t 
where id = 99

-- Знайти користувачів з певною електронною поштою. 
select *
from users u 
where email like 'a%'

-- Оновити ім'я користувача.
update users 
set fullname = 'Boda Tsviliy'
where id = 1

-- Отримати кількість завдань для кожного статусу.
select status_id, count(id)  
from tasks t 
group by status_id 

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти.
select *
from tasks t 
join users u on t.user_id = u.id 
where u.email like '%@example.net'

-- Отримати список завдань, що не мають опису.
select *
from tasks t 
where description is null 

-- Вибрати користувачів та їхні завдання, які є у статусі in progress
select u.fullname, t.title , s."name" 
from users u 
inner join tasks t on u.id = t.user_id 
inner join status s on s.id = t.status_id 
where s."name" like 'in progress'


-- Отримати користувачів та кількість їхніх завдань.
select u.fullname, count(t.id)
from users u 
left join tasks t on t.user_id = u.id 
group by u.id 