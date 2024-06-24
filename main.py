import sqlite3

# Создаем подключение к базе данных (файл students.db будет создан)
connection = sqlite3.connect('students.db')
cursor = connection.cursor()

# Создаем таблицу students, если она еще не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER NOT NULL
)
''')

# Создаем таблицу grades с внешним ключом
cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
id INTEGER PRIMARY KEY AUTOINCREMENT,
student_id INTEGER NOT NULL,
subject TEXT NOT NULL,
grade FLOAT NOT NULL,
FOREIGN KEY (student_id) REFERENCES students(id)
)
''')

connection.commit()
connection.close()

class University:
    def __init__(self, name_university):
        self.name_university = name_university

# метод добавления студентов
    def add_student(self, name, age):
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()

        # Добавляем данные в таблицу
        cursor.execute('''
            INSERT INTO students (name, age)
            VALUES (?, ?)
        ''', (name, age))
        student_id = cursor.lastrowid

        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()

        print(f'Добавили студента {name}, возрастом {age} с id {student_id}')
        return student_id


# метод добавления оценок
    def add_grade(self, student_id, subject, grade):
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()

# Добавляем данные в таблицу
        cursor.execute('''
            INSERT INTO grades (student_id, subject, grade)
            VALUES (?, ?, ?)
        ''', (student_id, subject, grade))

        # Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()

        print(f'Добавили оценку {grade} по предмету {subject} для студента с id {student_id}')


# метод возврата значений
    def get_students(self, subject=None):
        # Устанавливаем соединение с базой данных
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()

#         Если предмет  указан(if subject:):SQL-запрос выбирает имена студентов, их возраст, предмет и оценку из таблиц students и grades.
# JOIN grades g ON s.id = g.student_id соединяет две таблицы по полю id студента и можно получить оценки, соответствующие каждому студенту.
# WHERE g.subject = ? ограничивает выборку только теми записями, где предмет соответствует указанному в параметре subject.
# cursor.execute выполняет SQL-запрос с параметром subject, переданным в запрос.
# Результат запроса сохраняется в students_data с помощью метода cursor.fetchall(), который извлекает все строки результата запроса.

        if subject:
            # Получаем список студентов по определенному предмету
            cursor.execute('''
                SELECT s.name, s.age, g.subject, g.grade
                FROM students s
                JOIN grades g ON s.id = g.student_id
                WHERE g.subject = ?
            ''', (subject,))

# Если не указан предмет: SQL - запрос выбирает имена студентов, их возраст, предмет и оценку без ограничений.
# Будут получены данные обо всех студентах и всех их оценках. Результат сохраняется в students_data.
        else:
            # Получаем список всех студентов и их оценок
            cursor.execute('''
                SELECT s.name, s.age, g.subject, g.grade
                FROM students s
                JOIN grades g ON s.id = g.student_id
            ''')

        students_data = cursor.fetchall()

        # Закрываем соединение
        connection.close()

        return students_data

# Пример использования класса
u1 = University('Urban')
student_id_ivan = u1.add_student('Ivan', 26) # id - 1
student_id_ilya = u1.add_student('Ilya', 24) # id - 2
student_id_oleg = u1.add_student('Oleg', 28) # id - 3
student_id_olya = u1.add_student('Olya', 21) # id - 4


u1.add_grade(student_id_ivan, 'Python', 4.8)
u1.add_grade(student_id_ilya, 'PHP', 4.3)
u1.add_grade(student_id_oleg, 'PHP', 4.1)
u1.add_grade(student_id_olya,'PHP', 4.0)

print(u1.get_students())
print(u1.get_students('Python'))
print(u1.get_students('PHP'))






# ЧЕРНОВИК


