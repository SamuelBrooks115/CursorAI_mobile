import requests
from bs4 import BeautifulSoup


def scrape_page(url: str) -> str:
    """Fetch the url and return plain text content."""
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    # Get the textual content of the page
    return soup.get_text(separator='\n', strip=True)


def main():
    url = "https://quotes.toscrape.com/"  # Example site for scraping
    content = scrape_page(url)
    print(content)


if __name__ == "__main__":
    main()
