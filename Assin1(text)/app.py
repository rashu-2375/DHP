from flask import Flask,redirect, render_template, request, url_for
from bs4 import BeautifulSoup
import requests
import psycopg2
import nltk

app = Flask(__name__)

conn = psycopg2.connect(host = 'localhost', user = 'postgres', dbname = 'DHP2024', password = '2375rash')
cur = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

def create_table():
    # SQL command to create a table
    create_table_command = '''
        CREATE TABLE IF NOT EXISTS News_Articles (
            id SERIAL PRIMARY KEY,
            URL text, 
            Title text,
            words_count int,
            sentences_cout int,
            POS_tag_count text

        )
    '''

    # Execute the SQL command
    cur.execute(create_table_command)
    # Commit the transaction
    conn.commit()

    # Close the cursor and connection
    cur.close()
    conn.close()



##################Extract news and cleaning part#################

    

def get_html_content(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to fetch HTML content from {url}. Status code: {response.status_code}")
            return None
    except requests.RequestException as e: 
        print(f"An error occurred while fetching HTML content from {url}: {e}")
        return None


def extract_title(content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    # Find the title tag
    title_tag = soup.find('title')
    # Return the text inside the title tag
    return title_tag.text if title_tag else None


def extract_body(content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    # Find the body tag
    body_tag = soup.find('body')
    # Return the text inside the body tag
    return body_tag.text if body_tag else None


if __name__ == '__main__':
    app.run(debug = True)