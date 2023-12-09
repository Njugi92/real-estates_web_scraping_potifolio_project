import os
import pandas as pd
from bs4 import BeautifulSoup as beauty
import requests

def scrape_milikispace():
    csv_data_path = "csv_data"
    if not os.path.exists(csv_data_path):
        os.makedirs(csv_data_path)

    url = "https://milikispace.co.ke/projects/"
    all_urls = []

    for page in range(1, 20):
        next_urls = url + str(page)
        all_urls.append(next_urls)

    scraped_data = []  # Store scraped data

    for url in all_urls:
        render = requests.get(url)
        the_html = beauty(render.content, "html.parser")

        scrape = the_html.find_all(class_="title")

        for data in scrape:
            scraped_data.append(data.get_text().strip())  # Append cleaned text to the list

    # Create DataFrame from the scraped data list
    data_2_csv = pd.DataFrame({"column": scraped_data})

    csv_filename = os.path.join("csv_data", "milikispace.csv")  # Define the path to save the CSV file
    data_2_csv.to_csv(csv_filename, index=False)

    #return data_2_csv

if __name__ == "__main__":
    result = scrape_milikispace()
    #print(result)

