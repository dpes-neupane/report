import requests 
import json
import csv


def download_json():
    endpoint = requests.get('https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json')
    json_data = endpoint.json()

    data = []
    for item in range(len(json_data)):
        data.append([json_data[item]["year"], json_data[item]["petroleum_product"], json_data[item]["sale"]])

    write_file = r"data.csv"


    with open(write_file, 'w', newline= '') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(["year", "petroleum_product", "sale"])
        writer.writerows(data)
    return write_file