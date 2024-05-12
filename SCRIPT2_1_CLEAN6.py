def modify_csv(filename):

  with open(filename, 'r+') as csvfile:
    lines = csvfile.readlines() 

    for i in range(1, len(lines)):
      lines[i] = lines[i].strip().split(',')[:-1]
      lines[i] = ','.join(lines[i]) + ',0\n'  

    csvfile.seek(0)
    csvfile.writelines(lines) 


filename = 'EurostatDownloads.csv'
modify_csv(filename)

print(f"CSV modified in-place: {filename}")