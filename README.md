# Zillow House Price Data Entry Project

This project scrapes property data (address, price, and link) from a Zillow clone website ([https://appbrewery.github.io/Zillow-Clone/](https://appbrewery.github.io/Zillow-Clone/)) and automatically enters the data into a Google Form.  It uses Python libraries like `requests`, `BeautifulSoup`, and `selenium` to achieve this.

## Project Overview

The project performs the following steps:

1. **Web Scraping (with `requests` and `BeautifulSoup`):**
   - Fetches the HTML content of the Zillow clone website.
   - Parses the HTML to extract property addresses, prices, and links to property details.

2. **Data Entry (with `selenium`):**
   - Opens a Google Form in a web browser (using ChromeDriver).
   - Iterates through the scraped data.
   - For each property:
     - Enters the address, price, and link into the corresponding form fields.
     - Submits the form.
     - Clicks the "Submit another response" link to prepare for the next entry.

## Requirements

* **Python 3.6 or higher:**  Ensure you have Python installed.  You can download it from [python.org](https://www.python.org/).
* **Required Libraries:**  Install the necessary Python packages using pip:
  ```bash
  pip install requests beautifulsoup4 selenium


ChromeDriver: Download the appropriate ChromeDriver executable for your operating system from chromedriver.chromium. org and place it in a location within your system's PATH or provide the path directly to the chromedriver executable when initialising the driver (This is done for you in the main.py file).

Setup and Execution

1. Clone the Repository:
git clone https://github.com/your-username/zillow-house-price-data-sheet.git  # Replace with your repo URL
cd zillow-house-price-data-sheet

2. Install Libraries: (if you haven't already)
pip install -r requirements.txt  # Assuming you create a requirements.txt file listing the dependencies

3. Google Form URL: Update the driver.get() URL in the main.py file with the URL of your Google Form. Make sure your Google form has fields titled "Address", "Price", and "Link". Alternatively, you can change the code to suit the input fields of your Google Form.

4. Run the Script:
python main.py


Code Structure
main.py: Contains the main logic for web scraping and data entry.


Potential Improvements

More Robust Selectors: The current implementation relies on specific XPaths, which could break if the Zillow clone website or Google Form structure changes. Consider using more robust selectors or adding error handling to detect and manage such situations.
Data Validation: Add data validation to handle potential missing data or unexpected formats from the scraped website.
Configuration: Store sensitive information like the Google Form URL in environment variables or a configuration file.
Headless Mode: Run ChromeDriver in headless mode (without opening a browser window) for faster and more automated execution. This has been done for you within the script provided.

Contributing
Feel free to contribute to this project! Open issues or pull requests for bug fixes, enhancements, or new features.


License
[Specify your project's license here (e.g., MIT, GPL, etc.) or add a LICENSE file to your repository.]
Remember to replace placeholders like `"your-username"` and `"your repository name"` with your actual details.  You should also create a `requirements.txt` file listing the project dependencies:

This improved README provides a more detailed explanation of the project, including setup instructions, potential improvements, and contribution guidelines, making it easier for others to understand and use your project. It also correctly links to the Zillow clone website.  If you plan to share this project publicly, a license is essential. Choose an appropriate open-source license and add it to the README and/or include a `LICENSE` file in your repository.
