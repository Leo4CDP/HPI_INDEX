import requests
import os
import csv

download_folder = "xml12"
print(download_folder)

# Function to check internet connection
# def check_internet():
#  try:
#    response = requests.get("https://ec.europa.eu/")
#    response.raise_for_status()  # Raise exception for non-2xx status codes
#    return True
#  except requests.exceptions.RequestException:
#    return False


def download_file(rowN,link,c_measure):
  url = f"https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/data/dataflow/ESTAT/{link}/1.0/{c_measure}?c[TIME_PERIOD]=ge:2010&compress=false"
  print(url)
#  try:
  response = requests.get(url)
  response.raise_for_status()
  print(response)
  
  # Create download folder if it doesn't exist
  os.makedirs(download_folder, exist_ok=True)

  filename = os.path.basename(rowN+link+".xml")  # Extract filename from link
  filepath = os.path.join(download_folder, filename)

  with open(filepath, "wb") as f:
    f.write(response.content)

    print(f"Downloaded: {filename}")

#  except requests.exceptions.RequestException:
#    print(f"Error downloading: {link}")

downloaded_count = 0

with open("EurostatDownloads.csv", "r+") as csvfile:
  # Read all lines into memory (not ideal for large files)
  lines = csvfile.readlines()
  header = lines[0].strip().split(",")
  writer = csv.writer(csvfile)

  for i, row in enumerate(lines[1:]):
    rowN, variable, link, c_measure, prepared_date, download_flag = row.strip().split(",")
    download_flag = int(download_flag)

    if download_flag == 1:
        download_file(rowN,link,c_measure)
        downloaded_count += 1
      
# Print final output message
if downloaded_count > 0:
  print(f"{downloaded_count} files downloaded.")
else:
  print("Error, some files were not downloaded")