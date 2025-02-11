# Scribd Downloader Full Explanation With Code

## Idea
### Main Idea:
- Extract the PDF from the provided link.

### Execution:
- Retrieve the embedded link from the user’s input.
- Scroll through all pages from the first to the last (since the embed only loads one page at a time, leaving other pages blank if not scrolled).
- Remove the following elements via DevTools:
  + class="document_scroller"
  + <div>toolbar_drop</div>
  + <div>mobile_overlay</div>
- Open the print window.
- The results:
  + Google Chrome
![GoogleChrome_linktoPDF](https://github.com/user-attachments/assets/30ae8d58-fbca-4b9b-af0f-5f437e9bacb1)
  + Firefox
![Firefox_linktoPDF](https://github.com/user-attachments/assets/979ff4ec-5837-46e2-ae8c-ee0efacdf673)

**Note: The "Print as PDF" option must be selected, and "Print both header and footer" must be unchecked in the print settings.** 

## Code
- Python 3.8.20
- Environments: view requirements.txt (pip install -r requirements.txt)
- Currently, I have written the code to run on the Windows platform, supporting both Google Chrome and Firefox browsers. Please refer to GoogleChrome.py and Firefox.py for details.
- View the "ErrorLog" if you encounter any issues.
**Note: Each browser and OS may have different conditions, so please verify them beforehand.**
