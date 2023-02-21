import json
import sqlite3 

with open('store.json') as json_file:
    data = json.load(json_file)
    cnt = len(data['myFoods'])

# print(data)

# Connect to sqlite database
conn = sqlite3.connect('food.db')
cursor = conn.cursor()
# cursor object
# cursor = conn.cursor()
# # drop query
# cursor.execute("DROP TABLE IF EXISTS STUDENT")
# # create query
# query = """CREATE TABLE FOOD(
#         ID INT PRIMARY KEY NOT NULL,
#         NAME CHAR(20) NOT NULL, 
#         CATEGORY CHAR(20), 
#         SUBNAME CHAR(20), 
#         DESCRIPTION CHAR(100),
#         PRICE INT,
#         IS_VEGAN BOOL,
#         IS_SPECIAL BOOL,
#         TOPPINGS TEXT)"""
# cursor.execute(query)
# # commit and close
# conn.commit()
# conn.close()

def create():
    try:
        query = ('INSERT INTO FOOD (ID,NAME,CATEGORY,SUBNAME,DESCRIPTION,PRICE,IS_VEGAN,IS_SPECIAL,TOPPINGS)'
                'VALUES (:ID,:NAME,:CATEGORY,:SUBNAME,:DESCRIPTION,:PRICE,:IS_VEGAN,:IS_SPECIAL,:TOPPINGS);')
        # for i in range(cnt)
        for i in range(cnt):
            params = {
                        'ID': data['myFoods'][i]['id'],
                        'NAME': data['myFoods'][i]['name'],
                        'CATEGORY': data['myFoods'][i]['name'],
                        'SUBNAME': data['myFoods'][i]['foods'][0]['name'],
                        'DESCRIPTION': data['myFoods'][i]['foods'][0]['description'],
                        'PRICE': data['myFoods'][i]['foods'][0]['price'],
                        'IS_VEGAN': data['myFoods'][i]['foods'][0]['is_vegan'],
                        'IS_SPECIAL': data['myFoods'][i]['foods'][0]['is_special'],
                        'TOPPINGS': data['myFoods'][i]['foods'][0]['toppings'][0] +" " + data['myFoods'][i]['foods'][0]['toppings'][1],
                }
            print(params)
            conn.execute(query, params)
            conn.commit()
    except:
        print("Error in Record Creation")

def read_one():
    ids = int(input("Enter Your ID: "))
    query = "SELECT * from FOOD WHERE ID = ?"
    result = cursor.execute(query, (ids,))
    if (result):
        for i in result:
            print(f"ID: {i[0]}")
            print(f"NAME: {i[1]}")
            print(f"CATEGORY: {i[2]}")
            print(f"SUBNAME: {i[3]}")
            print(f"DESCRIPTION: {i[4]}")
            print(f"PRICE: {i[5]}")
            print(f"IS_VEGAN: {i[6]}")
            print(f"IS_SPECIAL: {i[7]}")
            print(f"TOPPINGS: {i[8]}")
    else:
        print("Roll Number Does not Exist")
        cursor.close()

def filter_one():
    # ids = int(input("Enter Your ID: "))
    query = "SELECT * from FOOD WHERE IS_VEGAN = TRUE"
    result = cursor.execute(query)
    if (result):
        for i in result:
            print(f"ID: {i[0]}")
            print(f"NAME: {i[1]}")
            print(f"CATEGORY: {i[2]}")
            print(f"SUBNAME: {i[3]}")
            print(f"DESCRIPTION: {i[4]}")
            print(f"PRICE: {i[5]}")
            print(f"IS_VEGAN: {i[6]}")
            print(f"IS_SPECIAL: {i[7]}")
            print(f"TOPPINGS: {i[8]}\n")
    else:
        print("Roll Number Does not Exist")
        cursor.close()


def read_all():
    query = "SELECT * from FOOD"
    result = cursor.execute(query)
    if (result):
        print("\n<===Available Records===>")
        for i in result:
            print(f"ID: {i[0]}")
            print(f"NAME: {i[1]}")
            print(f"CATEGORY: {i[2]}")
            print(f"SUBNAME: {i[3]}")
            print(f"DESCRIPTION: {i[4]}")
            print(f"PRICE: {i[5]}")
            print(f"IS_VEGAN: {i[6]}")
            print(f"IS_SPECIAL: {i[7]}")
            print(f"TOPPINGS: {i[8]}\n")
    else:
        pass
def update():
    idd = int(input("Enter ID: "))
    name = input("Enter Name: ")
    category = input("Enter CATEGORY: ")
    subname = input("Enter SUBNAME: ")
    description = input("Enter DESCRIPTION: ")
    price = int(input("Enter PRICE: "))
    is_vegan = bool(input("Enter IS_VEGAN: "))
    is_special = bool(input("Enter IS_SPECIAL: "))
    toppings = input("Enter TOPPINGS: ")

    params = ( name,category,subname,description,price,is_vegan,is_special,toppings,idd,)
    query = "UPDATE FOOD SET  NAME = ?,CATEGORY = ?,SUBNAME = ?,DESCRIPTION = ?,PRICE = ?,IS_VEGAN = ?,IS_SPECIAL = ?,TOPPINGS = ? WHERE ID = ?"
    result = cursor.execute(query, params)
    conn.commit()
    cursor.close()
    if (result):
        print("Records Updated")
    else:
        print("Something Error in Updation")
def delete():

    idd = int(input("Enter ID: "))
    query = "DELETE from FOOD where ID = ?"
    result = cursor.execute(query, (idd,))
    conn.commit()
    cursor.close()
    if (result):
        print("One record Deleted")
    else:
        print("Something Error in Deletion")
try:
    while (True):
        print("1). Create Records: ")
        print("2). Read Records: ")
        print("3). Update Records: ")
        print("4). Delete Records: ")
        print("5). Fileter by IS_VEGAN: ")
        print("6). Exit")
        ch = int(input("Enter Your Choice: "))
        if ch == 1:
            create()
        elif ch == 2:
            print("1). Read Single Record")
            print("2). Read All Records")
            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                read_one()
            elif choice == 2:
                read_all()
            else:
                print("Wrong Choice Entered")
        elif ch == 3:
            update()
        elif ch == 4:
            delete()
        elif ch == 5:
            filter_one()
        elif ch == 6:
            break
        else:
            print("Enter Correct Choice")
except:
    print("Database Error")
