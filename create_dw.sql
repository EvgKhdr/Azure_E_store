
CREATE SCHEMA dw;

GO 

CREATE TABLE dw.time_d(
    time_id INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    full_time VARCHAR(8) NOT NULL,
    hour INT NOT NULL,
    minute INT NOT NULL,
    second INT NOT NULL,
    time_of_day VARCHAR(10) CHECK (time_of_day IN('Morning', 'Afternoon', 'Evening', 'Night')) NOT NULL

)
GO

CREATE TABLE dw.date_d(
    date_id INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    full_date DATE NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    date INT NOT NULL,
    time_of_year VARCHAR(10) CHECK (time_of_year IN ('Winter','Spring','Summer','Autumn')),
    weekday VARCHAR(15) CHECK (weekday IN ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')),
    is_weekend BIT
)
GO

CREATE TABLE dw.customer_d(
    customer_id INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    customer_bk VARCHAR(8) NOT NULL,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    age INT NOT NULL CHECK (age >= 16 AND age <= 100),
    age_group VARCHAR(15) CHECK (age_group IN('Young','Middle-aged', 'Adult', 'Senior')),
    email VARCHAR(60),
    gender VARCHAR(6) CHECK (gender IN('Male', 'Female')),
    country VARCHAR(30),
    city VARCHAR(40),
    account_age INT NOT NULL,
    bonus_points INT CHECK (bonus_points >=0 AND bonus_points<=1000),
    loyalty_level VARCHAR(10) CHECK (loyalty_level IN ('Bronze', 'Silver', 'Gold', 'Platinum')),
)
GO

CREATE TABLE dw.product_d(
    product_id INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    product_bk VARCHAR(12) NOT NULL,
    name VARCHAR(50) NOT NULL,
    category VARCHAR(15) NOT NULL DEFAULT 'Other',
    brand VARCHAR(15) NOT NULL DEFAULT 'Unknown',
    price DECIMAL(7,2) NOT NULL,
    cost DECIMAL(7,2) NOT NULL,
    rating DECIMAL(2,1) NOT NULL DEFAULT 0 CHECK (rating >= 0 AND rating <= 5)
)
GO

CREATE TABLE dw.event_attr_d(
    event_attr_id INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    type VARCHAR(15) NOT NULL,
    medium VARCHAR(10) NOT NULL,
    session_id VARCHAR(15) NOT NULL
)
GO 

CREATE TABLE dw.event_f(
    event_id INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    event_bk VARCHAR(13) NOT NULL,
    product_id INT FOREIGN KEY REFERENCES dw.product_d(product_id),
    customer_id INT FOREIGN KEY REFERENCES dw.customer_d(customer_id),
    event_time INT FOREIGN KEY REFERENCES dw.time_d(time_id),
    event_date INT FOREIGN KEY REFERENCES dw.date_d(date_id),
    event_attr_id INT FOREIGN KEY REFERENCES dw.event_attr_d(event_attr_id)
)
GO

CREATE TABLE dw.order_attr_d(
    order_attr_id INT IDENTITY(1, 1) NOT NULL PRIMARY KEY,
    delivery VARCHAR(20) NOT NULL,
    payment VARCHAR(20) NOT NULL,
    session VARCHAR(15) NOT NULL
)
GO

CREATE TABLE dw.order_f(
    order_id INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    order_bk VARCHAR(9) NOT NULL,
    quantity INT NOT NULL,
    discount DECIMAL(2,1) NOT NULL,
    profit DECIMAL(8,2) NOT NULL,
    total_cost DECIMAL (8,2) NOT NULL,
    shipping DECIMAL(6,2) NOT NULL,
    time_of_completion_hours INT NOT NULL,
    order_date INT FOREIGN KEY REFERENCES dw.date_d(date_id),
    order_time INT FOREIGN KEY REFERENCES dw.time_d(time_id),
    product_id INT FOREIGN KEY REFERENCES dw.product_d(product_id),
    customer_id  INT FOREIGN KEY REFERENCES dw.customer_d(customer_id),
    order_attr_id  INT FOREIGN KEY REFERENCES dw.order_attr_d(order_attr_id)
)

GO


DROP TABLE IF EXISTS dw.order_f;
DROP TABLE IF EXISTS dw.event_f;

DROP TABLE IF EXISTS dw.order_attr_d;
DROP TABLE IF EXISTS dw.event_attr_d;
DROP TABLE IF EXISTS dw.product_d;
DROP TABLE IF EXISTS dw.customer_d;
DROP TABLE IF EXISTS dw.date_d;
DROP TABLE IF EXISTS dw.time_d;


