import os
import pandas as pd
from bs4 import BeautifulSoup as beauty
import requests

url = "https://milikispace.co.ke/projects/"
all_urls = []

for page in range(1,2):
    next_urls = url + str(page)
    all_urls.append(next_urls)

for url in all_urls:
    render = requests.get(url)
    the_html = beauty(render.content, "html.parser")
    #print(the_html)

    scrape = the_html.find_all(class_ = "title")
    #print(scrape)
    
    scraped_data = []
    for data in scrape:
        scraped_data.append(data.get_text())
        #print(data.get_text())
    #print(scraped_data)    
    cleaned_data = [data.replace("\n", "") for data in scraped_data]
    cleaned_data2 = [data.replace("\t", "") for data in cleaned_data]
    
    #print(cleaned_data2)
    clean_data_ = [data.replace("\r", "") for data in cleaned_data2]
    clean_data_2 = [data.replace("       ", "") for data in clean_data_]
    #print(clean_data_)

    data_2_csv = pd.DataFrame(clean_data_2, columns=["column"])
    data_2_csv.to_csv("milikispace.csv", mode="a", index=False)
    print(data_2_csv)

    
