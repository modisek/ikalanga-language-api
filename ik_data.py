import csv 
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ik_data"]
col = db["wordlist"]
with open('dictionary.txt') as f:
    reader = csv.reader(f, delimiter='\t')
    data = [x for x in reader]
    for i in data:
        print(i[1]+"--"+ i[5])
        col.insert_one({"word":i[1], "definition":i[5] })
