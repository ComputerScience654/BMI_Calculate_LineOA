# BMI_Calculate_LineOA

## Project Title
การพัฒนาระบบคำนวณค่า BMI ผ่าน Line Official Account

## Objective
เพื่อให้ผู้ใช้งานสามารถคำนวณค่า BMI (Body Mass Index) พร้อมรับคำแนะนำสุขภาพเบื้องต้นผ่านการสนทนาใน Line Official Account

## Scope of Work
### การสร้างและตั้งค่า Line Official Account (Line OA)
- สร้างบัญชี Line Official Account เพื่อใช้เป็นช่องทางการติดต่อกับผู้ใช้
- ตั้งค่า Messaging API และเปิดใช้งาน Webhook เพื่อเชื่อมต่อกับระบบเซิร์ฟเวอร์

### การพัฒนาระบบ Webhook Server
- พัฒนา Webhook Server โดยใช้ภาษา Python และไลบรารี Flask เพื่อรับ-ส่งข้อมูลระหว่าง Line OA และผู้ใช้งาน
- เชื่อมต่อ Webhook Server กับ Line OA ผ่าน Ngrok เพื่อเผยแพร่ URL ชั่วคราวในระหว่างการพัฒนา

### ฟังก์ชันการคำนวณ BMI
- รับข้อมูล น้ำหนัก(กิโลกรัม) และ ส่วนสูง(เซนติเมตร) จากผู้ใช้งานผ่านข้อความ
- คำนวณค่า BMI ตามสูตร
- แสดงผลค่า BMI พร้อมคำแนะนำสุขภาพเบื้องต้น

## Project Duration
เริ่มต้น วันที่ 1 มกราคม 2568 สิ้นสุด วันที่ 31 มีนาคม 2568

## Budget
งบประมาณรวม 1,000-2,000 บาท

## Stakeholders
- นายปัญจพล รัตนประเสริฐ  
  รหัสนักศึกษา: CSS46541N 465415241006

## Expected Outcomes
- ผู้ใช้สามารถรับรู้ค่า BMI ของตนเองได้ และได้รับรู้คำแนะนำหลังการคำนวณค่า BMI

## Technical Requirements

### ซอฟต์แวร์และเครื่องมือ
- **Python เวอร์ชัน 3.8 ขึ้นไป**
- ไลบรารี Python:
  - `Flask` สำหรับสร้าง Webhook Server
  - `line-bot-sdk` สำหรับเชื่อมต่อกับ Line Messaging API
  - `Ngrok` สำหรับเผยแพร่ URL ของ Webhook ในระหว่างการพัฒนา
- **Text Editor/IDE** เช่น VS Code, PyCharm

### ระบบปฏิบัติการ
- **Windows** (รองรับการติดตั้ง Python และ Ngrok)

### บัญชีผู้ใช้งาน
- บัญชี **Line** สำหรับการสร้าง Line Official Account
- บัญชี **Line Developers Console** เพื่อจัดการ Messaging API

### การเชื่อมต่ออินเทอร์เน็ต
- การเข้าถึงอินเทอร์เน็ตที่เสถียรสำหรับการทำงานของ Webhook และการเชื่อมต่อ Line API

### การตั้งค่า Webhook
- Channel Access Token และ Channel Secret จาก **Line Developers Console**
- URL สำหรับ Webhook (จาก Ngrok หรือเซิร์ฟเวอร์ที่รองรับ HTTPS)

### ฮาร์ดแวร์
- คอมพิวเตอร์ที่สามารถรองรับการติดตั้ง Python และไลบรารีที่เกี่ยวข้อง
- พื้นที่เก็บข้อมูลขั้นต่ำ 500MB สำหรับไลบรารีและการพัฒนา

## ขั้นตอนการติดตั้ง

