#!/bin/bash
# Startup script for the SEO Agent Army

mkdir -p reports logs

echo "Launching SEO Agent Army in 24/7 Mode..."

# Run the orchestrator in continuous mode (1 hour interval by default)
python3 seo_agent/orchestrator.py --continuous > logs/startup.log 2>&1 &

echo "SEO Army is now running in the background."
echo "You can monitor progress by running: tail -f logs/seo_army.log"
