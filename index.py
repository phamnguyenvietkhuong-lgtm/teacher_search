import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase 初始化
if not firebase_admin._apps:
    if os.path.exists("serviceAccountKey.json"):
        # 本地測試
        cred = credentials.Certificate("serviceAccountKey.json")
    else:
        # Vercel 環境
        service_account_info = os.environ.get("SERVICE_ACCOUNT_KEY")
        if not service_account_info:
            raise ValueError("找不到 SERVICE_ACCOUNT_KEY 環境變數")
        
        # 將字串轉回 JSON 物件
        cred_dict = json.loads(service_account_info)
        cred = credentials.Certificate(cred_dict)
        
    firebase_admin.initialize_app(cred)

db = firestore.client()
