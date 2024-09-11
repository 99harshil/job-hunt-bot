from scraping.base_scraper import ScraperFactory
from storage.job_storage import JobStorage
from notifications.notifier import Notifier
from utils.scheduler import schedule_scraper
import yaml

def main():
    # Load configuration
    with open("config.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)

    # Initialize storage for previously seen jobs
    job_storage = JobStorage()

    # Initialize notifier
    notifier = Notifier(config["email"])

    # Load career page URLs and filters from input file
    career_links = "input/career_links.csv"
    
    # Schedule and run the scraper
    schedule_scraper(career_links, job_storage, notifier, config["scraping_interval"])

if __name__ == "__main__":
    main()
