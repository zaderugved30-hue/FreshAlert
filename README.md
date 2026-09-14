# 🍃 FreshAlert – Food Expiry Management System

FreshAlert is a simple **Food Expiry Management System** developed using **Python Flask, MySQL, HTML, and CSS**.

The system helps users manage food inventory, track expiry dates, identify food that is expiring soon, manage suppliers, and reduce unnecessary food waste.

---

## 🎯 Project Objective

The main objective of FreshAlert is to provide a simple system for tracking food products and their expiry dates.

FreshAlert automatically classifies food items as:

- 🟢 **Safe** – 10 or more days remaining
- 🟡 **Expiring Soon** – Less than 10 days remaining
- 🔴 **Expired** – Expiry date has passed

---

## ✨ Features

- User Registration
- User Login and Logout
- Food Inventory Management
- Add Food Items
- Edit Food Items
- Delete Food Items
- Search Food by Name or Category
- Automatic Expiry Status
- Supplier Management
- User Profile
- Dashboard with Inventory Statistics
- Food Status Overview

---

# 📸 Application Screenshots

## 1. 📝 User Registration

New users can create a FreshAlert account by entering their full name, username, password, and confirming their password.

<img width="1920" height="1080" alt="Screenshot (157)" src="https://github.com/user-attachments/assets/2c1e1976-bbcb-4de5-a58b-801c1c1fbe7e" />


---

## 2. 🔐 User Login

Registered users can securely log in using their username and password.

<img width="1920" height="1080" alt="Screenshot (158)" src="https://github.com/user-attachments/assets/a487fbdf-3354-4407-9322-4d76ebffb7bf" />


---

## 3. 📊 Dashboard

The dashboard provides a quick overview of the food inventory.

It displays:

- Total Items
- Expired Items
- Expiring Soon Items
- Safe Items
- Current Date
- Food Status Overview

![Dashboard](screenshots/dashboard.png)

---

## 4. 🍴 Food Items

The Food Items page displays all food products stored in the system.

Information includes:

- Food ID
- Food Name
- Category
- Quantity
- Current Date
- Expiry Date
- Expiry Status
- Edit and Delete Actions

Users can also search for food using the food name or category.

![Food Items](screenshots/foods.png)

---

## 5. ➕ Add Food Item

Users can add new food products to the inventory.

The form contains:

- Food Name
- Category
- Quantity
- Unit
- Purchase Date
- Expiry Date
- Supplier

![Add Food](screenshots/add-food.png)

---

## 6. 🚚 Suppliers

The Suppliers page displays information about food suppliers.

Supplier information includes:

- Supplier ID
- Supplier Name
- Phone Number
- Email Address

![Suppliers](screenshots/suppliers.png)

---

## 7. 👤 User Profile

The Profile page displays the currently logged-in user's account information.

It shows:

- Full Name
- Username
- Role

![Profile](screenshots/profile.png)

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web application framework |
| MySQL | Database management |
| HTML | Web page structure |
| CSS | User interface design |
| Jinja2 | Dynamic HTML templates |
| MySQL Connector | Connecting Flask with MySQL |

---

# 🗄️ Database

FreshAlert uses a **MySQL database** to store application data.

Main database tables include:

- `users`
- `food_items`
- `suppliers`
- `categories`
- `activity_log`

The project demonstrates SQL concepts such as:

- CREATE
- INSERT
- SELECT
- UPDATE
- DELETE
- WHERE
- LIKE
- Primary Keys
- Foreign Keys
- Table Relationships

---

# 📁 Project Structure

```text
FreshAlert/
│
├── app.py
├── requirements.txt
│
├── static/
│   └── style.css
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── foods.html
│   ├── add_food.html
│   ├── edit_food.html
│   ├── suppliers.html
│   └── profile.html
│
└── screenshots/
    ├── register.png
    ├── login.png
    ├── dashboard.png
    ├── foods.png
    ├── add-food.png
    ├── suppliers.png
    └── profile.png
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

## 2. Open the Project

```bash
cd FreshAlert
```

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

## 4. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\Activate.ps1
```

## 5. Install Required Packages

```bash
pip install -r requirements.txt
```

## 6. Configure MySQL

Create the required MySQL database and update your local database configuration.

Do not upload your real MySQL password to GitHub.

## 7. Run the Application

```bash
python app.py
```

Then open the local Flask application in your browser.

---

# 🔄 Application Workflow

```text
Register
   ↓
Login
   ↓
Dashboard
   ↓
View Food Inventory
   ↓
Add / Edit / Delete Food
   ↓
Check Expiry Status
   ↓
View Suppliers
   ↓
View Profile
   ↓
Logout
```

---

# 🌱 Why FreshAlert?

Food products are often wasted because their expiry dates are forgotten.

FreshAlert provides a simple way to organize food inventory and quickly identify products that are safe, expiring soon, or already expired.

### Small Steps • Less Waste 🍃

---

# 👨‍💻 Author

**Rugved Zade**

PGCP-BDA + PGCP-AI  
C-DAC

---

## 📌 Project Status

✅ Registration  
✅ Login  
✅ Dashboard  
✅ Food Management  
✅ Expiry Tracking  
✅ Supplier Management  
✅ User Profile  
✅ Search  
✅ Logout  

**FreshAlert – Keep Your Food Fresh, Keep Your Life Healthy. 🍃**
