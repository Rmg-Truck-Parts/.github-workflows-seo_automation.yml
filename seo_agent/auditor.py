import requests
from bs4 import BeautifulSoup
import logging
import time
import random

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AuditAgent")

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"
]

class AuditAgent:
    def analyze_page(self, url):
        """
        Fetches and audits a webpage for SEO best practices.
        Includes anti-spam features.
        """
        logger.info(f"Starting audit for: {url}")

        # Anti-spam delay
        time.sleep(random.uniform(1, 4))

        try:
            headers = {'User-Agent': random.choice(USER_AGENTS)}
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            issues = []

            title = soup.title.string if soup.title else None
            if not title:
                issues.append("Missing <title> tag.")
            elif len(title) < 30:
                issues.append(f"Title too short ({len(title)} chars): '{title}'")

            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if not meta_desc or not meta_desc.get('content'):
                issues.append("Missing meta description.")

            h1s = soup.find_all('h1')
            if len(h1s) == 0:
                issues.append("Missing H1 heading.")
            elif len(h1s) > 1:
                issues.append(f"Multiple H1 headings found ({len(h1s)}).")

            images = soup.find_all('img')
            missing_alt = [img for img in images if not img.get('alt')]
            if missing_alt:
                issues.append(f"{len(missing_alt)} images are missing alt attributes.")

            score = max(0, 100 - (len(issues) * 10))

            return {
                "url": url,
                "title": title,
                "score": score,
                "issues": issues,
                "status": "Success"
            }
        except Exception as e:
            logger.error(f"Audit failed for {url}: {e}")
            return {"url": url, "status": "Error", "error": str(e), "score": 0, "issues": ["Could not reach site."]}

if __name__ == "__main__":
    agent = AuditAgent()
    results = agent.analyze_page("http://www.matrix-music.com.pl")
    print(results)
