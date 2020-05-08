from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from FlexMessage.QuestionMsg import *
from FlexMessage.ResultMsg import *

#coding: utf-8
from BasicFunction.COVID_ANALYZER import analyze_covid_from_user 
from firebase import firebase
from BasicFunction.firebase_db_connect import get, get_daily_tracking, post, post_daily_tracking, update, update_daily_tracking, delete 
from config import Firebase_DB_url
#Firebase_DB_url = "https://pybott-6th-c90ed.firebaseio.com/" # Your firebase Application
firebase = firebase.FirebaseApplication(Firebase_DB_url, None)
DB_COV_TRACKER = "COV_TRACKER"
DB_USER_SESSION= "USER_SESSION"
DB_USER_DATA = "USER_DATA"

from config import Channel_access_token, Channel_secret

app = Flask(__name__)

line_bot_api = LineBotApi(Channel_access_token)
handler = WebhookHandler(Channel_secret)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    REPLY_TOKEN = event.reply_token
    MESSAGE_FROM_USER = event.message.text
    UID = event.source.user_id

    #get user id
    profile = line_bot_api.get_profile(UID)
    DISPLAY_NAME = profile.display_name 
    PROFILE_PIC = profile.picture_url

    #check user in system?
    user = get(uid=UID, firebase_app=firebase, database_name=DB_USER_DATA)
    if not user:
        #continue
        print(user)
        data = {"session": "None"}

        #create user session
        post(uid=UID, data=data, firebase_app=firebase, database_name=DB_USER_SESSION )

        data = {"display_name": DISPLAY_NAME, "profile_pic": PROFILE_PIC}
        post(uid=UID, data=data, firebase_app=firebase, database_name=DB_USER_DATA)

    user_session = get(uid=UID, firebase_app=firebase, database_name=DB_USER_SESSION)
    user_session = user_session["session"]

    print (user_session)

    if user_session == "None":

        if MESSAGE_FROM_USER == "เริ่มบันทึกอาการป่วย" :

            daily_report = {
            "has_fever": "",
            "has_cough": "" ,
            "has_sore_throat": "",
            "has_mucus": "",
            "has_disp": "",
            "check_date": "",
            "score": 0,
            "suggestion": "",
            "other_symptom":""
            }

            # create user daily report
            post_daily_tracking(uid=UID, data=daily_report, firebase_app=firebase, database_name=DB_COV_TRACKER)

            session_data = {"session": "บันทึกอาการไข้"}
            update(uid=UID, new_data=session_data, firebase_app=firebase, database_name=DB_USER_SESSION)

            ## response กลับไปที่ห้อง Chat
            bubble = Base.get_or_new_from_json_dict(data=HasFeverQuestion, cls=FlexSendMessage)
            line_bot_api.reply_message(REPLY_TOKEN, bubble)
    else:
        ### func อื่น ๆ
        if user_session == "บันทึกอาการไข้":

            if MESSAGE_FROM_USER in ["0", "1","2","3","4","5"]:
                data = {"has_fever": MESSAGE_FROM_USER }
                update_daily_tracking(uid=UID, new_data=data, firebase_app=firebase, database_name=DB_COV_TRACKER)

                session_data = {"session": "บันทึกอาการไอ"}
                update(uid=UID, new_data= session_data, firebase_app=firebase, database_name=DB_USER_SESSION) #update

                print(hasCoughtQuestion)

                bubble = Base.get_or_new_from_json_dict(data=hasCoughtQuestion, cls=FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN, bubble)

            else:
                line_bot_api.reply_message(REPLY_TOKEN, TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นค่ะ (พิมพ์เลข 1-5"))

        elif user_session == "บันทึกอาการไอ":

            if MESSAGE_FROM_USER in ["0", "1","2","3","4","5"]:
                data = {"has_cough": MESSAGE_FROM_USER }
                update_daily_tracking(uid=UID, new_data=data, firebase_app=firebase, database_name=DB_COV_TRACKER)

                session_data = {"session": "บันทึกอาการเจ็บคอ"}
                update(uid=UID, new_data= session_data, firebase_app=firebase, database_name=DB_USER_SESSION)
                bubble = Base.get_or_new_from_json_dict(data=hasSorThroatQuestion, cls=FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN, bubble)

            else:
                line_bot_api.reply_message(REPLY_TOKEN, TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นค่ะ (พิมพ์เลข 1-5"))

        elif user_session == "บันทึกอาการเจ็บคอ":

            if MESSAGE_FROM_USER in ["0", "1","2","3","4","5"]:
                data = {"has_sore_throat": MESSAGE_FROM_USER}
                update_daily_tracking(uid=UID, new_data=data, firebase_app=firebase, database_name=DB_COV_TRACKER)

                session_data = {"session": "บันทึกอาการน้ำมูกไหล"}
                update(uid=UID, new_data= session_data, firebase_app=firebase, database_name=DB_USER_SESSION)

                bubble = Base.get_or_new_from_json_dict(data=hasMucusQuestion, cls=FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN, bubble)

            else:
                line_bot_api.reply_message(REPLY_TOKEN, TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นค่ะ (พิมพ์เลข 1-5"))

        elif user_session == "บันทึกอาการน้ำมูกไหล":

            if MESSAGE_FROM_USER in ["0", "1","2","3","4","5"]:
                data = {"has_mucus": MESSAGE_FROM_USER}
                update_daily_tracking(uid=UID, new_data=data, firebase_app=firebase, database_name=DB_COV_TRACKER)

                session_data = {"session": "บันทึกอาการเหนื่อยหอบ"}
                update(uid=UID, new_data= session_data , firebase_app=firebase, database_name=DB_USER_SESSION)
                bubble = Base.get_or_new_from_json_dict(data=hasGaspQuestion, cls=FlexSendMessage)
                line_bot_api.reply_message(REPLY_TOKEN, bubble)

            else:
                line_bot_api.reply_message(REPLY_TOKEN, TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นค่ะ (พิมพ์เลข 1-5"))

        elif user_session == "บันทึกอาการเหนื่อยหอบ":

            if MESSAGE_FROM_USER in ["0", "1","2","3","4","5"]:
                data = {"has_disp": MESSAGE_FROM_USER }
                update_daily_tracking(uid=UID, new_data=data, firebase_app=firebase, database_name=DB_COV_TRACKER)

                session_data = {"session": "บันทึกอาการอื่น ๆ ที่พบ"}
                update(uid=UID, new_data=session_data, firebase_app=firebase, database_name=DB_USER_SESSION)
              
                # user_daily_data = get_daily_tracking(uid=UID, firebase_app=firebase, database_name=DB_COV_TRACKER)
                # result = analyze_covid_from_user(user_daily_data)
              
                # post_daily_tracking(uid=UID, data=result, firebase_app=firebase, database_name=DB_COV_TRACKER)
                qBtn1 = QuickReplyButton(image_url="", action=MessageAction(label="ไม่มี", text="ไม่มี"))
                qBtn2 = QuickReplyButton(image_url="", action=MessageAction(label="มี", text="มี"))
                qRep = QuickReply(items=[qBtn1, qBtn2])
                line_bot_api.reply_message(REPLY_TOKEN, TextSendMessage("เรียบร้อยแล้วค่ะ ท่านมีอาหารอื่นเพิ่มเติมอีกไหมคะ" + "\n" , quick_reply=qRep))
            else:
                line_bot_api.reply_message(REPLY_TOKEN, TextSendMessage("กรุณาระบุเป็นตัวเลขเท่านั้นค่ะ (พิมพ์เลข 1-5"))

        elif user_session == "บันทึกอาการอื่น ๆ ที่พบ":
    
            data = {"other_symptom": MESSAGE_FROM_USER }
            update_daily_tracking(uid=UID, new_data=data, firebase_app=firebase, database_name=DB_COV_TRACKER)

            session_data = {"session": "None"}
            update(uid=UID, new_data=session_data, firebase_app=firebase, database_name=DB_USER_SESSION)
            
            user_daily_data = get_daily_tracking(uid=UID, firebase_app=firebase, database_name=DB_COV_TRACKER)
            result = analyze_covid_from_user(user_daily_data)
            
            post_daily_tracking(uid=UID, data=result, firebase_app=firebase, database_name=DB_COV_TRACKER)

            raw_bubble = GenerateREsultMsg(profile_name=DISPLAY_NAME, UserId=UID, Dict_daily_data=result)   
            bubble = Base.get_or_new_from_json_dict(raw_bubble, FlexSendMessage)     

            line_bot_api.reply_message(REPLY_TOKEN, bubble)



@handler.add(FollowEvent)
def handler_Follow(event):
    USER_ID = event.source.user_id
    REPLY_TOKEN = event.reply_token
   

    line_bot_api.link_rich_menu_to_user(user_id=USER_ID,
                            rich_menu_id="richmenu-f2a34fac71f671e662141a56ff997668")


    image_message = ImageSendMessage(

        original_content_url="https://image.bangkokbiznews.com/kt/media/image/news/2020/03/07/869597/750x422_869597_1583517761.png",
        preview_image_url="https://image.bangkokbiznews.com/kt/media/image/news/2020/03/07/869597/750x422_869597_1583517761.png"
    )

    qbtn1 = QuickReplyButton(image_url="https://image.bangkokbiznews.com/kt/media/image/news/2020/03/07/869597/750x422_869597_1583517761.png", 
                    action=MessageAction(label="เริ่มบันทึกอาการป่วย", text="เริ่มบันทึกอาการป่วย"))

    qbtn2 = QuickReplyButton(image_url="https://image.bangkokbiznews.com/kt/media/image/news/2020/03/07/869597/750x422_869597_1583517761.png", 
                    action=MessageAction(label="วันนี้เป็นไงบ้าง", text="วันนี้เป็นไงบ้าง"))


    qrep = QuickReply(items=[qbtn1, qbtn2])
    text_message = TextSendMessage(text="ยินดีต้อนรับเข้าสู่ บันทึกของผู้กักตัว", quick_reply=qrep)

    line_bot_api.reply_message(REPLY_TOKEN, messages=[image_message, text_message])

@app.route('/showhtml')
def showhtml():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <p>
    <select id="select1"> 
        <option>Select gender</option>
        <option>Male</option>
        <option>Femail</option>
    </select>
    
    </p>
    <code>Flask is <em>awesome</em></code>
    """

if __name__ == "__main__":
    app.run(debug=True)