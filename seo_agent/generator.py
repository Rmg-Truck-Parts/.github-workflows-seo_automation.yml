import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ContentAgent")

class ContentAgent:
    def __init__(self, model_name="gpt-4"):
        self.model_name = model_name

    def generate_seo_content(self, topic, keywords):
        """
        Generates SEO-optimized content.
        In production, this calls an LLM API.
        """
        logger.info(f"Generating content using {self.model_name} for topic: {topic}")

        # Simulating LLM response
        content = f"""
        # {topic}

        Are you looking for professional services regarding {keywords[0]}?
        Our company is a leader in the industry, providing excellent results for {', '.join(keywords)}.

        ## Why Choose Us?
        We have years of experience in the field and we use the latest AI tools to stay ahead of the competition.

        ## Our Services
        - High-quality {keywords[0]}
        - Professional {keywords[1] if len(keywords) > 1 else 'support'}
        - 24/7 Availability

        Contact us today to learn more!
        """
        return content.strip()

    def search_directories(self, niche):
        """
        Finds directory submission opportunities.
        """
        logger.info(f"Searching for directories in niche: {niche}")
        # Real logic would use a search API and filter for 'add company' or 'catalog'
        return [
            f"https://www.google.com/search?q={niche}+katalog+firm",
            f"https://panoramafirm.pl/szukaj?q={niche}",
            f"https://www.yellowpages.pl/search?q={niche}"
        ]

if __name__ == "__main__":
    agent = ContentAgent()
    print(agent.generate_seo_content("SEO for Music Bands", ["wedding band", "music event"]))
