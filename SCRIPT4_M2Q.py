import csv


def get_time_list(input_file):
  time_list = []
  with open(input_file, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header row!!
    for row in reader:
      time_period = row[0]
      time_list.append(time_period)
  return time_list


def transform_data(input_file1, input_file2, input_file3, output_file):
  data1 = {}
  countries = set()
  time_list = get_time_list(input_file2)  # Extract time list

  with open(input_file3, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip header!!!
    for row in reader:
      countries.add(row[0])

  with open(input_file1, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
      geo = row['geo']
      if geo in countries:  # Only process data for specified countries
        time_period = row['time_period']  # Capture time period 
        obs_value = float(row['obs_value'])
        key1 = row['key1']
        if geo not in data1:
          data1[geo] = {}
        data1[geo][time_period] = obs_value

  with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['geo', 'new_time_period', 'obs_value', 'key1'])
    for geo, periods in data1.items():
      for time_period in time_list:
        year, quarter = time_period.split('-')
        if quarter == 'Q1':
          # Calculate average for Q1
          q1_value = round(sum(periods[f'{year}-{m}'] for m in ['01', '02', '03']) / 3,2)
        elif quarter == 'Q2':
          # Calculate average for Q2
          q2_value = round(sum(periods[f'{year}-{m}'] for m in ['04', '05', '06']) / 3,2)
        elif quarter == 'Q3':
          # Calculate average for Q3
          q3_value = round(sum(periods[f'{year}-{m}'] for m in ['07', '08', '09']) / 3,2)
        else:
          # Calculate average for Q4
          q4_value = round(sum(periods[f'{year}-{m}'] for m in ['10', '11', '12']) / 3,2)
        writer.writerow([geo, time_period, q1_value if quarter == 'Q1' else q2_value if quarter == 'Q2' else q3_value if quarter == 'Q3' else q4_value, geo + time_period])  # Combine geo and time_period (alternative: add separate columns)


input_file1 = "xml12/2PRC_HICP_MIDX.xml_output.csv"
input_file2 = "xml12/A2Q_M2Q_DB.csv"
input_file3 = "xml12/A2Q_M2Q_COUNTRYLIST.csv"
input_file4 = "xml12/3PRC_HICP_MIDX.xml_output.csv"
output_file = "xml12/2PRC_HICP_MIDX_ANNUAL.xml_output.csv"
output_file1 = "xml12/3PRC_HICP_MIDX_ANNUAL.xml_output.csv"

transform_data(input_file1, input_file2, input_file3, output_file)
transform_data(input_file4, input_file2, input_file3, output_file1)
