from datetime import date, datetime

def analyze_covid_from_user(username, current_date_data):


        today = date.today()
        now = datetime.now().strftime("%H:%M:%S")
        #print(now)

        _input_current_date = str(today) + ' ' + str(now)
        print(_input_current_date)
    
        print("สรุปจากผลการตรวจสอบอาการเบื้องต้น พบว่า")
        score = 0

        if current_date_data["has_fever"] == "y":
            score += 20

        if current_date_data["has_cough"] == "y":
            score += 20

        if current_date_data["has_sore_throat"] == "y":
            score += 20

        if current_date_data["has_mucus"] == "y":
            score += 20

        if current_date_data["has_disp"] == "y":
            score += 20

        current_date_data["score"] = score 
        current_date_data["check_date"] = _input_current_date

        print("คุณ " + username)
        if 60 <= score < 100 :
            current_date_data["suggestion"] ="ควรกักตัวอยู่ที่บ้านนะคะ"
            print("ควรกักตัวอยู่ที่บ้านนะคะ")

        elif score == 100:
            current_date_data["suggestion"] ="ควรไปพบแพทย์เดี๋ยวนี้เลยค่ะ"
            print("ควรไปพบแพทย์เดี๋ยวนี้เลยค่ะ")

        else:
            current_date_data["suggestion"] = "ไม่มีอาการสุ่มเสี่ยงต่อเชื้อไวรัส COVID-19"
            print("ไม่มีอาการสุ่มเสี่ยงต่อเชื้อไวรัส COVID-19")

        print("ข้อมูลการตรวจเฝ้าระวังวันที่ " + _input_current_date)
       

        return current_date_data