### 1. **ติดตั้ง Python**
ก่อนอื่น คุณต้องติดตั้ง Python เวอร์ชัน 3.8 ขึ้นไป:
- ดาวน์โหลด Python จาก [https://www.python.org/downloads/](https://www.python.org/downloads/)
- ติดตั้ง Python และตรวจสอบว่าคุณได้เลือกเพิ่ม Python ใน PATH ระหว่างการติดตั้ง

หลังจากติดตั้งเสร็จแล้ว ให้ตรวจสอบเวอร์ชัน Python ด้วยคำสั่งใน terminal หรือ command prompt:
```bash
python --version
```

### 2. **ติดตั้งไลบรารีที่จำเป็น**
ในขั้นตอนนี้ คุณต้องติดตั้งไลบรารีที่ใช้ในโปรเจกต์โดยใช้คำสั่ง pip:
1. เปิด terminal หรือ command prompt
2. รันคำสั่งนี้ในโฟลเดอร์ที่เก็บไฟล์โปรเจกต์:
```bash
pip install Flask line-bot-sdk
```

### 3. **ติดตั้ง Ngrok**
Ngrok ใช้เพื่อเผยแพร่ URL ของ Webhook Server ที่รันในเครื่องของคุณ เพื่อเชื่อมต่อกับ Line API:
1. ดาวน์โหลด Ngrok จาก [https://ngrok.com/download](https://ngrok.com/download)
2. ติดตั้งและเปิด terminal หรือ command prompt
3. รันคำสั่งต่อไปนี้เพื่อเชื่อมต่อ Ngrok กับ Webhook ของคุณ:
```bash
ngrok http 5000
```
- จะได้รับ URL ของ Webhook ที่จะใช้ในการตั้งค่าใน Line Developers Console เช่น `http://<ngrok_subdomain>.ngrok.io`

### 4. **ตั้งค่าบัญชี Line Official Account**
1. เข้าไปที่ [Line Developers Console](https://developers.line.biz/)
2. ลงทะเบียนและสร้าง **Line Official Account**
3. เปิดใช้งาน **Messaging API** และบันทึกข้อมูล **Channel Access Token** และ **Channel Secret**

### 5. **ตั้งค่าในโค้ด**
1. เปิดไฟล์ `app.py`
2. แทนที่ค่า `CHANNEL_ACCESS_TOKEN` และ `CHANNEL_SECRET` ด้วยข้อมูลที่ได้จาก **Line Developers Console**:
   ```python
   CHANNEL_ACCESS_TOKEN = "your_channel_access_token"
   CHANNEL_SECRET = "your_channel_secret"
   ```

### 6. **รัน Webhook Server**
1. เปิด terminal หรือ command prompt ในโฟลเดอร์โปรเจกต์
2. รันคำสั่งนี้เพื่อเริ่มต้น Webhook Server:
```bash
python app.py
```
- เซิร์ฟเวอร์จะเริ่มทำงานที่พอร์ต 5000

### 7. **ตั้งค่า Webhook URL ใน Line Developers Console**
1. กลับไปที่ **Line Developers Console**
2. ไปที่เมนู **Messaging API** และกรอก URL ของ Webhook (ที่ได้จาก Ngrok) ในช่อง **Webhook URL**:
   - เช่น `http://<ngrok_subdomain>.ngrok.io/callback`

### 8. **ทดสอบการทำงาน**
- เปิด **Line** และค้นหาบัญชี **Line Official Account** ที่คุณสร้างขึ้น
- ส่งข้อความที่มีรูปแบบเป็น "น้ำหนัก(กิโลกรัม) ส่วนสูง(เซนติเมตร)" เช่น "70 170"
- ระบบจะคำนวณค่า BMI และส่งผลลัพธ์กลับไปให้ผู้ใช้พร้อมคำแนะนำสุขภาพ

---

## ขั้นตอนการใช้งาน
- **การส่งข้อมูล**: เมื่อผู้ใช้ส่งข้อความในรูปแบบ "น้ำหนัก(กิโลกรัม) ส่วนสูง(เซนติเมตร)" เช่น "70 170"
- **การคำนวณ BMI**: ระบบจะคำนวณค่า BMI และแสดงผลลัพธ์ พร้อมคำแนะนำ
  - หาก BMI ต่ำกว่า 18.5 → คำแนะนำ: เพิ่มน้ำหนัก
  - หาก BMI อยู่ในช่วง 18.5 - 22.9 → คำแนะนำ: น้ำหนักปกติ
  - หาก BMI อยู่ในช่วง 23.0 - 24.9 → คำแนะนำ: น้ำหนักเกิน
  - หาก BMI อยู่ในช่วง 25.0 - 29.9 → คำแนะนำ: อ้วนระดับ 1
  - หาก BMI มากกว่า 30 → คำแนะนำ: อ้วนระดับ 2

---

## ข้อกำหนดทางเทคนิค
- **Python 3.8 หรือสูงกว่า**
- **Flask** และ **line-bot-sdk** สำหรับเชื่อมต่อกับ Line API
- **Ngrok** สำหรับเผยแพร่ Webhook URL
- ระบบปฏิบัติการ **Windows** หรือ **Linux**
- การเชื่อมต่ออินเทอร์เน็ตที่เสถียร

