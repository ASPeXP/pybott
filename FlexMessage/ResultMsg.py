def GenerateREsultMsg(profile_name , UserId, Dict_daily_data):

    msg = {
    "type": "flex",
    "altText": "Flex Message",
    "contents": {
        "type": "carousel",
        "contents": [
        {
            "type": "bubble",
            "direction": "ltr",
            "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "image",
                "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th-c90ed.appspot.com/o/22648533.png?alt=media&token=3900f68b-d22b-41a4-b9f9-a87046d37be0"
                },
                {
                "type": "text",
                "text": "Diagonos Result",
                "margin": "xl",
                "size": "lg",
                "align": "center",
                "weight": "bold",
                "color": "#FFFFFF"
                }
            ]
            },
            "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                        "type": "text",
                        "text": "ข้อมูลผู้ป่วย",
                        "size": "xl",
                        "align": "center",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": "| ชื่อผู้เข้าตรวจ",
                        "margin": "md",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": "คุณ " + profile_name,
                        "margin": "sm",
                        "align": "start",
                        "weight": "bold"
                        },
                        {
                        "type": "text",
                        "text": "| รหัสผู้ใช้งาน",
                        "margin": "xl",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": UserId,
                        "margin": "sm",
                        "size": "sm",
                        "align": "start",
                        "weight": "bold"
                        },
                        {
                        "type": "text",
                        "text": "| รายงานวันที่",
                        "margin": "xl",
                        "weight": "bold",
                        "color": "#3F72AF"
                        },
                        {
                        "type": "text",
                        "text": Dict_daily_data["check_date"],
                        "margin": "sm",
                        "size": "sm",
                        "align": "start",
                        "weight": "bold"
                        }
                    ]
                    }
                ]
                }
            ]
            },
            "footer": {
            "type": "box",
            "layout": "horizontal",
            "margin": "xl",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "contents": [
                    {
                    "type": "text",
                    "text": "ขอขอบพระคุณเป็นอย่างสูงที่ให้ความร่วมมือกับน้องหมอนะคะ",
                    "margin": "xl",
                    "align": "center",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "wrap": True
                    }
                ]
                }
            ]
            },
            "styles": {
            "header": {
                "backgroundColor": "#3F72AF"
            },
            "footer": {
                "backgroundColor": "#3F72AF"
            }
            }
        },
        {
            "type": "bubble",
            "direction": "ltr",
            "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "image",
                "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th-c90ed.appspot.com/o/22648533.png?alt=media&token=3900f68b-d22b-41a4-b9f9-a87046d37be0"
                },
                {
                "type": "text",
                "text": "Diagonos Result",
                "margin": "xl",
                "size": "lg",
                "align": "center",
                "weight": "bold",
                "color": "#FFFFFF"
                }
            ]
            },
            "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "xxl",
                    "contents": [
                        {
                        "type": "text",
                        "text": "ข้อมูลอาการ",
                        "size": "xl",
                        "align": "center",
                        "weight": "bold",
                        "color": "#3F72AF"
                        }
                    ]
                    },
                    {
                    "type": "box",
                    "layout": "horizontal",
                    "margin": "sm",
                    "contents": [
                        {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 7,
                        "contents": [
                            {
                            "type": "text",
                            "text": "อาการเฝ้าระวัง",
                            "size": "md",
                            "weight": "bold",
                            "color": "#3F72AF"
                            },
                            {
                            "type": "text",
                            "text": "มีไข้สูง",
                            "margin": "lg",
                            "align": "start",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": "ไอแห้ง",
                            "margin": "lg",
                            "align": "start",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": "เจ็บคอ",
                            "margin": "lg",
                            "align": "start",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": "เหนื่อยหอบ",
                            "margin": "lg",
                            "align": "start",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": "น้ำมูกไหล",
                            "margin": "lg",
                            "align": "start",
                            "weight": "bold"
                            }
                        ]
                        },
                        {
                        "type": "box",
                        "layout": "vertical",
                        "flex": 4,
                        "contents": [
                            {
                            "type": "text",
                            "text": "ระดับ(1-5)",
                            "size": "md",
                            "weight": "bold",
                            "color": "#3F72AF"
                            },
                            {
                            "type": "text",
                            "text": Dict_daily_data["has_fever"],
                            "margin": "lg",
                            "align": "center",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": Dict_daily_data["has_cough"],
                            "margin": "lg",
                            "align": "center",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": Dict_daily_data["has_sore_throat"],
                            "margin": "lg",
                            "align": "center",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": Dict_daily_data["has_disp"],
                            "margin": "lg",
                            "align": "center",
                            "weight": "bold"
                            },
                            {
                            "type": "text",
                            "text": Dict_daily_data["has_mucus"],
                            "margin": "lg",
                            "align": "center",
                            "weight": "bold"
                            }
                        ]
                        }
                    ]
                    },
                    {
                    "type": "text",
                    "text": "อาการอื่นๆที่พบ",
                    "margin": "lg",
                    "weight": "bold",
                    "color": "#3F72AF"
                    },
                    {
                    "type": "text",
                    "text": Dict_daily_data["other_symptom"],
                    "margin": "md",
                    "size": "sm",
                    "align": "end",
                    "color": "#707070"
                    }
                ]
                }
            ]
            },
            "footer": {
            "type": "box",
            "layout": "horizontal",
            "margin": "xl",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "contents": [
                    {
                    "type": "text",
                    "text": "ขอขอบพระคุณเป็นอย่างสูงที่ให้ความร่วมมือกับน้องหมอนะคะ",
                    "margin": "xl",
                    "align": "center",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "wrap": True
                    }
                ]
                }
            ]
            },
            "styles": {
            "header": {
                "backgroundColor": "#3F72AF"
            },
            "footer": {
                "backgroundColor": "#3F72AF"
            }
            }
        },
        {
            "type": "bubble",
            "direction": "ltr",
            "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "image",
                "url": "https://firebasestorage.googleapis.com/v0/b/pybott-6th-c90ed.appspot.com/o/22648533.png?alt=media&token=3900f68b-d22b-41a4-b9f9-a87046d37be0"
                },
                {
                "type": "text",
                "text": "Diagonos Result",
                "margin": "xl",
                "size": "lg",
                "align": "center",
                "weight": "bold",
                "color": "#FFFFFF"
                }
            ]
            },
            "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "xxl",
                    "contents": [
                        {
                        "type": "text",
                        "text": "ผลการตรวจ",
                        "size": "xl",
                        "align": "center",
                        "weight": "bold",
                        "color": "#3F72AF"
                        }
                    ]
                    },
                    {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "sm",
                    "contents": [
                        {
                        "type": "text",
                        "text": Dict_daily_data["suggestion"],
                        "size": "sm",
                        "align": "center",
                        "color": "#505050",
                        "wrap": True
                        }
                    ]
                    }
                ]
                }
            ]
            },
            "footer": {
            "type": "box",
            "layout": "horizontal",
            "margin": "xl",
            "contents": [
                {
                "type": "box",
                "layout": "vertical",
                "margin": "xxl",
                "contents": [
                    {
                    "type": "text",
                    "text": "ขอขอบพระคุณเป็นอย่างสูงที่ให้ความร่วมมือกับน้องหมอนะคะ",
                    "margin": "xl",
                    "align": "center",
                    "weight": "bold",
                    "color": "#FFFFFF",
                    "wrap": True
                    }
                ]
                }
            ]
            },
            "styles": {
            "header": {
                "backgroundColor": "#3F72AF"
            },
            "footer": {
                "backgroundColor": "#3F72AF"
            }
            }
        }
        ]
    }
    }

    return msg