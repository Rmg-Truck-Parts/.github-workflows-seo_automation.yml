import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ContentAgent")

class ContentAgent:
    def __init__(self, model_name="gpt-4"):
        self.model_name = model_name

    def generate_seo_content(self, topic, keywords):
        """
        Generates SEO-optimized content.
        """
        logger.info(f"Generating content for topic: {topic}")

        content = f"""
        # {topic}

        Are you looking for professional services regarding {keywords[0]}?
        Our company is a leader in the industry, providing excellent results for {', '.join(keywords)}.

        ## Why Choose Us?
        We have years of experience in the field and we use the latest AI tools to stay ahead of the competition.

        ## Our Services
        - High-quality {keywords[0]}
        - Professional support
        - 24/7 Availability

        Contact us today to learn more!
        """

        final_content = content.strip()
        if self.validate_content(final_content, keywords):
            return final_content
        else:
            logger.warning("Content failed quality validation. Regenerating...")
            return "Quality content placeholder."

    def generate_geo_strategy(self, site_name, keywords):
        """
        Generates Generative Engine Optimization (GEO) strategy.
        Focuses on how to get AI search engines (like Perplexity or Gemini)
        to recommend the site.
        """
        logger.info(f"Developing AI Recommendation strategy for {site_name}")
        strategy = {
            "focus": "Authoritative Citations & Structured Data",
            "actions": [
                f"Ensure {site_name} is listed in top niche directories with consistent NAP (Name, Address, Phone).",
                "Create in-depth 'How-to' guides related to " + ", ".join(keywords[:2]),
                "Optimize for conversational queries (Natural Language Processing).",
                "Add Schema.org markup for LocalBusiness and FAQ."
            ],
            "recommendation": "Use authoritative tone and provide unique data points that AI models can cite."
        }
        return strategy

    def validate_content(self, content, keywords):
        """
        Checks for keyword stuffing and natural language.
        (Anti-spam feature)
        """
        words = re.findall(r'\w+', content.lower())
        total_words = len(words)

        for kw in keywords:
            kw_count = content.lower().count(kw.lower())
            density = (kw_count / total_words) * 100 if total_words > 0 else 0
            if density > 10:
                logger.warning(f"Keyword stuffing detected for '{kw}': {density:.2f}%")
                return False

        if total_words < 30:
            logger.warning("Content too short.")
            return False

        return True

    def search_directories(self, niche):
        """
        Finds directory submission opportunities.
        """
        logger.info(f"Searching for directories in niche: {niche}")
        return [
            f"https://www.google.com/search?q={niche}+katalog+firm",
            f"https://panoramafirm.pl/szukaj?q={niche}",
            f"https://www.yellowpages.pl/search?q={niche}"
        ]

if __name__ == "__main__":
    agent = ContentAgent()
    geo = agent.generate_geo_strategy("RMG Truck", ["parts", "trucks"])
    print(geo)
