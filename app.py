from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import os

# ตั้งค่า Flask app
app = Flask(__name__)

# ใส่ Token และ Secret ที่ได้จาก Line Developers
CHANNEL_ACCESS_TOKEN = "your_channel_access_token"
CHANNEL_SECRET = "your_channel_secret"

# สร้าง instance ของ LineBotApi และ WebhookHandler
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

@app.route("/", methods=['GET'])
def home():
    """
    หน้าเว็บหลักที่ตอบกลับข้อความเมื่อมีการเข้าถึง
    ใช้สำหรับตรวจสอบว่า Flask app ทำงานหรือไม่
    """
    return "Line Bot BMI Calculator is running!"

@app.route("/callback", methods=['POST'])
def callback():
    """
    Webhook ที่รับการส่งข้อมูลจาก LINE server
    ใช้ handle ข้อมูลที่มาจาก LINE Platform เช่น ข้อความที่ผู้ใช้ส่งมา
    """
    signature = request.headers['X-Line-Signature']  # รับค่า signature ที่แนบมาจาก LINE
    body = request.get_data(as_text=True)  # รับข้อมูลที่ส่งมาจาก LINE
    
    try:
        handler.handle(body, signature)  # ส่งข้อมูลไปให้ handler ของ LINE
    except Exception as e:
        print(f"Error: {e}")  # ถ้ามีข้อผิดพลาดให้แสดงใน log
    return "OK", 200  # ส่งกลับสถานะ OK เมื่อเสร็จสิ้นการประมวลผล

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    """
    ฟังก์ชั่นที่ใช้รับข้อความจากผู้ใช้ และคำนวณค่า BMI
    ถ้าผู้ใช้ส่งข้อมูลผิดรูปแบบจะมีข้อความแนะนำให้ส่งใหม่
    """
    user_text = event.message.text.strip()  # รับข้อความจากผู้ใช้และลบช่องว่างที่ไม่จำเป็น

    try:
        # พยายามแปลงข้อความเป็นน้ำหนักและส่วนสูง
        weight, height = map(float, user_text.split())  # แยกน้ำหนักและส่วนสูงจากข้อความ
        bmi = weight / (height / 100) ** 2  # คำนวณ BMI ตามสูตร
        
        # แสดงผลลัพธ์ที่แตกต่างกันตามค่า BMI
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
        
        # ส่งข้อความกลับไปยังผู้ใช้
        reply_text = f"ค่า BMI ของคุณคือ {bmi:.2f} ({result})"
    except ValueError:
        # ถ้าผู้ใช้กรอกข้อมูลผิดพลาดหรือไม่สามารถแปลงเป็นตัวเลขได้
        reply_text = "กรุณาส่งข้อมูลในรูปแบบ: น้ำหนัก(kg) ส่วนสูง(cm) เช่น 70 170"
    except Exception as e:
        # กรณีที่เกิดข้อผิดพลาดอื่น ๆ
        reply_text = f"เกิดข้อผิดพลาด: {str(e)}"
    
    # ส่งข้อความที่คำนวณได้กลับไปยังผู้ใช้
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))

if __name__ == "__main__":
    """
    เริ่มต้นการทำงานของ Flask app และเปิดใช้งาน server
    ในกรณีที่ใช้ ngrok จะต้องให้ ngrok แสดง URL ที่สามารถเข้าถึงจากภายนอกได้
    """
    app.run(port=5000, debug=True)
