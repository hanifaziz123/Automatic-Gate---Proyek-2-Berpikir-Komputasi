import json
import cv2



with open(r"C:\Users\mocha\Documents\TUGAS BERKOM ITB\Proyek 2\database.json", "r") as f:
    db = json.load(f)

qr_id = "STU16525232"

user = None
for u in db["users"]:
    if u["id"] == qr_id:
        user = u
        break

print(user["name"])