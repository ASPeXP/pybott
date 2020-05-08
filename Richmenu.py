richdata = {
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": True,
  "name": "Rich Menu 1",
  "chatBarText": "เมนูหลัก",
  "areas": [
    {
      "bounds": {
        "x": 52,
        "y": 42,
        "width": 1538,
        "height": 788
      },
      "action": {
        "type": "message",
        "text": "เริ่มบันทึกอาการป่วย"
      }
    },
    {
      "bounds": {
        "x": 1642,
        "y": 47,
        "width": 801,
        "height": 774
      },
      "action": {
        "type": "message",
        "text": "สรุปรายงานอาการของท่าน"
      }
    },
    {
      "bounds": {
        "x": 52,
        "y": 873,
        "width": 736,
        "height": 717
      },
      "action": {
        "type": "message",
        "text": "ข้อมูลผู้ติดเชื้อวันนี้"
      }
    },
    {
      "bounds": {
        "x": 821,
        "y": 868,
        "width": 745,
        "height": 722
      },
      "action": {
        "type": "message",
        "text": "ข้อมูลผู้ติดเชื้อตามพื้นที่"
      }
    },
    {
      "bounds": {
        "x": 1637,
        "y": 873,
        "width": 821,
        "height": 717
      },
      "action": {
        "type": "message",
        "text": "สรุปข้อมูลอาการจากผู้ใช้งานทั้งหมด"
      }
    }
  ]
}


from config import Channel_access_token #
channel_access_token = Channel_access_token
Image_File_Path = "./Material//richmenu.png"
import json

import requests



def RegisRich(Rich_json,channel_access_token):

    url = 'https://api.line.me/v2/bot/richmenu'

    Rich_json = json.dumps(Rich_json)

    Authorization = 'Bearer {}'.format(channel_access_token)


    headers = {'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': Authorization}

    response = requests.post(url,headers = headers , data = Rich_json)

    print(str(response.json()['richMenuId']))

    return str(response.json()['richMenuId'])

def CreateRichMenu(ImageFilePath,Rich_json,channel_access_token):


    richId = RegisRich(Rich_json = Rich_json,channel_access_token = channel_access_token)

    url = ' https://api.line.me/v2/bot/richmenu/{}/content'.format(richId)

    Authorization = 'Bearer {}'.format(channel_access_token)

    headers = {'Content-Type': 'image/jpeg',
    'Authorization': Authorization}

    img = open(ImageFilePath,'rb').read()

    response = requests.post(url,headers = headers , data = img)

    print(response.json())


CreateRichMenu(ImageFilePath=Image_File_Path,Rich_json=richdata,channel_access_token=channel_access_token)