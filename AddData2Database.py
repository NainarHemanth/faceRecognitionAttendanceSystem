import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognition-9e552-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "RA2111003011294":
        {
            "Name": "N Hemanth Kumar Sai",
            "id": "RA2111003011294",
            "Department": "CTECH",
            "Section": "E2",
            "Batch": 2,
            "Academic Year": "2021 - 2025",
            "Total-attendance": 40,
            "Last-attendance-time": "2023-12-11 11:59:00"
        },
    "RA2111026010179":
        {
            "Name": "Uday Kiran C",
            "id": "RA2111026010179",
            "Department": "CINTEL",
            "Section": "W1",
            "Batch": 1,
            "Academic Year": "2021 - 2025",
            "Total-attendance": 35,
            "Last-attendance-time": "2023-10-13 13:59:00"
        },
    "RA2111026010186":
        {
            "Name": "Arcot Raghunath Rao",
            "id": "RA2111026010186",
            "Department": "CINTEL",
            "Section": "W1",
            "Batch": 1,
            "Academic Year": "2021 - 2025",
            "Total-attendance": 28,
            "Last-attendance-time": "2023-10-13 13:59:00"
        },
    "RA2111026010190":
        {
            "Name": "Adepu Gautham",
            "id": "RA2111026010190",
            "Department": "CINTEL",
            "Section": "W1",
            "Batch": 1,
            "Academic Year": "2021 - 2025",
            "Total-attendance": 29,
            "Last-attendance-time": "2023-10-13 13:59:00"
        },
    "RA2111026010204":
        {
            "Name": "S Sainadh",
            "id": "RA2111026010204",
            "Department": "CINTEL",
            "Section": "W1",
            "Batch": 1,
            "Academic Year": "2021 - 2025",
            "Total-attendance": 30,
            "Last-attendance-time": "2023-10-13 13:59:00"
        },
    "RA2111003011611":
        {
            "Name": "Krishna Chaitanya",
            "id": "RA2111003011611",
            "Department": "CTECH",
            "Section": "J2",
            "Batch": 2,
            "Academic Year": "2021 - 2025",
            "Total-attendance": 38,
            "Last-attendance-time": "2023-10-13 13:59:00"
        },
}
# sending data, unzipping dictnaries in python

for key, value in data.items():
    ref.child(key).set(value)
