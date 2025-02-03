from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import re

def download_pdf(scribd_url):
    # Lấy ID tài liệu từ URL Scribd
    match = re.search(r'/document/(\d+)', scribd_url)
    if not match:
        print("❌ URL Scribd không hợp lệ!")
        return
    scribd_id = match.group(1)
    embed_url = f"https://www.scribd.com/embeds/{scribd_id}/content"
    
    # Cấu hình trình duyệt
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--disable-gpu")  # Tắt GPU để tránh lỗi
    chrome_options.add_argument("--disable-software-rasterizer")  # Tắt rasterizer phần mềm
    chrome_options.add_argument("--disable-dev-shm-usage")  # Giảm sử dụng bộ nhớ chia sẻ
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    # Tự động tải và sử dụng ChromeDriver phù hợp
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # Bypass detection
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    # Mở trang
    driver.get(embed_url)
    time.sleep(5)  # Chờ trang tải
    
    # Cuộn chuột qua các trang
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.find_element("tag name", "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1.5)  # Điều chỉnh thời gian để cuộn tự nhiên
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    print("✅ Đã cuộn tới trang cuối cùng!")
    
    # Mở DevTools bằng tổ hợp phím Ctrl + Shift + I
    time.sleep(2)  # Đợi trang ổn định trước khi mở DevTools
    body = driver.find_element("tag name", "body")
    body.send_keys(Keys.CONTROL + Keys.SHIFT + "i")
    
    # Giữ trình duyệt mở để kiểm tra
    input("Nhấn Enter để đóng trình duyệt...")
    
    driver.quit()

# Nhập link từ người dùng
scribd_link = input("Nhập link Scribd: ")
download_pdf(scribd_link)