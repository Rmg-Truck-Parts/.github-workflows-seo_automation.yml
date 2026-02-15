import requests
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AuditAgent")

class AuditAgent:
    def analyze_page(self, url):
        """
        Fetches and audits a webpage for SEO best practices.
        """
        logger.info(f"Starting audit for: {url}")
        try:
            # We use a user-agent to avoid being blocked by simple bot detectors
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) SEO-Agent/1.0'}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            issues = []

            # 1. Check Title
            title = soup.title.string if soup.title else None
            if not title:
                issues.append("Missing <title> tag.")
            elif len(title) < 30:
                issues.append(f"Title too short ({len(title)} chars): '{title}'")

            # 2. Check Meta Description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if not meta_desc or not meta_desc.get('content'):
                issues.append("Missing meta description.")

            # 3. Check Headings
            h1s = soup.find_all('h1')
            if len(h1s) == 0:
                issues.append("Missing H1 heading.")
            elif len(h1s) > 1:
                issues.append(f"Multiple H1 headings found ({len(h1s)}).")

            # 4. Check Images Alt Tags
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
    # Test with a known site
    results = agent.analyze_page("http://www.matrix-music.com.pl")
    print(results)
