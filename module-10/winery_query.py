# Aaron Crose shanika brittni
# Module 10

import mysql.connector
from mysql.connector import errorcode

config = {
"user": "root",
"password": "12qwaszx!@QWASZX",
"host": "127.0.0.1",
"database" : "bacchuswinery",
"raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MysQl on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print ("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)



# select all fields for genre 
cursor = db.cursor()
cursor.execute("SELECT distributor_id, distributor_name, distributor_sales FROM distributors")
distributors = cursor.fetchall()
print("Displaying Distributor Records")
for distributor in distributors:
    print("distributor ID: {}\n distributor Name: {}\n distributor sales: {}\n".format(distributors[0], distributors[1], distributors[2])) #three fields



# select all fields for genre 
cursor = db.cursor()
cursor.execute("SELECT employee_id, employee_first, employee_last, employee_department FROM employee")
employees = cursor.fetchall()
print("Displaying employee Records")
for employee in employees:
    print("employee ID: {}\n employee first: {}\n employee last: {}\n department".format(employee[0], employee[1])) #three fields


# select short films
cursor = db.cursor()
cursor.execute("SELECT hours_amount, quarter_id, employee_id FROM hours")
hours = cursor.fetchall()
print("Displaying Hour Records")
for hour in hours:
    print("hour amount: {}\n quarter: {}\n employee ID: {}\n".format(hours[0], hours[1])) #two fields

# film names by director
cursor = db.cursor()
cursor.execute("SELECT order_id, order_placement_date, order_delivery_date, order_amount, distributor_id, wine_id FROM orders")
orders = cursor.fetchall()
print("Displaying Order Records")
for order in orders:
    print("order ID: {}\n placement date: {}\n delivery date: {}\n order amount: {}\n distributor id: {}\n wine id {}\n".format(orders[0], orders[1])) #two fields

cursor = db.cursor()
cursor.execute("SELECT quarter_id, quarter_start_date, quarter_end_date FROM quarter")
quarters = cursor.fetchall()
print("Displaying quarter Records")
for quarter in quarters:
    print("quarter : {}\n start date: {}\n end date: {}\n".format(quarter[0], quarter[1])) 

cursor = db.cursor()
cursor.execute("SELECT shipment_id, supplier_id, shipment_order_placement_date, shipment_expected_delivery_date, shipment_actual_delivery_date FROM shipments")
shipments = cursor.fetchall()
print("Displaying shipments Records")
for shipment in shipments:
    print("shipment id : {}\n supplier id: {}\n order date: {}\n expected delivery date: {}\n delivery date: {}\n".format(shipments[0], shipments[1])) 

cursor = db.cursor()
cursor.execute("SELECT supplier_id, supplier_name, supplier_product FROM suppliers")
suppliers = cursor.fetchall()
print("Displaying supplier Records")
for supplier in suppliers:
    print("supplier ID : {}\n Supplier name: {}\n products: {}\n".format(suppliers[0], suppliers[1]))

cursor = db.cursor()
cursor.execute("SELECT wine_id, wine_type, wine_stock FROM wines")
wines = cursor.fetchall()
print("Displaying wine Records")
for wine in wines:
    print("wine ID : {}\n wine type: {}\n wine stock: {}\n".format(wines[0], wines[1]))  