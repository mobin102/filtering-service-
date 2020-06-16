import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# print(myclient.list_database_names())

# dblist = myclient.list_database_names()
# if "mydatabase" in dblist:
#     print("The database exists.")

# print(30*"#")
# mycol = mydb["customers"]
# print(mydb.list_collection_names())

# collist = mydb.list_collection_names()
# if "customers" in collist:
#     print("The collection exists.")

# print(30*"#")

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Rectangular"]
mycol = mydb["FilteredRec"]
#print([x for x in mycol.find({},{ 'ObjectId': 0})])
mycol.drop()
#1
{
"main": {"x":
 0, "y": 0, "width": 10, "height": 20},
"input": [
{"x":
 2, "y": 18, "width": 5, "height": 4},
{"x":
 12, "y": 18, "width": 5, "height": 4},
{"x":
 -1, "y": -1, "width": 5, "height": 4}
]
}
#2
{
"main":
    {"x": 3, "y": 2, "width": 5, "height": 10},
"input": [
    {"x": 4, "y": 10, "width": 1, "height": 1},
    {"x": 9, "y": 10, "width": 5, "height": 4}
    ]
}
