# BMI_Calculate_LineOA
## ชื่อโครงการ (Project Title)
การพัฒนาระบบคำนวณค่า BMI ผ่าน Line Official Account
## วัตถุประสงค์ของโครงการ (Objective)
เพื่อให้ผู้ใช้งานสามารถคำนวณค่า BMI (Body Mass Index) พร้อมรับคำแนะนำสุขภาพเบื้องต้นผ่านการสนทนาใน Line Official Account
## ขอบเขตของงาน (Scope of Work)
1. การสร้างและตั้งค่า Line Official Account (Line OA)
    * สร้างบัญชี Line Official Account เพื่อใช้เป็นช่องทางการติดต่อกับผู้ใช้
    * ตั้งค่า Messaging API และเปิดใช้งาน Webhook เพื่อเชื่อมต่อกับระบบเซิร์ฟเวอร์
2. การพัฒนาระบบ Webhook Server
    * พัฒนา Webhook Server โดยใช้ภาษา Python และไลบรารี Flask เพื่อรับ-ส่งข้อมูลระหว่าง Line OA และผู้ใช้งาน
    * เชื่อมต่อ Webhook Server กับ Line OA ผ่าน Ngrok เพื่อเผยแพร่ URL ชั่วคราวในระหว่างการพัฒนา
3. ฟังก์ชันการคำนวณ BMI
    * รับข้อมูล น้ำหนัก(กิโลกรัม) และ ส่วนสูง(เซนติเมตร) จากผู้ใช้งานผ่านข้อความ
    * คำนวณค่า BMI ตามสูตร
    * แสดงผลค่า BMI พร้อมคำแนะนำสุขภาพเบื้องต้น
## ระยะเวลาโครงการ (Project Duration)
เริ่มต้น วันที่ 1 มกราคม 2568
สิ้นสุด วันที่ 31 มีนาคม 2568
## งบประมาณ (Budget)
งบประมาณรวม 1,000-2,000 บาท
## ผู้รับผิดชอบโครงการ (Stakeholders)
นายปัญจพล รัตนประเสริฐ CSS46541N 465415241006
## ผลลัพธ์ที่คาดหวัง (Expected Outcomes)
ผู้ใช้สามารถรับรู้ค่า BMI ของตนเองได้ และได้รับรู้คำแนะนำหลังการคำนวณค่า BMI
## ข้อกำหนดทางเทคนิค (Technical Requirements)
1. ซอฟต์แวร์และเครื่องมือ
    * Python เวอร์ชัน 3.8 ขึ้นไป
    * ไลบรารี Python
      * Flask สำหรับสร้าง Webhook Server
      * line-bot-sdk สำหรับเชื่อมต่อกับ Line Messaging API
    * Ngrok สำหรับเผยแพร่ URL ของ Webhook ในระหว่างการพัฒนา
    * Text Editor/IDE เช่น VS Code, PyCharm
2. ระบบปฏิบัติการ
    * Windows(รองรับการติดตั้ง Python และ Ngrok)
3. บัญชีผู้ใช้งาน
    * บัญชี Line สำหรับการสร้าง Line Official Account
    * บัญชี Line Developers Console เพื่อจัดการ Messaging API
4. การเชื่อมต่ออินเทอร์เน็ต
    * การเข้าถึงอินเทอร์เน็ตที่เสถียรสำหรับการทำงานของ Webhook และการเชื่อมต่อ Line API
5. การตั้งค่า Webhook
    * Channel Access Token และ Channel Secret จาก Line Developers Console
    * URL สำหรับ Webhook (จาก Ngrok หรือเซิร์ฟเวอร์ที่รองรับ HTTPS)
6. ฮาร์ดแวร์
    * คอมพิวเตอร์ที่สามารถรองรับการติดตั้ง Python และไลบรารีที่เกี่ยวข้อง
    * พื้นที่เก็บข้อมูลขั้นต่ำ 500MB สำหรับไลบรารีและการพัฒนา
