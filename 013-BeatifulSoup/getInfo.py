import datetime
import requests
from bs4 import BeautifulSoup
import re

def file_already_exists(filename):
    """Check if the file already exists"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            # should not be empty
            if file.read() == "":
                return False
            return True
    except FileNotFoundError:
        return False


def get_site_info(itemLink):
    """Get the content of a site and save it in a file"""
    id = itemLink["_id"]
    url = itemLink["url"]
    name = itemLink["name"]
    filename = id + ".html"
    # check if the file already exists
    if not file_already_exists(filename):
        print(f"\n\nScraping {url}")
        # get the content of the site
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        # save the content of the site in a file with the same url name
        with open(id + ".html", "w", encoding="utf-8") as file:
            file.write(soup.get_text())
    soup = scrap_site_info(id)
    if name == "kabum":
        read_from_kabum(soup)
    elif name == "amazon":
        read_from_amazon(soup)


def scrap_site_info(id):
    """Get the content of a site"""
    filename = id + ".html"
    try:
        with open(filename, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file.read(), "html.parser")
            return soup
    except FileNotFoundError:
        return None


def remove_spaces(text):
    text_without_lines = text.replace("\n", "").strip()
    return " ".join(text_without_lines.split())


def read_from_kabum(soup):
    try:
        print("\nReading from Kabum")
        # get the title
        title = soup.find("h1").text
        # get the og:image
        og_image = soup.find("meta", property="og:image")["content"]
        print(og_image)
        # get the price
        finalPrice = soup.find(class_="finalPrice").text
        regularPrice = soup.find(class_="regularPrice").text
        cardParcels = soup.find(class_="cardParcels").text
        # get the date
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        cardParcels = remove_spaces(cardParcels)

        print(f"Title: {title.strip()}")
        print(f"Final Price: {finalPrice.strip()}")
        print(f"Regular Price: {regularPrice.strip()}")
        print(f"Card Parcels: {cardParcels}")
        print(f"Date: {date}")

    except AttributeError as e:
        print("\nError reading from Kabum: ", e)
        return None


def read_from_amazon(soup):
    try:
        print("\nReading from Amazon")
        # get the title
        title = soup.find(id="productTitle").text
        # get the corePriceDisplay
        # corePrice = soup.find_all(string=re.compile("corePriceDisplay"))
        # print("\n CORE PRICE", corePrice)
        finalPrice = soup.find(class_="a-price-symbol").text
        finalPrice += soup.find(class_="a-price-whole").text
        finalPrice += soup.find(class_="a-price-fraction").text
        # regularPrice = soup.find(class_=["best-offer-name a-text-bold"])
        # print(regularPrice)
        # regularPrice = re.compile("$(.*)").search(regularPrice).group(1)
        # cardParcels = soup.find(class_="best-offer-name").text
        # cardParcels = re.compile("ou R$ .*").search(cardParcels).group(1)
        # get the date
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        title = remove_spaces(title)
        finalPrice = remove_spaces(finalPrice)
        # cardParcels = remove_spaces(cardParcels)

        print(f"Title: {title}")
        print(f"Final Price: {finalPrice}")
        # print(f"Regular Price: {regularPrice.strip()}")
        # print(f"Card Parcels: {cardParcels}")
        print(f"Date: {date}")

    except AttributeError as e:
        print("\nError reading from Amazon: ", e)
        return None
