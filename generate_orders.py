from faker import Faker
import pandas as pd
import random
import csv



def multiple_orders_generation(seed):
    orders_columns =  ['Order_ID','Customer_ID','Product_ID', 'Quantity', 'Delivery_Method', 'Discount', 'Payment method', 'Shipping fee'] 
    Faker.seed(seed)
    random.seed(seed)
    delivery_method = ['Courier', 'Post', 'Pickup Point', 'Pickup Locker']
    payment_methods = ['Apple_pay', 'Debit_card', 'Cash_on_delivery','Bank_transfer']
    orders_columns =  ['Order_ID','Customer_ID','Product_ID', 'Quantity', 'Delivery_Method', 'Discount', 'Payment method', 'Shipping fee', 'Timestamp', 'Time_of_completion'] 
    orders_df = pd.DataFrame(columns=orders_columns)
    rows = []
    with open('events.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Type'] == 'purchase':
                rows.append({
                    'Product_ID': row['Product_ID'],
                    'Timestamp': row['Timestamp'],
                    'Session_ID': row['Session_ID'],
                    'Customer_ID': row['User_ID']
                })

    orders_df = pd.concat([orders_df, pd.DataFrame(rows)], ignore_index=True)

    for i in range(len(orders_df)):
        order = Faker()
        order_id = order.bothify(text='????_####').upper()
        quantity = random.randint(1,10)
        delivery = order.random_element(elements=delivery_method)
        discount_chance = random.randint(1,10)
        if discount_chance>8:
            discount = random.randint(1,8)
        else:
            discount = 0
        payment_method = order.random_element(elements=payment_methods)
        shipping_fee = round(random.uniform(0, 200),2)
        time_of_completion = (str(random.randint(0,8))+' days, '+ str(random.randint(0,23))+' hours')
        
        orders_df.loc[i, 'Order_ID'] = order_id
        orders_df.loc[i, 'Quantity'] = quantity
        orders_df.loc[i, 'Delivery_Method'] = delivery
        orders_df.loc[i, 'Discount'] = discount
        orders_df.loc[i, 'Payment method'] = payment_method
        orders_df.loc[i, 'Shipping fee'] = shipping_fee
        orders_df.loc[i, 'Time_of_completion'] = time_of_completion
    
    return orders_df 
    
    
        