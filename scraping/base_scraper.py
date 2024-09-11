from abc import ABC, abstractmethod

class BaseScraper(ABC):
    
    @abstractmethod
    def scrape(self, url, filters):
        pass

class ScraperFactory:
    @staticmethod
    def get_scraper(url):
        # Return the appropriate scraper based on the URL structure
        if "workday" in url:
            return DynamicScraper()
        else:
            return StaticScraper()
