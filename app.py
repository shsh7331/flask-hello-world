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
