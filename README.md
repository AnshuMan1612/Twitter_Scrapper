# Twitter_Scrapper

# Twitter Profile Scraper

This Python script scrapes data from a public Twitter profile (bio, location, website, and join date) and saves it to a CSV file.  It uses Selenium for browser automation and BeautifulSoup for HTML parsing.

## Prerequisites

Before running the script, make sure you have the following installed:

*   **Python 3:**  You can download it from [https://www.python.org/](https://www.python.org/).
*   **Selenium:** Install it using pip: `pip install selenium`
*   **BeautifulSoup4:** Install it using pip: `pip install beautifulsoup4`
*   **ChromeDriver:** Download the ChromeDriver that matches your Chrome browser version from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads).  Place the `chromedriver` executable in a directory in your system's PATH, or specify the path to the executable in the script (see "Usage" below).

## How to Use

1.  **Clone or download the repository:** If you have the code in a repository, clone it. Otherwise, download the Python script (`twitter_scraper.py` or whatever you named it).

2.  **Install the required libraries:** If you haven't already, install the necessary Python libraries as mentioned in the "Prerequisites" section.

3.  **Configure the script:**
    *   Open the Python script in a text editor.
    *   Modify the `user_url` and `user_name` variables at the beginning of the script to the desired Twitter profile.  For example:

    ```python
    user_url = "[https://twitter.com/elonmusk](https://twitter.com/elonmusk)"  # Replace with the desired username
    user_name = "elonmusk"  # Replace with the desired username
    ```

4.  **(Optional) Specify ChromeDriver path:** If you did not add the `chromedriver` to your system's PATH, you'll need to tell Selenium where it is. Add the following line after `driver = webdriver.Chrome()`:

    ```python
    driver = webdriver.Chrome("/path/to/your/chromedriver") # Replace with the full path to your chromedriver
    ```

5.  **Run the script:** Open a terminal or command prompt, navigate to the directory where you saved the script, and run it using:

    ```bash
    python twitter_scraper.py
    ```

6.  **Check the output:** The scraped data will be saved in a CSV file named `twitter_data.csv` in the same directory as the script.

## Output

The `twitter_data.csv` file will contain the following columns:

*   `User Name`: The Twitter username.
*   `Bio`: The user's bio.
*   `Location`: The user's location.
*   `Website`: The user's website.
*   `Join Date`: The user's join date.

## Important Notes

*   This script is for educational purposes only.  Please use it responsibly and respect Twitter's terms of service.
*   Twitter's website structure can change, which might break the script. You may need to update the CSS selectors if this happens.
*   The script includes error handling (using `try-except` blocks), but it's always good practice to review the output and logs for any potential issues.
*   Be mindful of rate limiting.  Scraping too frequently might lead to your IP being temporarily blocked by Twitter.  Consider adding delays to your script if needed.

## Disclaimer

The author of this script is not responsible for any misuse of the code.  Use it at your own risk.
