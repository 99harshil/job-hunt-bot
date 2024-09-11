from selenium import webdriver
from selenium.webdriver.common.by import By
from scraping.base_scraper import BaseScraper

class DynamicScraper(BaseScraper):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def scrape(self, url, filters):
        self.driver.get(url)
        # Example interaction with filters (Job Function, Location)
        location_dropdown = self.driver.find_element(By.XPATH, "//select[@name='location']")
        location_dropdown.click()
        location_option = self.driver.find_element(By.XPATH, f"//option[contains(text(), '{filters['location']}')]")
        location_option.click()

        # Fetch job postings after filters applied
        jobs = []
        job_elements = self.driver.find_elements(By.CLASS_NAME, 'job-listing')
        for job_element in job_elements:
            job = {
                "title": job_element.find_element(By.CLASS_NAME, "title").text,
                "link": job_element.find_element(By.TAG_NAME, "a").get_attribute("href"),
                "location": job_element.find_element(By.CLASS_NAME, "location").text
            }
            jobs.append(job)
        return jobs
