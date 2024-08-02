import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage containing the list
url = 'https://hfr.health.gov.ng/facilities/hospitals-search?_token=H9TbDwQ8hbeymByDbFIrmH5nVnBRUKgChZaUi1Rh&state_id=1&lga_id=1&ward_id=0&facility_level_id=2&ownership_id=0&operational_status_id=1&registration_status_id=2&license_status_id=1&geo_codes=0&service_type=0&service_category_id=0&facility_name=&entries_per_page=500'

# Send a GET request to fetch the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# List to store the extracted data
hospitals = []

# Example: Extracting data from table rows (change according to your page structure)
for row in soup.find_all('tr'):
    cols = row.find_all('td')
    if len(cols) > 1:  # Check if it is a data row
        hospital = {
            'State': cols[0].text.strip(),
            'LGA': cols[1].text.strip(),
            'Ward': cols[2].text.strip(),
            'Facility Name': cols[3].text.strip(),
            'Level': cols[4].text.strip(),
            'Ownership': cols[5].text.strip()
        }
        hospitals.append(hospital)

# Convert the list to a DataFrame
df = pd.DataFrame(hospitals)

# Save the DataFrame to a CSV file
df.to_csv('nigeria_hospitals.csv', index=False)
