# youtube-trending-analytics
A Python tool to analyze top 100 trending YouTube videos
# YouTube Trending Video Analytics
A Python tool to fetch and analyze the top 100 trending YouTube videos globally.  
Built with the YouTube Data API, it collects video titles, views, likes, channel details, and more, saving results to Excel.

## Features
- Fetches 100 trending videos with detailed metadata.
- Saves data to timestamped Excel files (e.g., `trending_videos_20250401_123456.xlsx`).
- Uses Python, pandas, and Google’s API for real-time insights.

## How to Run
1. Install dependencies: `pip install google-api-python-client pandas openpyxl`
2. Add your YouTube Data API key in `youtube_analytics.py`.
3. Run: `python youtube_analytics.py`

## Output
Excel file with columns: Video Name, Views, Likes, Channel Name, Post Date, Duration, Subscribers, Description, Category.

## Author
Supriya Sonone - April 2025
