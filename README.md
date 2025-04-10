# YouTube Trending Video Analytics
A Python tool to fetch, analyze, and visualize the top 100 trending YouTube videos globally.  
Built with the YouTube Data API, it saves data to Excel and includes hourly automation.

## Features
- Fetches 100 trending videos with metadata.
- Saves to Excel (e.g., `trending_videos_20250410_113236.xlsx`).
- Analyzes and visualizes top categories and channels with Matplotlib.
- Automated version runs hourly.

## Files
- `youtube_trending_videos.ipynb`: Notebook with fetch, analysis, and visuals.
- `youtube_analytics_auto.py`: Automated data fetch (hourly).
- `trending_videos_20250410_144053.xlsx`: Sample output.
- `top_categories.png`: Top 5 categories by count.
- `avg_views_by_category.png`: Average views by top 5 categories.
- `top_channels_subscribers.png`: Subscribers of top 5 channels.

## How to Run
1. Install: `pip install google-api-python-client pandas openpyxl matplotlib`
2. Run:
   - Notebook: `jupyter notebook youtube_trending_videos.ipynb`
   - Automated: `python youtube_analytics_auto.py`

## Author
Supriya Sonone - April 2025
