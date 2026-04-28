USE CustomerShoppingDB;
GO


-- Customers Table
CREATE TABLE Customers (
    Customer_ID INT PRIMARY KEY,
    Age INT,
    Age_Group VARCHAR(20),
    Gender VARCHAR(20),
    Location VARCHAR(100),
    Subscription_Status VARCHAR(10),
    Subscription_Flag INT,
    Previous_Purchases INT,
    Loyalty_Segment VARCHAR(50)
);

-- Products Table
CREATE TABLE Products (
    Product_ID INT IDENTITY(1,1) PRIMARY KEY,
    Item_Purchased VARCHAR(255),
    Category VARCHAR(100),
    Size VARCHAR(20),
    Color VARCHAR(50)
);

-- Transactions Table
CREATE TABLE Transactions (
    Transaction_ID INT IDENTITY(1,1) PRIMARY KEY,
    Customer_ID INT,
    Product_ID INT,
    Purchase_Amount_USD DECIMAL(10,2),
    Season VARCHAR(20),
    Shipping_Type VARCHAR(50),
    Discount_Applied VARCHAR(10),
    Discount_Flag INT,
    Promo_Code_Used VARCHAR(10),
    Promo_Used_Flag INT,
    Payment_Method VARCHAR(50),
    Frequency_of_Purchases VARCHAR(50),

    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
    FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);

-- Reviews Table
CREATE TABLE Reviews (
    Review_ID INT IDENTITY(1,1) PRIMARY KEY,
    Customer_ID INT,
    Product_ID INT,
    Review_Rating DECIMAL(3,1),
    Review_Category VARCHAR(20),

    FOREIGN KEY (Customer_ID) REFERENCES Customers(Customer_ID),
    FOREIGN KEY (Product_ID) REFERENCES Products(Product_ID)
);