# import sqlite3
#
# # Создаем подключение к базе данных (файл my_database.db будет создан)
# connection = sqlite3.connect('students.db')
# cursor = connection.cursor()
#
# # Создаем таблицу students, если она еще не существует
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS students (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# age INTEGER
# )
# ''')
#
# # Создаем таблицу grade с внешним ключом
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS grade (
# id INTEGER PRIMARY KEY,
# student_id INTEGER,
# subject TEXT NOT NULL,
# grade FLOAT,
# FOREIGN KEY (student_id) REFERENCES students(id)
# )
# ''')
#
# connection.commit()
# connection.close()
# class University:
#
#     def __init__(self, name_university):
#         self.name_university = name_university
#
#     def add_student(self, name, age):
#         self.name = name
#         self.age = age
#         print(f'Добавили студента {self.name}, возрастом {self.age}')
#
#         # Устанавливаем соединение с базой данных
#         connection = sqlite3.connect('students.db')
#         cursor = connection.cursor()
#
#         # Добавляем данные в таблицу
#         cursor.execute('''
#             INSERT INTO students (name, age)
#             VALUES (?, ?)
#         ''', (self.name, self.age))
#
#         # Сохраняем изменения и закрываем соединение
#         connection.commit()
#         connection.close()
#
#
#     def add_grade(self, student_id, subject, grade):
#         self.student_id = student_id
#         self.subject = subject
#         self.grade = grade
#         print(f'Добавили номер студента: {self.student_id}, по предмету: {self.subject} с оценкой {self.grade}')
#
#         # Устанавливаем соединение с базой данных
#         connection = sqlite3.connect('students.db')
#         cursor = connection.cursor()
#
#         # Добавляем данные в таблицу
#         cursor.execute('''
#             INSERT INTO grade (student_id, subject, grade)
#             VALUES (?, ?, ?)
#         ''', (self.student_id, self.subject, self.grade))
#
#         # Сохраняем изменения и закрываем соединение
#         connection.commit()
#         connection.close()
#
#     # Возвращаем данные о студентах:
#     def get_students(self, subject=None):
#         self.subject = subject
#         # Устанавливаем соединение с базой данных
#         connection = sqlite3.connect('students.db')
#         cursor = connection.cursor()
#
#
#         # Получаем и возвращаем данные, используя полученный id
#         cursor.execute('SELECT * FROM students WHERE id = ?', (subject,))
#         inserted_data = cursor.fetchone()
#
#         # Сохраняем изменения и закрываем соединение
#         connection.commit()
#         connection.close()
#
#         return inserted_data
#
#         # # Сохраняем изменения и закрываем соединение
#         # connection.commit()
#         # connection.close()
#
#
#
#
# u1 = University('Urban')
# u1.add_student('Ivan', 26) # id - 1
# u1.add_student('Ilya', 24) # id - 2
#
# u1.add_grade(1, 'Python', 4.8)
# u1.add_grade(2, 'PHP', 4.3)
#
# print(u1.get_students())
# print(u1.get_students('Python'))







# # МЕТОД ВОЗВРАЩЕНИЯ ДАННЫХ С БД
#
#    def save_and_get_data(self):
#         # Устанавливаем соединение с базой данных
#         connection = sqlite3.connect('my_database.db')
#         cursor = connection.cursor()
#
#         # получаем id последней вставленной строки
#         last_id = cursor.lastrowid
#
#         # Получаем и возвращаем данные, используя полученный id
#         cursor.execute('SELECT * FROM students WHERE id = ?', (last_id,))
#         inserted_data = cursor.fetchone()
#
#         # Сохраняем изменения и закрываем соединение
#         connection.commit()
#         connection.close()
#
#         return inserted_data
#
# # Пример создания объекта класса и добавления его в базу данных
# student = Student('Иван', 20, 'Математика', 4.5)
# inserted_student_data = student.save_and_get_data()
# print(inserted_student_data)







# МЕТОД ДОБАВЛЕНИЯ В БД

# import sqlite3
#
# class Student:
#     def __init__(self, name, age, subject, grade):
#         self.name = name
#         self.age = age
#         self.subject = subject
#         self.grade = grade
#
#     def save_to_db(self):
#         # Устанавливаем соединение с базой данных
#         connection = sqlite3.connect('my_database.db')
#         cursor = connection.cursor()
#
#         # Добавляем данные в таблицу
#         cursor.execute('''
#             INSERT INTO students (name, age, subject, grade)
#             VALUES (?, ?, ?, ?)
#         ''', (self.name, self.age, self.subject, self.grade))
#
#         # Сохраняем изменения и закрываем соединение
#         connection.commit()
#         connection.close()
#
# # Пример создания объекта класса и добавления его в базу данных
# student = Student('Иван', 20, 'Математика', 4.5)
# student.save_to_db()







# import sqlite3
#
# # Устанавливаем соединение с базой данных
# connection = sqlite3.connect('tasks.db')
# cursor = connection.cursor()
#
# # Создаем таблицу Tasks
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Tasks (
# id INTEGER PRIMARY KEY,
# title TEXT NOT NULL,
# status TEXT DEFAULT 'Not Started'
# )
# ''')
#
#
# # Функция для добавления новой задачи
# def add_task(title):
#     cursor.execute('INSERT INTO Tasks (title) VALUES (?)', (title,))
#     connection.commit()
#
#
# # Функция для обновления статуса задачи
# def update_task_status(task_id, status):
#     cursor.execute('UPDATE Tasks SET status = ? WHERE id = ?', (status, task_id))
#     connection.commit()
#
#
# # Функция для вывода списка задач
# def list_tasks():
#     cursor.execute('SELECT * FROM Tasks')
#     tasks = cursor.fetchall()
#     for task in tasks:
#         print(task)
#
#
# # Добавляем задачи
# add_task('Подготовить презентацию')
# add_task('Закончить отчет')
# add_task('Подготовить ужин')
#
# # Обновляем статус задачи
# update_task_status(2, 'In Progress')
#
# # Выводим список задач
# list_tasks()
#
# # Закрываем соединение
# connection.close()




# import sqlite3
#
# # Создаем подключение к базе данных (файл my_database.db будет создан)
# connection = sqlite3.connect('students.db')
# connection.close()
#
#
# # Создаем подключение к базе данных (файл my_database.db будет создан)
# connection = sqlite3.connect('my_database.db')
# cursor = connection.cursor()
#
# # Создаем таблицу students, если она еще не существует
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS students (
# id INTEGER PRIMARY KEY,
# name TEXT NOT NULL,
# age INTEGER
# )
# ''')
#
# # Создаем таблицу grade с внешним ключом
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS grade (
# id INTEGER PRIMARY KEY,
# student_id INTEGER,
# subject TEXT NOT NULL,
# grade FLOAT,
# FOREIGN KEY (student_id) REFERENCES students(id)
# )
# ''')
#
# # Сохраняем изменения и закрываем соединение
# connection.commit()
# connection.close()



# name TEXT NOT NULL,
# age INTEGER,
# subject TEXT NOT NULL,
# grade FLOAT

# # Создаем подключение к базе данных (файл my_database.db будет создан)
# connection = sqlite3.connect('students.db')
# connection.close()

# УРОК

# import sqlite3
#
# # Сперва создадим соединение с нашей базой данных, нельзя коммитить базу данных в репозиторий!
# conn = sqlite3.connect('Northwind.sl3')
# # Укажем тип получаемых данных
# conn.text_factory = bytes
# # Создадим курсор - специальный объект, с помощью которого мы сможем делать запросы к БД на языке запросов
# cursor = conn.cursor()
#
# # Отбор данных из БД:
# # SELECT <список-полей> FROM <имя-таблицы>[ WHERE <условие>]
# # Пример:
# # Требуется отобрать список заказов,
# # для которых значение поля Freight (плата за груз) больше значения 100,
# # а регион доставки (ShipRegion) -- 'RJ'
# cursor.execute("SELECT * FROM Orders WHERE (Freight > 100) AND (ShipRegion = 'RJ')")
#
# # Получение отобранных значений:
# results = cursor.fetchall()
# print(f'Здесь выведется список значений, подходящих под заданные условия: {results}')
#
# results_one_more_time = cursor.fetchall()
# print(f'А здесь пустой список: {results_one_more_time}')
# # Это происходит из-за того, что для повторного получения результата из курсора, необходимо создать новый запрос.
#
# # Попробуем получить именя всех клиентов, фамилии которых начинаются на C:
# cursor.execute("SELECT ContactName FROM Customers WHERE ContactName LIKE '% C%'")
# another_results = cursor.fetchall()
# print(f'Список клиентов: {another_results}')
#
# # Удаление записи
# cursor.execute("DELETE FROM Orders WHERE OrderID='10'")
# # Изменения необходимо подтвердить:
# conn.commit()
#
# # Запись в БД:
# cursor.execute("INSERT INTO Orders (OrderID, CustomerID, EmployeeID) VALUES ('10', 'Anton', '5')")
# conn.commit()
#
# cursor.execute("SELECT * FROM Orders WHERE OrderID = 10")
# changes = cursor.fetchall()
# print(f'Внесенные нами изменения: {changes}')
#
# # Закрываем соединение
# conn.close()
