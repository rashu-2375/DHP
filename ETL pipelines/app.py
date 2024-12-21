# import schedule
from flask import Flask, render_template
import psycopg2
import psutil
from datetime import datetime
import time

app = Flask(__name__)from flask import Flask, render_template
import psycopg2
import psutil
from datetime import datetime
import time

app = Flask(__name__)

# Database configuration
DB_CONFIG = {
    "dbname": "ETL2024",
    "user": "postgres",
    "password": "2375rash",
    "host": "localhost"
}

def extract_cpu_usage():
    return psutil.cpu_percent(interval=1)

def extract_ram_usage():
    return psutil.virtual_memory().percent

def transform_data(data):
    # Manipulate data if needed
    # For demonstration, let's add 10% to the RAM usage
    return data + 10

def load_data(cpu_usage, ram_usage, connection):
    try:
        with connection.cursor() as cursor:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            insert_query = "INSERT INTO performance_metrics (timestamp, cpu_usage, ram_usage) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (timestamp, cpu_usage, ram_usage))
            connection.commit()
            print("Data inserted successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

def fetch_data(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM performance_metrics ORDER BY timestamp DESC LIMIT 10")
            data = cursor.fetchall()
            return data
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
        return []

@app.route('/')
def index():
    with psycopg2.connect(**DB_CONFIG) as connection:
        data = fetch_data(connection)
    return render_template('index.html', data=data)

def etl_job():
    cpu_usage = extract_cpu_usage()
    ram_usage = extract_ram_usage()
    ram_usage = transform_data(ram_usage)
    with psycopg2.connect(**DB_CONFIG) as connection:
        load_data(cpu_usage, ram_usage, connection)

def main():
    while True:
        etl_job()
        time.sleep(60)  # Sleep for 60 seconds (1 minute)

if __name__ == "__main__":
    main()


def extract_cpu_usage():
    return psutil.cpu_percent(interval=1)

def extract_ram_usage():
    return psutil.virtual_memory().percent

def transform_data(data):
    # Manipulate data if needed
    # For demonstration, let's add 10% to the RAM usage
    return data + 10

def load_data(cpu_usage, ram_usage):
    try:
        connection = psycopg2.connect(
        dbname="ETL2024",
        user="postgres",
        password="2375rash",
        host="localhost"
        )
        cur = connection.cursor()


        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        insert_query = "INSERT INTO performance_metrics (timestamp, cpu_usage, ram_usage) VALUES (%s, %s, %s)"

        cur.execute(insert_query, (timestamp, cpu_usage, ram_usage))

        connection.commit()
        print("Data inserted successfully!")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if connection:
            cur.close()
            connection.close()

@app.route('/')
def index():

    
    
def etl_job():
    cpu_usage = extract_cpu_usage()
    ram_usage = extract_ram_usage()
    ram_usage = transform_data(ram_usage)
    load_data(cpu_usage, ram_usage)

def main():
    while True:
        etl_job()
        time.sleep(60)  # Sleep for 60 seconds (1 minute)
    

if __name__ == "__main__":
    main()