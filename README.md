# Professional AI SEO Agent Army

This system is designed for continuous, multi-agent SEO optimization and monitoring for `www.matrix-music.com.pl` and `www.rmg-truck.pl`.

## Features
- **Parallel Agent Execution**: Uses Python threading to run multiple SEO agents simultaneously.
- **24/7 Monitoring**: Continuous ranking checks for Google search positions.
- **Automated Technical Audits**: Real-time health checks using `BeautifulSoup`.
- **GEO (Generative Engine Optimization)**: Specialized strategies to improve recommendations in AI search engines (Perplexity, SGE, Gemini).
- **Anti-Spam Measures**: Randomized delays and User-Agent rotation.

## Directory Structure
- `seo_agent/`
  - `orchestrator.py`: The Commander. Coordinates parallel agents.
  - `monitor.py`: Ranking and competitor tracking.
  - `auditor.py`: Real HTML auditing.
  - `generator.py`: AI-ready content and GEO strategy.
- `reports/`: JSON reports generated for each site.
- `logs/`: Execution logs for 24/7 monitoring.
- `config.json`: Multi-site and keyword configuration.

## Setup & Execution
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the orchestrator in 24/7 mode:
   ```bash
   python3 seo_agent/orchestrator.py --continuous
   ```
   Or use the provided startup script:
   ```bash
   bash start_seo_army.sh
   ```

## Scaling for Professional Use
To achieve the best results in a production environment:
- **Search API**: Integrate a paid API (e.g., [Serper.dev](https://serper.dev/)) in `monitor.py`.
- **LLM API**: Integrate OpenAI GPT-4 or Anthropic Claude in `generator.py` by adding your API keys.
- **CMS Integration**: Extend the agents to automatically push content to your website via WordPress REST API or other CMS endpoints.
