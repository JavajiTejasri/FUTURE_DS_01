# FUTURE INTERNS - DATA SCIENCE TASK 1

CIN ID: FIT/APR26/DS16969

---

# 📊 Sales Data Analysis (Task 1)

## 📌 Project Overview
This project focuses on analyzing business sales data to identify revenue trends, customer behavior, and key factors influencing sales performance. The goal is to extract meaningful insights that can help businesses make data-driven decisions.

---

## 🛠 Tools & Technologies Used
- Python
- Pandas (Data manipulation and analysis)
- Matplotlib (Data visualization)

---

## 🎯 Objective
The main objectives of this project are:
- Analyze sales data to identify revenue patterns
- Understand customer purchasing behavior
- Identify high-performing days and customer segments
- Generate insights to improve business revenue

---

## 📂 Dataset Description
The dataset contains sales-related information such as:
- Day of transaction
- Customer group size
- Gender of customers
- Individual sales amount
- Calculated **Revenue**

---

## ⚙️ Steps Performed
1. Imported the dataset using pandas
2. Explored data using `.head()`, `.info()`, `.describe()`
3. Created a new column **Revenue**
4. Grouped data by:
   - Day
   - Group size
   - Gender
5. Performed aggregation to calculate total revenue
6. Visualized the results using bar charts

---

## 📊 Data Visualization

### 🔹 Revenue by Day
![Revenue by Day](revenue_by_day.png)

### 🔹 Revenue by Group Size
![Revenue by Group Size](revenue_by_group_size.png)

### 🔹 Revenue by Gender
![Revenue by Gender](revenue_by_gender.png)

---

## 🔍 Key Insights
- Weekend days (**Saturday & Sunday**) generate the highest revenue
- Customers in **larger groups** tend to spend more compared to smaller groups
- Revenue differences between genders are **minimal**
- Peak business activity occurs during weekends
- Group-based customer visits significantly contribute to overall sales

---

## 📈 Business Recommendations
- Focus marketing and promotions on **weekends**
- Offer **group discounts or combo offers** to attract larger groups
- Improve customer experience during peak days to maximize revenue
- Introduce targeted campaigns to increase weekday sales
- Optimize staffing during high-traffic days (weekends)

---

## ✅ Conclusion
Sales performance is strongly influenced by customer group size and timing of visits. By focusing on weekends and encouraging group purchases, businesses can significantly increase their revenue and improve overall performance.

---

## 🚀 Future Work
- Build predictive models for sales forecasting
- Perform customer segmentation analysis
- Develop dashboards for real-time sales monitoring
- Integrate machine learning for demand prediction
