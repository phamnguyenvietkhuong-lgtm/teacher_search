# Firebase 初始化

if not firebase_admin._apps:

# 優先讀取本地 JSON 檔（本地測試用）

	if os.path.exists("serviceAccountKey.json"):

		cred = credentials.Certificate("serviceAccountKey.json")

	else:

# Vercel 環境：讀取環境變數

		service_account_json = os.environ.get("SERVICE_ACCOUNT_KEY")

		if not service_account_json:

			raise ValueError("SERVICE_ACCOUNT_KEY 環境變數未設定")

# 解析 JSON 字串

		import json

		cred = credentials.Certificate(json.loads(service_account_json))

	firebase_admin.initialize_app(cred)