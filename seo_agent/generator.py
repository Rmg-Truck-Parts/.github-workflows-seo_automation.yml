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

    def validate_content(self, content, keywords):
        """
        Checks for keyword stuffing and natural language.
        (Anti-spam feature)
        """
        # Check keyword density (simple version)
        words = re.findall(r'\w+', content.lower())
        total_words = len(words)

        for kw in keywords:
            kw_count = content.lower().count(kw.lower())
            density = (kw_count / total_words) * 100 if total_words > 0 else 0
            if density > 10: # Threshold for keyword stuffing
                logger.warning(f"Keyword stuffing detected for '{kw}': {density:.2f}%")
                return False

        # Check for minimum length
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
    c = agent.generate_seo_content("SEO test", ["test"])
    print(c)
