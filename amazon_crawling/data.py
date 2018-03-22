import requests
import csv
import time

url = ["https://www.amazon.co.jp/exec/obidos/ASIN/B00027LF7S", "https://www.amazon.co.jp/exec/obidos/ASIN/B073VM9RXL", "https://www.amazon.co.jp/exec/obidos/ASIN/B073VMQN5S", "https://www.amazon.co.jp/exec/obidos/ASIN/B01BSTSN2I"]


output_file = open("data.csv", "w", encoding="utf-8")
writer = csv.writer(output_file, lineterminator='\n')

for ur in url:
    time.sleep(1)
    response = requests.get(ur)
    writer.writerow([ur, response.text])

output_file.close()
