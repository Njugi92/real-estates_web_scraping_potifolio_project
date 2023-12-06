Web scraping portifolio project

The projects aims at visiting milikispace website where the lands for sale are uploaded. We scrap the data to see the list of lands for sale contry wide.
- To archive this we have to set up the environment:
	- Ensure you have Python installed on your system.
	- Install the necessary Python libraries like Flask, pandas, requests, and BeautifulSoup if you haven't already. You can install them using pip:
	pip install Flask pandas requests beautifulsoup4
- Run Flask App:
	- Open a terminal or command prompt in the directory where your manage.py file is located
	- Run the Flask app using the following command:
	python manage.py

- Access the appliccation:
	- Once the Flask app is running, it will start a local server.
	- Open a web browser and navigate to http://127.0.0.1:5000/ or http://localhost:5000/. This is where your Flask app is hosted.
	- You should see the results of the scraped data rendered on the webpage according to the milikispace.html template.

- Check the csv:
	- The data scraped from the website should be saved to a CSV file named milikispace.csv in the same directory as your manage.py file.
