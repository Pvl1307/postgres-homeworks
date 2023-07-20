-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar

CREATE TABLE student (
  student_id SERIAL PRIMARY KEY,
  first_name VARCHAR,
  last_name VARCHAR,
  birthday DATE,
  phone VARCHAR
);

-- 2. Добавить в таблицу student колонку middle_name varchar

ALTER TABLE student
ADD COLUMN middle_name VARCHAR;

-- 3. Удалить колонку middle_name

ALTER TABLE student
DROP COLUMN middle_name;

-- 4. Переименовать колонку birthday в birth_date

ALTER TABLE student
RENAME COLUMN birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)

ALTER TABLE student
ALTER COLUMN phone TYPE VARCHAR(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора

INSERT INTO student (first_name, last_name, birth_date, phone)
VALUES ('John', 'Doe', '1995-05-10', '123456789'),
       ('Jane', 'Smith', '1998-09-15', '987654321'),
       ('Michael', 'Johnson', '2000-02-20', '555666777');

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние

DELETE FROM student;
