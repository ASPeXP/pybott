HasFeverQuestion = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
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
          "text": "Diagonos Question 1",
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
              "type": "text",
              "text": "ข้อที่ 1",
              "size": "sm",
              "color": "#0428F2"
            },
            {
              "type": "text",
              "text": "ท่านมีอาการไข้ขึ้นสูงหรือไม่คะ?",
              "size": "md",
              "weight": "bold"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "lg",
              "margin": "xxl",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ไม่มีอาการ",
                    "text": "0"
                  },
                  "flex": 1,
                  "color": "#F5F5F9",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อยมาก",
                    "text": "1"
                  },
                  "flex": 1,
                  "color": "#C9C9F0",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "lg",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อย",
                    "text": "2"
                  },
                  "flex": 1,
                  "color": "#4E50D2",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ปานกลาง",
                    "text": "3"
                  },
                  "flex": 1,
                  "color": "#1F22D9",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "lg",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มาก",
                    "text": "4"
                  },
                  "flex": 1,
                  "color": "#1518B0",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มากที่สุด",
                    "text": "5"
                  },
                  "flex": 1,
                  "color": "#0D0F8C",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "text",
              "text": "กรุณากรอกข้อมูลตามความเป็นจริงนะคะ",
              "flex": 1,
              "margin": "sm",
              "size": "xs",
              "align": "end",
              "wrap": True
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
}

hasCoughtQuestion = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
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
          "text": "Diagonos Question 2",
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
              "type": "text",
              "text": "ข้อที่ 2",
              "size": "sm",
              "color": "#0428F2"
            },
            {
              "type": "text",
              "text": "ท่านมีอาการไอแห้งหรือไม่คะ?",
              "size": "md",
              "weight": "bold"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "lg",
              "margin": "xxl",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ไม่มีอาการ",
                    "text": "0"
                  },
                  "flex": 1,
                  "color": "#F5F5F9",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อยมาก",
                    "text": "1"
                  },
                  "flex": 1,
                  "color": "#C9C9F0",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "lg",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อย",
                    "text": "2"
                  },
                  "flex": 1,
                  "color": "#4E50D2",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ปานกลาง",
                    "text": "3"
                  },
                  "flex": 1,
                  "color": "#1F22D9",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "lg",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มาก",
                    "text": "4"
                  },
                  "flex": 1,
                  "color": "#1518B0",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มากที่สุด",
                    "text": "5"
                  },
                  "flex": 1,
                  "color": "#0D0F8C",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "text",
              "text": "กรุณากรอกข้อมูลตามความเป็นจริงนะคะ",
              "flex": 1,
              "margin": "sm",
              "size": "xs",
              "align": "end",
              "wrap": True
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
}

hasSorThroatQuestion = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
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
          "text": "Diagonos Question 3",
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
              "type": "text",
              "text": "ข้อที่ 3",
              "size": "sm",
              "color": "#0428F2"
            },
            {
              "type": "text",
              "text": "ท่านมีอาการเจ็บคอหรือไม่คะ?",
              "size": "md",
              "weight": "bold"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "lg",
              "margin": "xxl",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ไม่มีอาการ",
                    "text": "0"
                  },
                  "flex": 1,
                  "color": "#F5F5F9",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อยมาก",
                    "text": "1"
                  },
                  "flex": 1,
                  "color": "#C9C9F0",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "lg",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อย",
                    "text": "2"
                  },
                  "flex": 1,
                  "color": "#4E50D2",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ปานกลาง",
                    "text": "3"
                  },
                  "flex": 1,
                  "color": "#1F22D9",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "lg",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มาก",
                    "text": "4"
                  },
                  "flex": 1,
                  "color": "#1518B0",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มากที่สุด",
                    "text": "5"
                  },
                  "flex": 1,
                  "color": "#0D0F8C",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "text",
              "text": "กรุณากรอกข้อมูลตามความเป็นจริงนะคะ",
              "flex": 1,
              "margin": "sm",
              "size": "xs",
              "align": "end",
              "wrap": True
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
}

hasMucusQuestion = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
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
          "text": "Diagonos Question 4",
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
              "type": "text",
              "text": "ข้อที่ 4",
              "size": "sm",
              "color": "#0428F2"
            },
            {
              "type": "text",
              "text": "ท่านมีอาการน้ำมูกไหลหรือไม่คะ?",
              "size": "md",
              "weight": "bold"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "lg",
              "margin": "xxl",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ไม่มีอาการ",
                    "text": "0"
                  },
                  "flex": 1,
                  "color": "#F5F5F9",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อยมาก",
                    "text": "1"
                  },
                  "flex": 1,
                  "color": "#C9C9F0",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "lg",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อย",
                    "text": "2"
                  },
                  "flex": 1,
                  "color": "#4E50D2",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ปานกลาง",
                    "text": "3"
                  },
                  "flex": 1,
                  "color": "#1F22D9",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "lg",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มาก",
                    "text": "4"
                  },
                  "flex": 1,
                  "color": "#1518B0",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มากที่สุด",
                    "text": "5"
                  },
                  "flex": 1,
                  "color": "#0D0F8C",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "text",
              "text": "กรุณากรอกข้อมูลตามความเป็นจริงนะคะ",
              "flex": 1,
              "margin": "sm",
              "size": "xs",
              "align": "end",
              "wrap": True
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
}

hasGaspQuestion = {
  "type": "flex",
  "altText": "Flex Message",
  "contents": {
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
          "text": "Diagonos Question 5",
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
              "type": "text",
              "text": "ข้อที่ 5",
              "size": "sm",
              "color": "#0428F2"
            },
            {
              "type": "text",
              "text": "ท่านมีอาการเหนื่อยหอบหรือไม่คะ?",
              "size": "md",
              "weight": "bold"
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "lg",
              "margin": "xxl",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ไม่มีอาการ",
                    "text": "0"
                  },
                  "flex": 1,
                  "color": "#F5F5F9",
                  "height": "sm",
                  "style": "secondary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อยมาก",
                    "text": "1"
                  },
                  "flex": 1,
                  "color": "#C9C9F0",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "lg",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "น้อย",
                    "text": "2"
                  },
                  "flex": 1,
                  "color": "#4E50D2",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "ปานกลาง",
                    "text": "3"
                  },
                  "flex": 1,
                  "color": "#1F22D9",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "box",
              "layout": "horizontal",
              "spacing": "xl",
              "margin": "lg",
              "contents": [
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มาก",
                    "text": "4"
                  },
                  "flex": 1,
                  "color": "#1518B0",
                  "height": "sm",
                  "style": "primary"
                },
                {
                  "type": "button",
                  "action": {
                    "type": "message",
                    "label": "มากที่สุด",
                    "text": "5"
                  },
                  "flex": 1,
                  "color": "#0D0F8C",
                  "height": "sm",
                  "style": "primary"
                }
              ]
            },
            {
              "type": "text",
              "text": "กรุณากรอกข้อมูลตามความเป็นจริงนะคะ",
              "flex": 1,
              "margin": "sm",
              "size": "xs",
              "align": "end",
              "wrap": True
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
}