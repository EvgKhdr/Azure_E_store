from faker import Faker
import pandas as pd
import random

def multiple_customers_generation(num_customers, seed, start_signup_date, end_signup_date, countries):
    customers_columns = ['Name', 'Surname', 'Age', 'Email', 'Sex', 'Customer_ID', 'Country','City', 'Signup_date', 'Loyalty_level']
    Faker.seed(seed)
    random.seed(seed)
    customers_df = pd.DataFrame(columns=customers_columns)
    fake_instances = {loc: Faker(loc) for loc in countries}
    
    for i in range(num_customers):
        customer_country = random.choice(countries)
        customers_df.loc[i] = one_customer_generation(
            customer_country, start_signup_date, end_signup_date, fake_instances
        )
    
    customers_df.to_csv('customers.csv', header=True, columns= ['Customer_ID'],index=False)
    return customers_df


def one_customer_generation(customer_country, start_signup_date, end_signup_date, fake_instances):

    customer = fake_instances[customer_country]

    sex_choice = random.randint(1, 2)
    if sex_choice == 1:
        sex = 'M'
        name = customer.first_name_male()
    elif sex_choice == 2:
        sex = 'F'
        name = customer.first_name_female()

    surname = customer.last_name()
    email = customer.free_email()
    customer_id = customer.bothify(text='??######').upper()
    city = customer.city()
    date = customer.date_between(start_date=start_signup_date, end_date=end_signup_date)
    level = customer.random_element(elements=('Bronze', 'Silver', 'Gold', 'Platinum'))

    customer_instance = {
        'Name': name,
        'Surname': surname,
        'Age': random.randint(16, 90),
        'Email': email,
        'Sex': sex,
        'Customer_ID': customer_id,
        'Country': customer_country[-2:],  
        'City': city,
        'Signup_date': date,
        'Loyalty_level': level
    }
    return customer_instance



    