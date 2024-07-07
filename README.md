# **Automate WhatsApp Messages for Efficient Intern Communication**

Streamline your workflow by automating WhatsApp messages to interns who fill out your company form. This project eliminates manual effort, reduces duplication, and ensures seamless communication. With automation, you can focus on more critical tasks while keeping your interns informed and engaged.

### ``` Libraries used: pywhatkit, mysql-connector-python, datetime, threading  ```

### Getting Started

## Step 1: Clone the repository
git clone https://github.com/Khushiaggarwal710/automated-IM-whatsapp.git

## Step 2: Install dependencies
pip install -r requirements.txt

## Step 3: Create database & table in MySQL
Database: 'automatedIM_DB'
Table: 'interns' 

Structure of interns:


Sample Data:

## Step 4: Update localhost, username, password in connectivity.py
mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='automatedIM_DB'
)

## Step 5: Run the application
python automate.py