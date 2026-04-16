from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json
app = Flask(__name__)
# 1. 初始化 Firebase
if not firebase_admin._apps:
    if os.path.exists("serviceAccountKey.json"):
        cred = credentials.Certificate("serviceAccountKey.json")
    else:
# Vercel 環境變數
        cred_json = json.loads(os.environ.get("SERVICE_ACCOUNT_KEY"))
        cred = credentials.Certificate(cred_json)
firebase_admin.initialize_app(cred)
db = firestore.client()
# 2. 首頁 (顯示兩個連結：電影 + 老師)
@app.route("/")
def home():
# 這裡顯示你的名字：范阮越姜
    homepage = f"<h1>范阮越姜 - 資管管理導論作業</h1>"
    homepage += "<a href=/movie>電影查詢系統 (開眼電影)</a><br><br>"
    homepage += "<a href=/search>老師查詢系統 (靜宜資管)</a><br>"
    return homepage
# 3. 老師查詢功能 (這是作業核心)
@app.route("/search", methods=["GET", "POST"])
def search_teacher():
    result = []
    keyword = ""
    if request.method == "POST":
        keyword = request.form.get("keyword", "").strip()
# 🔥 這裡要對應你截圖的集合名稱！
# 如果你的集合叫「靜宜資管」，就填 "靜宜資管"
    docs = db.collection("靜宜資管").get()

    for doc in docs:
        teacher = doc.to_dict()
# 比對名字 (如果你的欄位不是叫 name，請改回正確的欄位名稱)
        if keyword in teacher.get("name", ""):
            result.append(teacher)
# 渲染頁面，帶入資料
    return render_template("search.html", keyword=keyword, results=result)
# 4. 電影功能 (保持不變，讓你原本的專案能運行)
@app.route("/movie")
def movie():
# 這裡放你原本的電影爬蟲程式碼即可
    return "電影功能運行中"
if __name__ == "__main__":
    app.run(debug=True)