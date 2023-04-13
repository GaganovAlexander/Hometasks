import psycopg2.extras
from os import getenv
from datetime import datetime


def start_db():
    global db, cur
    db = psycopg2.connect(
        f"dbname=postgres user=postgres password={getenv('password')}")
    cur = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("""CREATE TABLE IF NOT EXISTS students(
                id SERIAL PRIMARY KEY, 
                name VARCHAR(255), 
                department VARCHAR(255))""")
    cur.execute("""CREATE TABLE IF NOT EXISTS exams(
                id SERIAL PRIMARY KEY, 
                student_id INTEGER, 
                subject_id INTEGER, 
                point INTEGER,
                exam_date DATE DEFAULT NOW(),
                CONSTRAINT fk_student_id 
                FOREIGN KEY (student_id) REFERENCES students(id)
                )""")
    db.commit()


def insert_student(name: str, department: str):
    cur.execute("""INSERT INTO students(name, department) VALUES(%s, %s)""",
                (name, department))
    db.commit()


def session(session_data):
    for exam in session_data:
        cur.execute("""INSERT INTO exams(student_id, subject_id, point) VALUES (%s, %s, %s)""",
                    (exam[0], exam[1], exam[2]))
    db.commit()
    today = datetime.now().strftime('%Y-%m-%d')
    cur.execute(
        """
        CREATE TEMP TABLE bad_st AS
        SELECT student_id FROM exams 
        WHERE exam_date = %s
        GROUP BY student_id
        HAVING AVG(point) < 3.5;
        DELETE FROM exams WHERE student_id = ANY(SELECT student_id from bad_st);
        SELECT name FROM students WHERE id = ANY(SELECT student_id from exambad_st_data)
        """, (today,))
    data = cur.fetchall()


def sample():
    insert_student("Danila", "SHAD112")
    insert_student('Alexander', 'SHAD112')
    insert_student('Artemiy', 'SHAD111')
    insert_student('Ryadnov', 'SHAD112')
    insert_student('Vladimir', 'SHAD111')
    insert_student('Roman', 'SHAD111')


def get_view():
    cur.execute("""SELECT * FROM students""")
    data = cur.fetchall()
    print(list(data[0].keys()))
    for student in data:
        print(list(student.values()))


def reset_db():
    cur.execute("""DELETE FROM students""")
    db.commit()


if __name__ == "__main__":
    start_db()
    sample()
    session([
        [1, 1, 5],
        [2, 1, 4],
        [3, 1, 2],
        [4, 1, 3],
        [5, 1, 5],
        [1, 2, 4],
        [2, 2, 5],
        [3, 2, 3],
        [4, 2, 2],
        [5, 2, 3]
    ])
