--A) TOP 10 HIGH-VALUE CUSTOMERS--
SELECT TOP 10
    c.Customer_ID,
    c.Gender,
    c.Location,
    c.Loyalty_Segment,
    SUM(t.Purchase_Amount_USD) AS Total_Spent
FROM Transactions t
JOIN Customers c ON t.Customer_ID = c.Customer_ID
GROUP BY c.Customer_ID, c.Gender, c.Location, c.Loyalty_Segment
ORDER BY Total_Spent DESC;


--B) AVERAGE ORDER VALUE--
SELECT AVG(Purchase_Amount_USD) AS Average_Order_Value
FROM Transactions;

--C) WHICH CATEGORY HAS BEST REVIEWS?--
SELECT 
    p.Category,
    AVG(r.Review_Rating) AS Avg_Rating,
    COUNT(*) AS Review_Count
FROM Reviews r
JOIN Products p ON r.Product_ID = p.Product_ID
GROUP BY p.Category
ORDER BY Avg_Rating DESC;

--D) DOES DISCOUNT LEAD TO HIGHER SPENDING?--
SELECT 
    Discount_Applied,
    AVG(Purchase_Amount_USD) AS Avg_Spending,
    SUM(Purchase_Amount_USD) AS Total_Revenue
FROM Transactions
GROUP BY Discount_Applied;

--E) SUBSCRIBERS VS NON-SUBSCRIBERS--
SELECT 
    c.Subscription_Status,
    COUNT(DISTINCT c.Customer_ID) AS Total_Customers,
    SUM(t.Purchase_Amount_USD) AS Total_Revenue,
    AVG(t.Purchase_Amount_USD) AS Avg_Order_Value
FROM Customers c
JOIN Transactions t ON c.Customer_ID = t.Customer_ID
GROUP BY c.Subscription_Status;

--F) REPEAT PURCHASE BEHAVIOR USING PREVIOUS PURCHASES--
SELECT 
    CASE
        WHEN Previous_Purchases < 10 THEN 'Low Repeat'
        WHEN Previous_Purchases BETWEEN 10 AND 25 THEN 'Moderate Repeat'
        ELSE 'High Repeat'
    END AS Repeat_Level,
    COUNT(*) AS Customer_Count
FROM Customers
GROUP BY 
    CASE
        WHEN Previous_Purchases < 10 THEN 'Low Repeat'
        WHEN Previous_Purchases BETWEEN 10 AND 25 THEN 'Moderate Repeat'
        ELSE 'High Repeat'
    END
ORDER BY Customer_Count DESC;
