import time
import random
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["university_db"]

students = db["students"]

def insert_test(n=5000):
    start = time.time()
    docs = []

    for i in range(n):
        docs.append({
            "_id": f"test_{i}",
            "first_name": "Test",
            "last_name": "Student",
            "group_id": f"G{random.randint(1,10)}",
            "year": 2022
        })

    students.insert_many(docs)
    end = time.time()

    print("Insert time:", end - start)

def read_test(n=2000):
    start = time.time()

    for i in range(n):
        sid = f"test_{random.randint(0,4999)}"
        students.find_one({"_id": sid})

    end = time.time()

    print("Read time:", end - start)

if __name__ == "__main__":
    insert_test()
    read_test()
