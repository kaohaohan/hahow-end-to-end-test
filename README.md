# Hahow End-to-End Test
這是一個使用Selenium和Pytest進行自動化測試的專案。目的是提學習撰寫自動化測試框架，能夠讓使用者進行Hahow網站上的UI測試。

## 安裝
* Python 3：https://www.python.org/downloads/
* Chrome WebDriver https://chromedriver.chromium.org/downloads
## 執行
```js
  git clone https://github.com/kaohaohan/hahow-end-to-end-test.git
cd hahow-end-to-end-test
pip install -r requirements.txt

```

*執行測試

```js
    pytest test/
```

## 專案資訊
* UI Test: Selenium
* Language: Python 3.9.7
* Test Framework: pytest
## 專案架構
```js
hahow-end-to-end-test/
├── pages/                  
│   ├── __init__.py
│   ├── classroom.py       # 課程頁面UI測試
│   ├── home_page.py       # 首頁登入
│   └── course_list_page.py #點擊探索UI測試
├── test/                  # 測試用例
│   ├── __init__.py
│   ├── cookies.json       #cookies 登入需要的cookies
│   ├── test_login.py.     #token 
│   ├── test_browserstack.py #執行程式
├── .gitignore
├── README.md
├── requirements.txt 

```

