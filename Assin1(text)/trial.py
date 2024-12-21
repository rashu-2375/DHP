import requests
from bs4 import BeautifulSoup
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
    
link = 'https://indianexpress.com/article/india/telangana-phone-tapping-case-congress-bjp-brs-9234722/'
a = get_html_content(link)
# print(a)

def extract_title(content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    # Find the title tag
    title_tag = soup.find('title')
    # Return the text inside the title tag
    return title_tag.text if title_tag else None

print(extract_title(a))

def extract_body(content):
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    elements_with_class = soup.find_all(class_='story_details')
    # Extract the text content from the elements and concatenate them
    extracted_content = ' '.join(element.get_text(strip=True) for element in elements_with_class)
    return extracted_content.strip() if extracted_content else None
print(extract_body(a))







