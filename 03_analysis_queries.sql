--1. Total Sales--
/*SELECT SUM(Purchase_Amount_USD) AS Total_Sales
FROM Transactions;

--2.TOTAL CUSTOMERS--
SELECT COUNT(DISTINCT Customer_ID) AS Total_Customers
FROM Customers;

--3. Top products by sales--
SELECT 
    p.Category,
    SUM(t.Purchase_Amount_USD) AS Total_Sales
FROM Transactions t
JOIN Products p ON t.Product_ID = p.Product_ID
GROUP BY p.Category
ORDER BY Total_Sales DESC;*/


--4. TOP PURCHASED ITEMS--
SELECT TOP 10
    p.Item_Purchased,
    COUNT(*) AS Purchase_Count,
    SUM(t.Purchase_Amount_USD) AS Total_Revenue
FROM Transactions t
JOIN Products p ON t.Product_ID = p.Product_ID
GROUP BY p.Item_Purchased
ORDER BY Purchase_Count DESC;

--5.GENDER-WISE PURCHASE ANALYSIS--
SELECT 
    c.Gender,
    COUNT(*) AS Total_Transactions,
    SUM(t.Purchase_Amount_USD) AS Total_Sales,
    AVG(t.Purchase_Amount_USD) AS Avg_Spending
FROM Transactions t
JOIN Customers c ON t.Customer_ID = c.Customer_ID
GROUP BY c.Gender
ORDER BY Total_Sales DESC;

--AGE GROUP ANALYSIS--
SELECT 
    c.Age_Group,
    COUNT(*) AS Total_Transactions,
    SUM(t.Purchase_Amount_USD) AS Total_Sales,
    AVG(t.Purchase_Amount_USD) AS Avg_Spending
FROM Transactions t
JOIN Customers c ON t.Customer_ID = c.Customer_ID
GROUP BY c.Age_Group
ORDER BY Total_Sales DESC;


--7. LOCATION-WISE SALES--
SELECT 
    c.Location,
    COUNT(*) AS Total_Transactions,
    SUM(t.Purchase_Amount_USD) AS Total_Sales
FROM Transactions t
JOIN Customers c ON t.Customer_ID = c.Customer_ID
GROUP BY c.Location
ORDER BY Total_Sales DESC;

--8. SEASONAL SHOPPING TREND--
SELECT 
    Season,
    COUNT(*) AS Total_Transactions,
    SUM(Purchase_Amount_USD) AS Total_Sales
FROM Transactions
GROUP BY Season
ORDER BY Total_Sales DESC;


--9. PAYMENT METHOD PREFERENCE--
SELECT 
    Payment_Method,
    COUNT(*) AS Usage_Count,
    SUM(Purchase_Amount_USD) AS Total_Sales
FROM Transactions
GROUP BY Payment_Method
ORDER BY Usage_Count DESC;


--10. SHIPPING TYPE ANALYSIS--
SELECT 
    Shipping_Type,
    COUNT(*) AS Total_Orders,
    SUM(Purchase_Amount_USD) AS Total_Sales
FROM Transactions
GROUP BY Shipping_Type
ORDER BY Total_Sales DESC;

--11. SUBSCRIPTION STATUS IMPACT--
SELECT 
    c.Subscription_Status,
    COUNT(*) AS Total_Transactions,
    SUM(t.Purchase_Amount_USD) AS Total_Sales,
    AVG(t.Purchase_Amount_USD) AS Avg_Spending
FROM Transactions t
JOIN Customers c ON t.Customer_ID = c.Customer_ID
GROUP BY c.Subscription_Status;

--12. DISCOUNT IMPACT ON SALES--
SELECT 
    Discount_Applied,
    COUNT(*) AS Total_Transactions,
    SUM(Purchase_Amount_USD) AS Total_Sales,
    AVG(Purchase_Amount_USD) AS Avg_Spending
FROM Transactions
GROUP BY Discount_Applied;

--13. PROMO CODE EFFECTIVENESS--
SELECT 
    Promo_Code_Used,
    COUNT(*) AS Total_Transactions,
    SUM(Purchase_Amount_USD) AS Total_Sales,
    AVG(Purchase_Amount_USD) AS Avg_Spending
FROM Transactions
GROUP BY Promo_Code_Used;

--14. REVIEW RATING IMPACT
SELECT 
    Review_Category,
    COUNT(*) AS Review_Count,
    AVG(Review_Rating) AS Avg_Rating
FROM Reviews
GROUP BY Review_Category
ORDER BY Avg_Rating DESC;

--15. LOYALTY SEGMENT ANALYSIS
SELECT 
    c.Loyalty_Segment,
    COUNT(*) AS Total_Transactions,
    SUM(t.Purchase_Amount_USD) AS Total_Sales,
    AVG(t.Purchase_Amount_USD) AS Avg_Spending
FROM Transactions t
JOIN Customers c ON t.Customer_ID = c.Customer_ID
GROUP BY c.Loyalty_Segment
ORDER BY Total_Sales DESC;





