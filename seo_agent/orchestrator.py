import threading
import time
import logging
import json
import os
import sys

# Add the current directory to sys.path to allow running from root
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from monitor import RankAgent
from auditor import AuditAgent
from generator import ContentAgent

# Global Configuration
logging.basicConfig(
    level=logging.INFO,
    format='[%(name)s] %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler("logs/seo_army.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("Orchestrator")

class SEOAgentArmy:
    def __init__(self, config_file="config.json"):
        self.sites = self.load_config(config_file)
        self.rank_agent = RankAgent()
        self.audit_agent = AuditAgent()
        self.content_agent = ContentAgent()
        self.is_running = False

    def load_config(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
        return []

    def process_site(self, site):
        """
        Runs a full SEO cycle for a single site.
        """
        name = site['name']
        url = site['url']
        keywords = site['keywords']

        logger.info(f"Agent starting work on {name}...")

        # 1. Monitoring (Real Audit logic in RankAgent)
        ranks = {kw: self.rank_agent.get_google_rank(kw, url) for kw in keywords}

        # 2. Technical Audit (Real Audit logic in AuditAgent)
        audit = self.audit_agent.analyze_page(url)

        # 3. AI Search Optimization (GEO)
        logger.info(f"Generating GEO (Generative Engine Optimization) strategy for {name}...")
        geo_strategy = self.content_agent.generate_geo_strategy(name, keywords)

        # 4. Optimization Recommendation
        if audit['score'] < 80:
            logger.info(f"Low SEO score ({audit['score']}) for {name}. Generating optimization content...")
            topic = f"Optimizing {name} for {keywords[0]}"
            suggestion = self.content_agent.generate_seo_content(topic, keywords)

        logger.info(f"Agent finished work on {name}. Score: {audit['score']}, Ranks: {ranks}")

        # Save report locally in reports/ directory
        report = {
            "timestamp": time.ctime(),
            "site": name,
            "url": url,
            "audit": audit,
            "rankings": ranks,
            "geo_strategy": geo_strategy
        }
        filename = f"reports/report_{name.lower().replace(' ', '_')}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)

    def start_army(self):
        """
        Spawns multiple agents in parallel.
        """
        if not self.sites:
            logger.error("No sites configured in config.json")
            return

        threads = []
        for site in self.sites:
            t = threading.Thread(target=self.process_site, args=(site,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def run_continuous(self, interval_seconds=3600):
        """
        Runs the army 24/7.
        """
        self.is_running = True
        logger.info("24/7 SEO Agent Army activated!")
        try:
            while self.is_running:
                self.start_army()
                logger.info(f"Cycle complete. Next run in {interval_seconds}s...")
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            self.is_running = False
            logger.info("Shutting down the army...")

if __name__ == "__main__":
    army = SEOAgentArmy()
    if "--continuous" in sys.argv:
        army.run_continuous()
    else:
        army.start_army()
