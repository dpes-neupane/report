#script to run to add data to the database in written in sqllite3

#all the addition is done using the api of django and kept clear as possible 

import os
from petroleum_report.models import *
import datetime
path = r"E:\college\projex\data\data.csv"
import requests
import csv



def add_year_product(file_pointer): 
        reader = file_pointer
        for row in reader:
            y = row["year"]
            z = row["petroleum_product"]
            
            try:
               YearBarsa.objects.get(year_barsa=y) 
               print(f"The year {y} was a duplicate") 
               
               
            except:
                p = YearBarsa(year_barsa=y)
                
                p.save()
                
                print(f"The year {y} is added")

            if len(Product.objects.filter(product=z)) == 0:
                q = Product(product=z)
                q.save()
                print(f"The product {z} is added")
            else:
                print(f"The {z} was already added")



def add_sales(file_pointer):
    reader = file_pointer
    for row in reader:
        y = row["year"]
        p = row["petroleum_product"]
        s = row["sale"]
        
        year = YearBarsa.objects.get(year_barsa=y)
        
        produ = Product.objects.get(product=p)
        
        try:
            sales = Sales(year_sales=year, product_name=produ, sales=s)
            sales.save()
            print(f"{s} added!")
        except :
            print(f"\n{s} not added!\n")

if __name__ == "__main__":#had to run through manage.py shell to add the data
    with open('data.csv', newline='') as fp:
        reader = csv.DictReader(fp)
        add_year_product(reader)
        add_sales(reader)

