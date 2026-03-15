import requests
from bs4 import BeautifulSoup

def parse_product_data(html_content):
    """
    Example parsing function. 
    In a real-world scenario, this logic can be generated or optimized by AI 
    based on the specific HTML structure of the target site.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # We use generic selectors for this tutorial example
    # In a live project, these would be specific CSS classes or IDs
    try:
        name = soup.find('h1').text.strip()
        price = soup.find('span', class_='price-value').text.strip()
        return {
            "product_name": name,
            "price": price,
            "status": "success"
        }
    except AttributeError:
        return {"error": "Could not find elements. Check if the selectors are correct."}

def run_scraper():
    # Replace 'YOUR_ZENROWS_API_KEY' with your actual key from the ZenRows dashboard
    API_KEY = 'YOUR_ZENROWS_API_KEY'
    TARGET_URL = 'https://www.example.com/product' # Example target

    # ZenRows parameters:
    # 'js_render': True - to handle sites built with React/Angular/Vue
    # 'premium_proxy': True - to use high-quality residential proxies and avoid blocks
    params = {
        'url': TARGET_URL,
        'apikey': API_KEY,
        'js_render': 'true',
        'premium_proxy': 'true',
    }

    print(f"Connecting to ZenRows API to fetch: {TARGET_URL}...")
    
    try:
        response = requests.get('https://api.zenrows.com/v1/', params=params)
        
        if response.status_code == 200:
            print("Successfully fetched the page!")
            data = parse_product_data(response.text)
            print("Extracted Data:", data)
        else:
            print(f"Failed to fetch page. Status Code: {response.status_code}")
            print("Response:", response.text)
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_scraper()
