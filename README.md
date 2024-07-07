# **Automate WhatsApp Messages for Efficient Intern Communication**

Streamline your workflow by automating WhatsApp messages to interns who fill out your company form. This project eliminates manual effort, reduces duplication, and ensures seamless communication. With automation, you can focus on more critical tasks while keeping your interns informed and engaged.

### ``` Libraries used: pywhatkit, mysql-connector-python, datetime, threading  ```

### Getting Started

## Step 1: Clone the repository
<pre>
git clone https://github.com/Khushiaggarwal710/automated-IM-whatsapp.git
</pre>

## Step 2: Install dependencies
<pre>
pip install -r requirements.txt        
</pre>

## Step 3: Create database & table in MySQL
<pre>
Database: 'automatedIM_DB'
Table: 'interns' 
</pre>

Structure of interns:

![sql2](https://github.com/Khushiaggarwal710/automated-IM-whatsapp/assets/107229428/8848b1ed-25f3-4dbf-9950-cb850034d10d)

Sample Data:

![sql](https://github.com/Khushiaggarwal710/automated-IM-whatsapp/assets/107229428/7222cd60-e02c-4ee4-9015-402a0ef5b02d)


## Step 4: Update localhost, username, password in connectivity.py
<pre>
mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password',
        database='automatedIM_DB'
)        
</pre>

## Step 5: Run the application
<pre>
python automate.py      
</pre>








