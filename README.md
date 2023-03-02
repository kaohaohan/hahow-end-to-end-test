Hahow End-to-End Test
這是一個使用Selenium和Pytest進行自動化測試的專案。目的是提學習撰寫自動化測試框架，能夠讓使用者進行Hahow網站上的UI測試。

安裝
下載並安裝 Python 3.x：https://www.python.org/downloads/
Clone這個repository到您的本地
安裝相關套件：pip install -r requirements.txt
下載並加入ChromeDriver執行檔到您的環境變數PATH中
執行
在專案的根目錄執行以下指令:

bash
Copy code
pytest test/
專案資訊
UI Test: Selenium
Language: Python 3.9.7
Test Framework: pytest
專案架構
ruby
Copy code
hahow-end-to-end-test/
├── pages/                  # 頁面對象模型
│   ├── __init__.py
│   ├── base_page.py
│   ├── home_page.py
│   └── ...
├── tests/                  # 測試用例
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_purchase.py
│   └── ...
├── utils/                  # 工具
│   ├── __init__.py
│   ├── config.py
│   └── ...
├── .gitignore
├── README.md
├── requirements.txt
└── run_tests.sh            # 自動化測試腳本

