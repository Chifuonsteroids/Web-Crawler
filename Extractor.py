import requests
from bs4 import BeautifulSoup
import csv

# Define the URL you want to scrape
url = 'https://www.tum.ac.ke/'  # Replace with the URL of the website you want to scrape

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define the data you want to extract (example: extracting links)
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))

    # Define the CSV file name
    csv_filename = 'extracted_data.csv'

    # Write the extracted data to a CSV file
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write header row (if needed)
        # csv_writer.writerow(['Link Text', 'Link URL'])

        # Write data rows
        for link in links:
            csv_writer.writerow([link])

    print(f'Data has been extracted and saved to {csv_filename}')
else:
    print(f'Failed to retrieve data. Status code: {response.status_code}')
