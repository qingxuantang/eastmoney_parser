
from eastmoney_parser import eastmoney_parser
from importlib import reload
eastmoney_parser = reload(eastmoney_parser)


if __name__ == "__main__":

    scraper = eastmoney_parser.ReportScraper()
    scraper.run()