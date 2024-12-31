# Quotes Scraper

This Python script is designed to scrape quotes from the website "Quotes to Scrape" (http://quotes.toscrape.com). It fetches quotes and their respective authors from the website and saves them into two formats: CSV and TXT. The script uses the `requests` library to fetch web pages, `BeautifulSoup` (from `bs4`) to parse the HTML, and the `csv` module to output data into CSV format.

## What the Script Does:

1. **Send an HTTP Request**:  
   The script sends a request to the URL `http://quotes.toscrape.com` using the `requests` library. If the website responds with a status code of 200 (OK), it proceeds with extracting data from the page.

2. **Parse the HTML Page**:  
   Once the page is successfully fetched, the script parses the HTML content using `BeautifulSoup`. This allows it to navigate and extract the quotes and authors embedded in the page.

3. **Extract Quotes and Authors**:  
   The page is structured such that each quote is contained within a `div` element with the class `quote`. Within each of these `div` elements:
   - The actual quote text is inside a `span` tag with the class `text`.
   - The author of the quote is inside a `small` tag with the class `author`.

4. **Output the Data**:  
   After extracting all the quotes and authors, the script saves the data into two different formats:
   - **CSV file (`quotes.csv`)**: Each quote and its corresponding author are written into a CSV file. The first row contains headers, and subsequent rows contain the quote text and the author's name.
   - **TXT file (`quotes.txt`)**: Each q
