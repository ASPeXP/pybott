# x = 1
# y = 2

# print(x + y)

# x = "pybott1"
# y = "pybott2"

# print(x + y)

# x = [1, 2,3 ,4]

# result = x[1] + x[3]
# print(result)

x = ["pybottครั้งที่ 1","pybootครั้งที่ 2", "pybottครั้งที่ 3"]
y = ['web programming','chatbot','network']
# ครั้งที่_1 = x[0]

# for valuex, valuey in zip(x,y):
#     print(valuex, valuey)
example_dict = {
    "userid": "1",
    "name":"uncle_engineer",
    "country": "usa",
    "address": "bangkok",
    "Infected_Corona_Virus": False
}
from datetime import date 
print(example_dict["userid"] + " : " + example_dict["name"])
today= date.today()
print(today)

#สรุป Database model, DB relationship
# 1 user มีการกรอกได้หลายวัน
# 1 วัน มีข้อมูล _input_has_fever, input_has_cought, _input_has_throat_pain, 
#              _input_has_mucus, _input_has_gasp, วันที่, score

dic_day1 = {
    "มีไข้": True,
    "มีอาการไอ": True ,
    "มีอาการเจ็บคอ": True,
    "น้ำมูลไหบ": True,
    "เหนื่อยหอบ": True,
    "วันที่": "2020-04-04",
    "score": 100
}

dic_day2 = {
    "มีไข้": True,
    "มีอาการไอ": True ,
    "มีอาการเจ็บคอ": True,
    "น้ำมูลไหบ": True,
    "เหนื่อยหอบ": False,
    "วันที่": "2020-04-05",
    "score": 80
}
