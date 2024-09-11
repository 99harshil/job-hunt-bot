from scraping.base_scraper import BaseScraper
import requests
from bs4 import BeautifulSoup

class StaticScraper(BaseScraper):
    def scrape(self, url, filters):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        jobs = []
        for job_element in soup.find_all("div", class_="job-listing"):
            job = {
                "title": job_element.find("h2").text,
                "link": job_element.find("a")["href"],
                "location": job_element.find("span", class_="location").text
            }
            jobs.append(job)
        return jobs
