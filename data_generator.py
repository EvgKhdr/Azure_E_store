from  generate_customers import multiple_customers_generation
from  generate_products import multiple_products_generation
from  generate_events import multiple_events_generation
from  generate_orders import multiple_orders_generation
from datetime import datetime
from dotenv import load_dotenv
import io
import os
import pandas as pd
import time
from azure.storage.blob import BlobServiceClient


#configurations
load_dotenv()
start_signup_date = datetime.strptime("2023-01-01", '%Y-%m-%d') # start date from which customer accounts are registered 
end_signup_date = datetime.strptime("2025-01-01", '%Y-%m-%d') # end date of customer's accounts registration
countries = ['de_DE', 'pl_PL', 'cs_CZ']
today_date = datetime.today().strftime('%Y/%m/%d')
connection_string = os.getenv("AZURE_CONNECTION_STRING")
container_name = "raw"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)
starting_seed = 125
NUMBER_OF_CUSTOMERS = 200
NUMBER_OF_PRODUCTS = 50
NUMBER_OF_EVENTS = 2000
sleep_time = 30 #in seconds, delay between batches upload
NUMBER_OF_BATCHES = 10 # how many batches will be uploaded into the Azure storage
seeds_list = list(range(starting_seed, starting_seed+NUMBER_OF_BATCHES))

def upload_to_azure(name, config, SEED):
    buffer = io.BytesIO()
    config['df'].to_csv(buffer, index=False)
    buffer.seek(0)
    blob_name = f"{config['path']}{name}_raw_{SEED}.csv"
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    try:
        blob_client.upload_blob(buffer, overwrite=True)
        print(f"ok, Uploaded {name} with seed {SEED}")
    except Exception as e:
        print(f"Failed to upload {name}: {e} with seed {SEED}")


def upload_customers_products(NUMBER_OF_CUSTOMERS,NUMBER_OF_PRODUCTS,SEED):
    customers_df = multiple_customers_generation(NUMBER_OF_CUSTOMERS,SEED,start_signup_date, end_signup_date, countries)
    products_df = multiple_products_generation(NUMBER_OF_PRODUCTS,SEED)
    customers_products_dict = {
        "customers": {"df": customers_df, "path": "customers/"+today_date+"/"},
        "products": {"df": products_df, "path": "products/"+today_date+"/"},
    }
    for name, config in customers_products_dict.items():
        upload_to_azure(name, config, SEED)

def upload_events_orders(NUMBER_OF_EVENTS,SEED ):
    events_df = multiple_events_generation(NUMBER_OF_EVENTS,SEED)
    orders_df = multiple_orders_generation(SEED)

    events_orders_dict = {
        "events": {"df": events_df, "path": "events/"+today_date+"/"},
        "orders": {"df": orders_df, "path": "orders/"+today_date+"/"}
    }
    for name, config in events_orders_dict.items():
        upload_to_azure(name, config, SEED)
        
    
    
def main_upload():
    for seed in seeds_list:
        if seed == seeds_list[0]:
            upload_customers_products(NUMBER_OF_CUSTOMERS,NUMBER_OF_PRODUCTS,seed)
        upload_events_orders(NUMBER_OF_EVENTS,seed)
        time.sleep(sleep_time)
    print("Final upload completed")

if __name__=="__main__":
    main_upload()

   
   
