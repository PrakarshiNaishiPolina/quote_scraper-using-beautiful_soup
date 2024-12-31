import requests
from bs4 import BeautifulSoup
import csv

url="http://quotes.toscrape.com"
response=requests.get(url)

if response.status_code ==200:

    soup=BeautifulSoup(response.text,"html.parser")

    quotes=soup.find_all("div",class_="quote")

    for quote in quotes:
        text=quote.find("span",class_="text").get_text()
        author=quote.find("small",class_="author").get_text()
        print(f"Quote:{text}\nAuthor:{author}\n")
    

    with open("quotes.csv",mode="w",newline="",encoding="utf-8") as file:

        writer=csv.writer(file)

        # write header row
        writer.writerow(["Quote","Author"])
        
        for quote in quotes:
            # extract the quote text

            text=quote.find("span",class_="text").get_text()

            # extract the author name

            author=quote.find("small",class_="author").get_text()

            writer.writerow([text,author])
    
    print("Quotes have been written to 'quotes.csv'. ")

    with open("quotes.txt",mode="w",encoding="utf-8") as file:

        for quote in quotes:

            text=quote.find("span",class_="text").get_text()

            author=quote.find("small",class_="author").get_text()

            file.write(f"Quote: {text}\n Author:{author}\n")
    
    print("Quotes have been written to 'quotes.txt'.")


           



