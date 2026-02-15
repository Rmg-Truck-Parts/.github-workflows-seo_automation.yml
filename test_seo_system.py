import sys
import os
import unittest

# Add the seo_agent directory to the search path
sys.path.append(os.path.join(os.getcwd(), 'seo_agent'))

from monitor import RankAgent
from auditor import AuditAgent
from generator import ContentAgent
from orchestrator import SEOAgentArmy

class TestSEOSystem(unittest.TestCase):
    def test_rank_agent(self):
        agent = RankAgent()
        rank = agent.get_google_rank("test", "test.com")
        self.assertIsInstance(rank, int)

    def test_audit_agent(self):
        agent = AuditAgent()
        # Using a reliable site for testing
        result = agent.analyze_page("https://www.google.com")
        self.assertEqual(result['status'], 'Success')
        self.assertIn('score', result)

    def test_content_agent(self):
        agent = ContentAgent()
        content = agent.generate_seo_content("Test", ["kw1"])
        self.assertIn("# Test", content)

    def test_orchestrator_load(self):
        army = SEOAgentArmy()
        self.assertIsInstance(army.sites, list)

if __name__ == "__main__":
    unittest.main()
