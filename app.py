from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

app = Flask(__name__)

# ใส่ Token และ Secret ที่ได้จาก Line Developers
CHANNEL_ACCESS_TOKEN = "afP4lIE/ENRuXqNOAQoYULu2AHDPLBoMZfwK/RqlMmF2RTnaKBWCOa9vV9uA/qJxnfchUKUTWr60sUd5y6QvgxJ7HOVLKbQJBlX1atO8gLXzmqZNNUVaXWA6uIkqHmG4EbbvFEQORoDyohs+TgXiBwdB04t89/1O/w1cDnyilFU="
CHANNEL_SECRET = "1b3e9047b351df082ee16ca9724a5f8f"

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/", methods=['GET'])
def home():
    return "Line Bot BMI Calculator is running!"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except Exception as e:
        print(f"Error: {e}")
    return "OK", 200

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_text = event.message.text.strip()
    
    try:
        weight, height = map(float, user_text.split())
        bmi = weight / (height / 100) ** 2
        if bmi < 18.5:
            result = "คุณมีน้ำหนักน้อย ควรเพิ่มสารอาหารและออกกำลังกายเพิ่มกล้ามเนื้อ"
        elif 18.5 <= bmi < 22.9:
            result = "คุณมีน้ำหนักปกติ รักษาสมดุลของคุณต่อไป"
        elif 23.0 <= bmi < 24.9:
            result = "คุณน้ำหนักเกิน ควรลดไขมันลงและออกกำลังกายเพิ่ม"
        elif 25.0 <= bmi < 29.9:
            result = "คุณมีภาวะอ้วนระดับ 1 เสี่ยงเกิดโรค ควรลดไขมันด่วนและออกกำลังกายเพิ่ม"
        else:
            result = "คุณมีภาวะอ้วนระดับ 2 เสี่ยงเกิดโรคร้ายแรง ต้องเปลี่ยนการกิน พักผ่อน ออกกำลังกายทันที"
        
        reply_text = f"ค่า BMI ของคุณคือ {bmi:.2f} ({result})"
    except:
        reply_text = "กรุณาส่งข้อมูลในรูปแบบ: น้ำหนัก(kg) ส่วนสูง(cm) เช่น 70 170"

    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
