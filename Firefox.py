# Use Firefox


from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


# Set up Firefox options
options = Options()
# Enable Developer Tools to open automatically
options.add_argument("-devtools")

# Convert link
def convert_scribd_link(url):
    import re
    match = re.search(r'https://www\.scribd\.com/document/(\d+)/', url)
    if match:
        doc_id = match.group(1)
        return f'https://www.scribd.com/embeds/{doc_id}/content'
    else:
        return "Invalid Scribd URL"


# Input Scribd link
input_url = input("Input link Scribd: ")
converted_url = convert_scribd_link(input_url)
print("Link embed:", converted_url)

# Initialize the WebDriver with the specified options
driver = webdriver.Firefox(options=options) # replace Firefox with Chrome if you use Google Chrome
firefox_profile = webdriver.FirefoxProfile()


# Open the webpage
driver.get(converted_url)


# Wait for the page to load
time.sleep(2)


""" STEP 01: SCROLL """
# Scroll from the top to the bottom of the page
page_elements = driver.find_elements("css selector", "[class*='page']")
for page in page_elements:
    driver.execute_script("arguments[0].scrollIntoView();", page)
    time.sleep(2)

print("Last Page") 


time.sleep(2)  # Wait for DevTools to open


""" STEP 02: DELETE DIVS - CLASS """
# delete footer top & bottom: 
toolbar_top_exists = driver.execute_script("""
        var toolbarTop = document.querySelector('.toolbar_top');
        if (toolbarTop) {
            toolbarTop.parentNode.removeChild(toolbarTop);
            return true;  // Indicate that it was removed
        }
        return false;  // Indicate that it was not found
    """)

# Debug message for toolbar_top
if toolbar_top_exists:
    print("'toolbar_top' was successfully deleted.")
else:
    print("'toolbar_top' was not found.")

# Check and delete toolbar_bottom
toolbar_bottom_exists = driver.execute_script("""
    var toolbarBottom = document.querySelector('.toolbar_bottom');
    if (toolbarBottom) {
        toolbarBottom.parentNode.removeChild(toolbarBottom);
        return true;  // Indicate that it was removed
    }
    return false;           // Indicate that it was not found
""")

# Debug message for toolbar_bottom
if toolbar_bottom_exists:
    print("✅ 'toolbar_bottom' was successfully deleted.")
else:
    print("❌ 'toolbar_bottom' was not found.") 

# deleting container:
elements = driver.find_elements(By.CLASS_NAME, "document_scroller")

# Loop through each element and change its class
for element in elements:
    driver.execute_script("arguments[0].setAttribute('class', '');", element)

print("  -------  Deleted containers  ----------")


""" STEP 03: PRINT PDF """
# open print windown
driver.execute_script("window.print();")


