from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Set up Firefox options
options = Options()
# Enable Developer Tools to open automatically
options.add_argument("-devtools")

# Initialize the WebDriver with the specified options
driver = webdriver.Firefox(options=options)
link = "https://www.scribd.com/embeds/645227545/content"

# Open a webpage (e.g., Google)
driver.get(link)

# Wait for a moment to ensure the page loads
time.sleep(2)

# Open Developer Tools using F12 key simulation
# Debug: only use F12 to open DevTools, use Ctrl Shift I maybe can not open DevTools windown!!!
ActionChains(driver).send_keys(Keys.F12).perform()

# Keep the browser open for a while to inspect
time.sleep(10)