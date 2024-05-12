import csv
import requests
import sys
from xml.etree import ElementTree as ET
from datetime import datetime

def parse_xml(link):
    response = requests.get(link)
    xml_data = response.content
    
    root = ET.fromstring(xml_data)
    namespaces = {'m': 'http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message'}
    header = root.find(".//m:Header", namespaces=namespaces)
    if header is not None:
        prepared_n = header.find("./m:Prepared", namespaces=namespaces).text
        
        # Transform Prepared_n to Time Parameter
        prepared_n_time = datetime.strptime(prepared_n, "%Y-%m-%dT%H:%M:%S.%fZ")
        return prepared_n_time
    else:
        print("Prepared_n element not found in the XML document.")
        return None

def update_csv(filename):

    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        rows = list(csv_reader)
        
        for row in rows:
            prepared_c = row['m.Prepared_c']
            Link = row['Link']
            link_parts = ['https://ec.europa.eu/eurostat/api/dissemination/sdmx/3.0/structure/dataflow/ESTAT/',
                                                         Link,
                                                         '/1.0?compress=false']
            link = ''.join(link_parts)
            
            # Parse XML and get Prepared_n time parameter
            prepared_n_time = parse_xml(link)

            # Compare Prepared_n with m.Prepared_c
            if not prepared_c or prepared_n_time > datetime.strptime(prepared_c, "%Y-%m-%dT%H:%M:%S.%fZ"):
            # Update data
                row['m.Prepared_c'] = prepared_n_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                row['Download'] = '1'
 
    # Write back to the CSV file
        with open(filename, 'w', newline='') as file:
           fieldnames = ['Row','Variable','Link','Measure','m.Prepared_c','Download']
           writer = csv.DictWriter(file, fieldnames=fieldnames)
           writer.writeheader()
           
           writer.writerows(rows)
    return None

def update_check(filename):
  updates = 0
  with open(filename, 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
      updates += int(row['Download'])  # Convert Download to int directly

  print(updates)
  if updates > 0:
    return True
  else:
    return Falst


filename = 'EurostatDownloads.csv'
update_csv(filename)
result = update_check(filename)

print(result)
if result:
    sys.exit(0)
else:
    sys.exit(1)