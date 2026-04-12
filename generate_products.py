from faker import Faker
import pandas as pd
import random


#Used brands: 'Apple', 'Samsung', 'Sony', 'Lenovo', 'Xiaomi','Huawei', 'ASUS', 'Braun'

def choose_prod_name(category, product):
    
    if category == 'Music':
        product_brand = product.random_element(['Apple', 'Samsung', 'Sony', 'Xiaomi'])
        product_name = product.random_element(['Headphones', 'Speaker']) + " " + product_brand + " " + product.bothify(text='???####').upper()
    elif category == 'TV & Displays':
        product_brand = product.random_element(['Samsung', 'Sony', 'ASUS'])
        product_name = product.random_element(['TV', 'Display']) + " " + product_brand + " " + product.bothify(text='??###').upper()
    elif category == 'Smartphones':
        product_brand = product.random_element(['Samsung', 'Sony', 'Apple', 'Xiaomi','Huawei'])
        product_name =  "Smartphone " + product_brand + " " + product.bothify(text='????##').upper()
    elif category == 'Laptops':
        product_brand = product.random_element(['Apple', 'Xiaomi','Lenovo', 'ASUS'])
        product_name =  "Laptop " + product_brand + " " + product.bothify(text='???###').upper()
    elif category == 'Tablets':
        product_brand = product.random_element(['Apple', 'Xiaomi','Lenovo', 'Huawei', 'Samsung'])
        product_name =  "Tablet " + product_brand + " " + product.bothify(text='?##??').upper()
    elif category == 'Kitchen':
        product_brand = product.random_element(['Braun', 'Xiaomi'])
        product_name =  product.random_element(['Kettle', 'Air Fryer', 'Cooker', 'Fridge']) + " " + product_brand + " " + product.bothify(text='??###?').upper()
    elif category == 'Cameras':
        product_brand = product.random_element(['Samsung', 'Sony'])
        product_name = "Camera " + product_brand + " " + product.bothify(text='?##??').upper()
    elif category == 'Consoles':
        product_brand = product.random_element(['Sony', 'ASUS'])
        product_name = "Console " + product_brand + " " + product.bothify(text='?#?#??').upper()
    return product_brand, product_name


def one_product_generation(product):
    categories_list = ['Music', 'TV & Displays', 'Smartphones', 'Laptops', 'Tablets', 'Kitchen', 'Cameras', 'Consoles']

    product_id = product.bothify(text='??########??').upper()
    product_category = product.random_element(categories_list)
    product_price =  round(random.uniform(500, 2000), 2)
    product_cost = round(random.uniform(100, 500), 2)
    product_rating = round(random.uniform(1, 4.9), 1)
    product_brand, product_name = choose_prod_name(product_category, product)
    
    product_instance = {
        'Product_ID': product_id, 
        'Name': product_name, 
        'Category': product_category,
        'Brand': product_brand, 
        'Price': product_price,
        'Cost': product_cost, 
        'Rating': product_rating
    }
    return product_instance

def multiple_products_generation(num_products, seed):
    products_columns = ['Product_ID', 'Name', 'Category', 'Brand', 'Price', 'Cost', 'Rating']
    Faker.seed(seed)
    random.seed(seed)
    product_df = pd.DataFrame(columns = products_columns)

    for i in range(num_products):
        product = Faker()
        product_df.loc[i] = one_product_generation(product)
    product_df.to_csv('products.csv',header=True,columns=["Product_ID"], index= False)
    return product_df

    
