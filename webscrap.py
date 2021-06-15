#Project 2 :
#web Scraping using BeautifulSoup
import requests
from bs4 import BeautifulSoup
import pandas

flipkart_url = "https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_4_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_4_0_na_na_na&as-pos=4&as-type=TRENDING&suggestionId=laptops&requestId=77ece9fc-03ad-4eae-964c-fbe432575db8/&page="

page_num_max = 5
scraped_info_list = []
for page_num in range(1, page_num_max):
    #flipkart_url = "https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_4_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_4_0_na_na_na&as-pos=4&as-type=TRENDING&suggestionId=laptops&requestId=77ece9fc-03ad-4eae-964c-fbe432575db8/&page="

    req = requests.get(flipkart_url  + str(page_num))
    content = req.content

    soup = BeautifulSoup(content, "html.parser")

    all_flipkart = soup.find_all("div", {"class": "_13oc-S"})

    for laptop in all_flipkart:
        laptop_dict = {}
        laptop_dict["name"] = laptop.find("div", {"class": "_4rR01T"}).text
        laptop_dict["address"] = laptop.find("ul", {"class": "_1xgFaf"}).text
        laptop_dict["prize"] = laptop.find("div", {"class": "_30jeq3 _1_WHN1"}).text

        try:

            laptop_dict["offers"] = laptop.find("div", {"class": "_3Ay6Sb"}).text
            laptop_dict["rating"] = laptop.find("div", {"class": "_3LWZlK"}).text
            laptop_dict["rating_and_review"] = laptop.find("span", {"class": "_2_R_DZ"} ).text
        except AttributeError:
            pass
        scraped_info_list.append(laptop_dict)
    print(flipkart_url)
            #print(restaurant_name, restaurant_items, restuarant_offers)
dataFrame = pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("Flipkart.csv")
