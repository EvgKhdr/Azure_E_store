from faker import Faker
import pandas as pd
import random
import datetime
from datetime import timedelta
import csv



medium = ['App', 'Chrome', 'Edge', 'Firefox', 'Safari']

def generate_event_sequence(event, products_id, customers_id):
    rows = []

    event_type = 'click'
    event_id = event.bothify(text='??_########__').upper()
    event_product = event.random_element(products_id)
    event_user = event.random_element(customers_id)
    event_medium = event.random_element(medium)
    event_time = event.date_time_between(start_date=datetime.datetime(2025, 1, 1))
    event_session = event.bothify(text='????-####-####').upper()
    click_id = event_id+"00"
    rows.append([click_id, event_type, event_product, event_time, event_session, event_medium, event_user])

    chance_sequence = random.randint(1, 10)

    if chance_sequence > 6:
        add_time = event.date_time_between(start_date=event_time + timedelta(seconds=2), end_date=event_time + timedelta(hours=1))
        add_id = event_id+"01"
        rows.append([add_id, 'add_to_cart', event_product, add_time, event_session, event_medium, event_user])

    if chance_sequence > 8:
        checkout_id = event_id+"02"
        checkout_time = event.date_time_between(start_date=add_time + timedelta(seconds=2), end_date=add_time + timedelta(hours=2))
        rows.append([checkout_id, 'checkout', event_product, checkout_time, event_session, event_medium, event_user])

    if chance_sequence > 9:
        purchase_id = event_id +"03"
        purchase_time = event.date_time_between(start_date=checkout_time + timedelta(seconds=2), end_date=checkout_time + timedelta(minutes=10))
        rows.append([purchase_id, 'purchase', event_product, purchase_time, event_session, event_medium, event_user])

    return rows

def multiple_events_generation(num_events_seq, seed):
    events_columns =  ['Event_ID','Type','Product_ID', 'Timestamp', 'Session_ID', 'Medium', 'User_ID'] 
    products_id = []
    customers_id = []
    with open('products.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products_id.append(row['Product_ID'])

    with open('customers.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers_id.append(row['Customer_ID'])

    Faker.seed(seed)
    random.seed(seed)
    event = Faker()

    all_rows = []
    for i in range(num_events_seq):
        all_rows.extend(generate_event_sequence(event,products_id, customers_id)) 

    events_df = pd.DataFrame(all_rows, columns=events_columns)  

    events_df.to_csv('events.csv', header=True, columns=['Product_ID', 'Timestamp', 'Session_ID', 'User_ID', 'Type'], index=False)
    return events_df