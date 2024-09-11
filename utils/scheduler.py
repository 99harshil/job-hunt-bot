import time
from scraping.base_scraper import ScraperFactory

def schedule_scraper(career_links_file, job_storage, notifier, interval):
    with open(career_links_file, "r") as file:
        lines = file.readlines()

    while True:
        for line in lines:
            url, filters = parse_line(line)
            scraper = ScraperFactory.get_scraper(url)
            jobs = scraper.scrape(url, filters)

            for job in jobs:
                if not job_storage.has_seen(job["link"]):
                    job_storage.save_job(job["link"])
                    notifier.send_email(job)
                    #notifier.send_sms(job)

        # Wait for the next scrape interval
        time.sleep(interval)

def parse_line(line):
    parts = line.strip().split(",")
    url = parts[0]
    filters = {"job_function": parts[1], "location": parts[2]}
    return url, filters
