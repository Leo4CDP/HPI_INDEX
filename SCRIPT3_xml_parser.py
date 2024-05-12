import csv
from lxml import etree
import os

def extract_data(file_path):
    tree = etree.parse(file_path)
    root = tree.getroot()

    analysed_xml_filename = file_path.split('/')[-1]
    extracted = root.find(".//m:Extracted", namespaces=root.nsmap).text
    structure_ref = root.find(".//m:Structure", namespaces=root.nsmap).get("structureID")


    version_data = [analysed_xml_filename, extracted, structure_ref]

    data_rows = []
    for series in root.findall(".//Series", namespaces=root.nsmap):
        freq = series.get("freq")
        geo = series.get("geo")
        hhtyp = series.get("hhtyp")
        indic_is = series.get("indic_is")
        unit = series.get("unit")

        for obs in series.findall("Obs", namespaces=root.nsmap):
            time_period = obs.get("TIME_PERIOD")
            obs_value = obs.get("OBS_VALUE")
            key1 = geo+time_period

            data_rows.append([freq, geo, hhtyp, indic_is, unit, time_period, obs_value, key1])

    return version_data, data_rows

def save_to_csv(file_path, version_data, data_rows):
    with open(f"version.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(version_data)

    with open(f"{file_path}_output.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["freq", "geo", "hhtyp", "indic_is", "unit", "time_period", "obs_value", "key1"])
        writer.writerows(data_rows)
    print("{file_path}_output.csv")

# Usage
#file_path = "download/example.xml"
#version_data, data_rows = extract_data(file_path)
#save_to_csv(file_path, version_data, data_rows)

folder_path = "xml12/"
for file in os.listdir(folder_path):
    if file.endswith(".xml"):
        file_path = os.path.join(folder_path, file)
        version_data, data_rows = extract_data(file_path)
        if version_data and data_rows:
            save_to_csv(file_path, version_data, data_rows)