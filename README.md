
# Project Title
Job-hunt-bot

#Pre-requisite
    
    1 Programming Language & Package Manager
	•	Python 3.8+: The bot is written in Python, so ensure you have Python installed.

    2 Web Scraping Tools
	•	Selenium: Required for scraping dynamic pages (e.g., Workday) that require interaction.
    •	BeautifulSoup: For scraping static pages.
    •	Chrome WebDriver: Selenium requires a driver for interacting with your browser

    3 Database
	•	SQLite: For storing job postings to avoid duplicate notifications. No additional installation is needed as Python comes with SQLite built-in.

    4 Email Notifications
	•	Gmail SMTP (Free):
    •	SendGrid (Paid with free tier)

    5 SMS Notifications (Optional)
    •	Email-to-SMS Gateway (Free)
    •	Twilio (Paid with free trial)

    6 Python Dependencies
    •	requirements.txt

    7 CSV Input File:
    url,job_function,location

# Flow Chart
      Start
         |
         v
    Read Input File (URLs + Filters)
         |
         v
    Loop through each URL from File
         |
         v
    Fetch Career Page Content
    (Check for Redirect)
         |
         v
    Is there a Redirect?
     /       \
    No        Yes
    /            \
    Scrape         Follow Redirect
    Page           (Workday, etc.)
               Apply Filters
               (e.g., "Job Function"="Engineering")
                    |
                    v
          Scrape Job Listings from
            Filtered Results
                    |
                    v
      Compare Listings with Previously Seen Jobs
                    |
                    v
            Any New Jobs Found?
                    /    \
                    Yes     No
                    /         \
            Send Notification    End (No New Jobs)
            (Email/SMS)
                |
                v
        Save Scraped Jobs to Storage
                |
                v
                End

# Code Structure
    job_hunting_bot/
    │
    ├── main.py                    # Main entry point of the bot
    ├── config.yaml                 # Configuration file for email, phone, filters, etc.
    ├── input/                      # Input folder
    │   └── career_links.csv        # CSV file containing list of career URLs and filters
    ├── scraping/                   # Scraping logic folder
    │   ├── base_scraper.py         # Base class for scraping logic
    │   ├── static_scraper.py       # Static page scraper
    │   ├── dynamic_scraper.py      # Dynamic page scraper (Workday, etc.)
    ├── notifications/              # Notifications module
    │   └── notifier.py             # Email/SMS notification logic
    ├── storage/                    # Storage module for tracking seen jobs
    │   └── job_storage.py          # Logic to save and check previously seen jobs
    ├── utils/                      # Utility functions
    │   ├── logger.py               # Logging helper
    │   └── scheduler.py            # Scheduler logic to run the bot continuously
    └── requirements.txt            # Python dependencies

