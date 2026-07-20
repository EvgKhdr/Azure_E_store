## Description
This project is created in order to support operations of imaginary electronics store.
All data is generated with the help of Faker library and Python random module.

Electronics store has a lot of different data related to its customers, products and orders.
Management wants to store this data efficiently for which cloud solution seems appropriate.
Moreover, they expect store expansion in the nearest future and want the solution to be scalable.
To formulate their future strategy management wants to obtain business insights from the data, that is why structure of 
storage needs to support future analysis.

## Data 
1) Clients' data includes period from 2023 to 2025. Store has basic customers' info, such as 
name, email, age, sex, signup date, country and city (store operates in Poland, Germany and Czechia). Additonally,
each customer has his own unique business ID assigned by the system. Loyalty program is implemented in the store:
there are 4 levels (Bronze, Silver, Gold, Platinum). 

2) Products' data consists of name of the product, assigned category, brand, price, cost and rating given by the 
buyers. There is also unique product ID given by the system

3) There is also data of events which happened on the company's website. Each event is assigned specific
type which is represented in the sequence Click on the product -> Product is added to cart -> Order checkout 
-> Purchase compelted and specific ID. System also records medium of the event (store's app or any web browser),
session ID, time when event occured, customer and product related to event.

4) When customer clicks "purchase", order is created. Customer also chooses delivery method (either by courier, post, 
at pickup point or pickup locker), payment method (Apple Pay, debit card, cash on delivery, or bank transfer) and quantity
of the product ordered. Discount is applied in some cases to the order (up to 80%) and there is also a shipping
fee. Time of order's compeletion is also recorded by the system. 

## Data Warehouse design
To store all the data for future analysis the following data warehouse schema is proposed:
<img width="14193" height="11010" alt="ERD Electronics store-1" src="https://github.com/user-attachments/assets/bbd1960b-cf11-44b8-b578-8bd19767b10a" />
It is a constellation schema since due to different structure of order and event tables there should be two 
fact tables. Also, date and time tables are populated using SQL scripts once afrer warehouse creation. 

## Azure infrastructure
Data is generated using Python scripts, then it is inserted into Azure Blob storage as .csv files.
This is done in order to store raw data so it could be transformed later to respect the format of 
tables in data warehouse (several columns need to be changed and some new columns created). 
Data warehouse is created as a SQL database on Azure SQL server. After creation scripts should be run
in order to populate date_d and time_d tables.
Azure Data Factory is used to perform data transformation and insertion from raw blob storage into SQL data
warehouse. Pipelines are set to run after each insertion and they don't allow duplicates (determined by business 
keys or composite keys).
**Main pipeline:**
<img width="734" height="253" alt="Screenshot 2026-07-19 at 20 15 19" src="https://github.com/user-attachments/assets/81a393e0-9f13-4dc0-91ae-b16328e4370c" />






