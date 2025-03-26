import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from shrey shah in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://flask_hello_world_db_ji9s_user:Qo42UGQJsv9sPlbtQQ5VmvohgpAaKfw6@dpg-cvhmc1qqgecs73d26aag-a/flask_hello_world_db_ji9s")
    conn.close()
    return 'Database connection successful - shsh7331'

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgresql://flask_hello_world_db_ji9s_user:Qo42UGQJsv9sPlbtQQ5VmvohgpAaKfw6@dpg-cvhmc1qqgecs73d26aag-a/flask_hello_world_db_ji9s")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
    ''')
    conn.commit()
    conn.close()
    return 'Basketball table successfully created - shsh7331'

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgresql://flask_hello_world_db_ji9s_user:Qo42UGQJsv9sPlbtQQ5VmvohgpAaKfw6@dpg-cvhmc1qqgecs73d26aag-a/flask_hello_world_db_ji9s")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
    Values
    ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
    ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
    ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
    ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Populated - shsh7331'

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect("postgresql://flask_hello_world_db_ji9s_user:Qo42UGQJsv9sPlbtQQ5VmvohgpAaKfw6@dpg-cvhmc1qqgecs73d26aag-a/flask_hello_world_db_ji9s")
    cur = conn.cursor()
    cur.execute('''
    SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info)
        resonse_string+="</tr>"
    response_string+="</tables>"
    return response_string


@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgresql://flask_hello_world_db_ji9s_user:Qo42UGQJsv9sPlbtQQ5VmvohgpAaKfw6@dpg-cvhmc1qqgecs73d26aag-a/flask_hello_world_db_ji9s")
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE Basketball;;
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Dropped - shsh7331'