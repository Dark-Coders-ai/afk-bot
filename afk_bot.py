import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run without UI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://example.com")  # Replace with the AFK site URL
    print("Bot is running...")
    while True:
        time.sleep(60)  # Stay AFK (adjust time if needed)
except KeyboardInterrupt:
    print("Stopping bot...")
finally:
    driver.quit()
