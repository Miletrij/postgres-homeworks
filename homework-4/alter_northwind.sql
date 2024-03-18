-- Подключиться к БД Northwind и сделать следующие изменения:
-- 1. Добавить ограничение на поле unit_price таблицы products (цена должна быть больше 0)
alter table products add CONSTRAINT chk_products_price check (unit_price>0)

-- 2. Добавить ограничение, что поле discontinued таблицы products может содержать только значения 0 или 1
alter table products add CONSTRAINT chk_products_discontinued check (discontinued in (0, 1))

-- 3. Создать новую таблицу, содержащую все продукты, снятые с продажи (discontinued = 1)
create table discontinued_products (product_name varchar not null, discontinued int);
insert into discontinued_products select product_name, discontinued from products where discontinued=1

-- 4. Удалить из products товары, снятые с продажи (discontinued = 1)
-- Для 4-го пункта может потребоваться удаление ограничения, связанного с foreign_key. Подумайте, как это можно решить, чтобы связь с таблицей order_details все же осталась.
alter table order_details drop CONSTRAINT fk_order_details_products,
add CONSTRAINT fk_order_details_products
foreign key (product_id) references products (product_id) on delete cascade
