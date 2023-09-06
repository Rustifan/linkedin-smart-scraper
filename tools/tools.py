import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

def get_profile_url(text: str) -> str:
    """Searches for Linkedin Profile Page and returns a stringified list of descriptions and urls"""
    url_encoded_text = urllib.parse.quote_plus(text)
    url = f"https://google.com/search?q={url_encoded_text}"
    request = urllib.request.Request(url)
    request.add_header(
        "User-Agent",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    )
    raw_response = urllib.request.urlopen(request).read()
    html = raw_response.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    divs = soup.select("#search div.g")
    results = []
    for div in divs:
        anchor = div.select_one("a")
        if anchor is None:
           continue;
        href = anchor.get_attribute_list("href")[0]
        h3 = anchor.select_one("h3")
        title = h3.get_text() if h3 is not None else ""
        result = {"title": title, "url": href}
        results.append(result)
    
    return json.dumps(results)