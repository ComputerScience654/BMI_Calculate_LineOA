# BMI_Calculate_LineOA

## Project Title
การพัฒนาระบบคำนวณค่า BMI ผ่าน Line Official Account

## Objective
เพื่อให้ผู้ใช้งานสามารถคำนวณค่า BMI (Body Mass Index) พร้อมรับคำแนะนำสุขภาพเบื้องต้นผ่านการสนทนาใน Line Official Account

## Scope of Work
### 1. การสร้างและตั้งค่า Line Official Account (Line OA)
- สร้างบัญชี Line Official Account (Line OA) ผ่าน Line Developers Console
- เลือกประเภทของบัญชี Line OA ที่เหมาะสม (เช่น: "Standard Account" หรือ "Line Business Account")
- ตั้งค่าเบื้องต้นของ Line OA เช่น ชื่อบัญชี, รูปโปรไฟล์, และข้อมูลการติดต่อ
- เปิดใช้งาน **Messaging API** และบันทึกข้อมูลที่สำคัญ ได้แก่ **Channel Access Token** และ **Channel Secret** เพื่อใช้ในการเชื่อมต่อ API
- ตั้งค่า **Webhook URL** ที่จะใช้ในการรับและส่งข้อความระหว่างผู้ใช้กับ Line OA ผ่านเซิร์ฟเวอร์

### 2. การพัฒนาระบบ Webhook Server
- สร้างเซิร์ฟเวอร์ **Webhook** โดยใช้ **Flask Framework** ในภาษา **Python** เพื่อรับคำขอจาก Line OA และส่งข้อมูลตอบกลับ
- ตั้งค่า **Route** สำหรับการรับข้อความจากผู้ใช้ เช่น `POST /callback` ซึ่งจะได้รับข้อมูลจาก Line OA เมื่อผู้ใช้ส่งข้อความ
- การสร้าง **ฟังก์ชันการคำนวณ BMI**:
    - รับข้อมูลน้ำหนัก (กิโลกรัม) และส่วนสูง (เซนติเมตร) จากข้อความที่ผู้ใช้ส่ง
    - คำนวณค่า BMI โดยใช้สูตร: BMI = น้ำหนัก(kg)/ส่วนสูง(m)^2
    - ส่งผลลัพธ์ (ค่า BMI) พร้อมคำแนะนำสุขภาพตามเกณฑ์ที่กำหนด เช่น:
        - BMI ต่ำกว่า 18.5: "เพิ่มน้ำหนัก"
        - BMI ระหว่าง 18.5 - 22.9: "น้ำหนักปกติ"
        - BMI ระหว่าง 23.0 - 24.9: "น้ำหนักเกิน"
        - BMI ระหว่าง 25.0 - 29.9: "อ้วนระดับ 1"
        - BMI มากกว่า 30: "อ้วนระดับ 2"
- ทดสอบฟังก์ชันการคำนวณ BMI ว่าสามารถคำนวณได้ถูกต้องและแสดงคำแนะนำที่เหมาะสมตามค่า BMI

### 3. การเชื่อมต่อกับ Ngrok เพื่อเผยแพร่ Webhook URL
- ติดตั้ง **Ngrok** สำหรับสร้าง **Tunnel** และเผยแพร่ URL ของ Webhook Server
- รันคำสั่ง `ngrok http 5000` เพื่อเปิดเผย URL สำหรับการเชื่อมต่อกับ Line API
- ทดสอบการเชื่อมต่อระหว่าง Ngrok และ Webhook Server ว่าสามารถรับข้อมูลจาก Line OA ได้อย่างถูกต้อง

### 4. การตั้งค่าและเชื่อมต่อกับ Line Messaging API
- เชื่อมต่อ **Webhook Server** กับ Line OA โดยการกรอก **Channel Access Token** และ **Channel Secret** ที่ได้จาก Line Developers Console ในโค้ด Python
- ตั้งค่า **Webhook URL** ที่ได้รับจาก Ngrok ใน Line Developers Console เพื่อให้ระบบสามารถรับข้อมูลจาก Line OA ได้
- ทดสอบการส่งข้อความไปยัง Line OA และตรวจสอบว่าเซิร์ฟเวอร์สามารถตอบกลับได้ถูกต้อง

### 5. การพัฒนาและทดสอบระบบ
- ทดสอบการคำนวณ BMI ด้วยข้อมูลต่างๆ ที่ผู้ใช้ส่งมา เช่น "70 170" หรือ "85 160"
- ทดสอบการตอบกลับข้อความจาก Line OA ว่าสามารถแสดงผลลัพธ์ของ BMI และคำแนะนำได้ถูกต้อง
- ทดสอบระบบในหลายๆ สถานการณ์ เช่น การส่งข้อมูลไม่ครบถ้วน (เช่น แค่ส่งน้ำหนักหรือแค่ส่งส่วนสูง) เพื่อให้แน่ใจว่าแอปพลิเคชันสามารถจัดการข้อผิดพลาดได้ดี

### 6. การทดสอบการใช้งาน
- ทดสอบระบบโดยให้ผู้ใช้ทดลองคำนวณค่า BMI ผ่านการสนทนากับ Line OA และตรวจสอบว่าได้คำแนะนำที่เหมาะสมจากระบบ
  
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
- **Python 3.8 หรือสูงกว่า**
- **Flask** และ **line-bot-sdk** สำหรับเชื่อมต่อกับ Line API
- **Ngrok** สำหรับเผยแพร่ Webhook URL
- ระบบปฏิบัติการ **Windows** หรือ **Linux**
- การเชื่อมต่ออินเทอร์เน็ตที่เสถียร

### บัญชีผู้ใช้งาน
- บัญชี **Line** สำหรับการสร้าง Line Official Account
- บัญชี **Line Developers Console** เพื่อจัดการ Messaging API

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

## วิธีเปิดใช้งาน
[![ดูวิดีโอ](https://img.youtube.com/vi/5kiNomXyzV0/0.jpg)](https://www.youtube.com/watch?v=5kiNomXyzV0)

---

