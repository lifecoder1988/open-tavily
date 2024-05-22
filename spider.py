import requests
from bs4 import BeautifulSoup

import json


def crawl(url: str) -> str:
    """
    Fetches HTML data from the given URL, parses it using BeautifulSoup, and extracts text content.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        str: A JSON string containing either the extracted text or an error message.

    Example:
        url = "https://example.com"
        result = crew(url)
        print(result)
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Check if the request was successful
        if response.status_code == 200:
            html_content = response.text
            # Create a BeautifulSoup object and parse the HTML
            soup = BeautifulSoup(html_content, "html.parser")
            # Remove script and style elements
            for script_or_style in soup(["script", "style"]):
                script_or_style.decompose()
            # Get text and remove leading/trailing whitespace
            text = soup.get_text()
            # Condense all whitespace to one space for better readability
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = "\n".join(chunk for chunk in chunks if chunk)
            return text
        else:
            return "Failed to retrieve content."
    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        return json.dumps({"error": f"Request error: {str(e)}"})
    except Exception as e:
        # Handle any other parsing-related errors
        return json.dumps({"error": f"Parsing error: {str(e)}"})


# Example usage
if __name__ == "__main__":
    url = "https://baike.baidu.com/item/%E5%BC%A0%E7%A3%8A/8864724"
    result = crawl(url)
    print(result)
