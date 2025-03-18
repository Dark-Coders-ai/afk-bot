import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setup Chrome options
chrome_options = Options()
chrome_options.binary_location = "/usr/bin/google-chrome-stable"
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Start ChromeDriver
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://example.com")  # Replace with your target URL
    print("Bot is running...")
    while True:
        time.sleep(60)  # Refresh every 60 seconds
        driver.refresh()
except KeyboardInterrupt:
    print("Stopping bot...")
finally:
    driver.quit()
