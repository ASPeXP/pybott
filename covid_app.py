#coding: utf-8
from BasicFunction.COVID_ANALYZER import analyze_covid_from_user 
from firebase import firebase
from BasicFunction.firebase_db_connect import get, post, update, delete 
from config import Firebase_DB_url
#Firebase_DB_url = "https://pybott-6th-c90ed.firebaseio.com/" # Your firebase Application
firebase = firebase.FirebaseApplication(Firebase_DB_url, None)
DB_NAME = "COVID-19-Tracker"

while not input("Press x to Exit : ") == "x":
    print("ยินดีต้อนรับเข้าสู่บริการตรวจคัดกรองไวรัส Covid19 \n คุณควรจะกักตัวหรือไม่")
    _input_name = input("กรุณากรอกชื่อของท่าน : ")
    print("สวัสดีคุณ : " + _input_name)
    _input_has_fever = input("คุณ " + _input_name + " มีไข้สูงกว่า 37.5 องศา หรือไม่? (y/n) : ")
    _input_has_cought = input("ตุณ " + _input_name + " มีอาการไอหรือไม่ (y/n) : ")
    _input_has_throat_pain = input("คุณ " + _input_name + " มีอาการเจ็บคอหรือไม่ (y/n) : " )
    _input_has_mucus = input("คุณ " + _input_name + " มีอาการน้ำมูกไหลหรือไม่ (y/n) : ")
    _input_has_gasp = input("คุณ " + _input_name + " มีอาการเหนือ่ยหอบหรือไม่ (y/n) : ")

    current_date_data = {
        "has_fever": _input_has_fever,
        "has_cough": _input_has_cought ,
        "has_sore_throat": _input_has_throat_pain,
        "has_mucus": _input_has_mucus,
        "has_disp": _input_has_gasp,
        "check_date": "",
        "score": 0,
        "suggestion": ""
    }


    result = analyze_covid_from_user(username=_input_name, current_date_data=current_date_data)

    post(uid=_input_name, 
        data=result, 
        firebase_app=firebase, 
        database_name=DB_NAME)

print("You're exited")