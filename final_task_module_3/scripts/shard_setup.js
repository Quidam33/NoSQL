sh.enableSharding("university_db")

sh.shardCollection(
  "university_db.students",
  { "_id": "hashed" }
)

sh.shardCollection(
  "university_db.grades",
  { "student_id": "hashed" }
)

print("Sharding enabled")
