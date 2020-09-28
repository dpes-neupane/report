from petroleum_report.models import *

#this function rerurns the list of the sales for the given interval of years and for the respective products
def calculator(from_year, to_year, product):
    year = YearBarsa.objects.filter(year_barsa__gte=from_year, year_barsa__lte=to_year)
    product = Product.objects.get(product=product)
    sales_list = []
    for y in year:
        sale_value = Sales.objects.get(year_sales=y.id, product_name=product.id)
        
        if sale_value.sales != 0:
            sales_list.append(sale_value.sales)
    return (sales_list) 
    
if __name__ == "__main__":
    #testing the given function in manage.py shell
    s = calculator(2000, 2004, "Mineral Turpentine Oil")
    print(s)


    
