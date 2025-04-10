{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "c5334419-5bcd-4c2e-8e42-b3990af3b5a3",
   "metadata": {},
   "source": [
    "\n",
    "#### YouTube Trending Video Analytics\n",
    "\n",
    "###### Fetches top 100 trending videos globally, including title, views, likes, channel details, and more.\n",
    "###### Saves data to an Excel file for analysis. Built with YouTube Data API and Python.\n",
    "\n",
    "###### Author: Supriya Sonone\n",
    "###### Date: April 2025\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "92bbe7bf-49ed-4ef0-a66d-f7b8c44bcb8e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from googleapiclient.discovery import build\n",
    "import pandas as pd\n",
    "from datetime import datetime\n",
    "\n",
    "# Configuration\n",
    "API_KEY = \"AIzaSyBWBqa1IYGJWcIkM8sMJRqwbV04fd4Wp7c\"\n",
    "TARGET_VIDEOS = 100  # Number of trending videos to fetch\n",
    "REGION_CODE = None  # can use country code for specific country or region\n",
    "\n",
    "# Initialize YouTube API client\n",
    "youtube = build(\"youtube\", \"v3\", developerKey=API_KEY)\n",
    "\n",
    "def get_subscribers(channel_id):\n",
    "    \"\"\"Fetch subscriber count for a given channel ID.\"\"\"\n",
    "    try:\n",
    "        request = youtube.channels().list(part=\"statistics\", id=channel_id)\n",
    "        response = request.execute()\n",
    "        return int(response[\"items\"][0][\"statistics\"][\"subscriberCount\"]) if response[\"items\"] else 0\n",
    "    except Exception as e:\n",
    "        print(f\"Error fetching subscribers for channel {channel_id}: {e}\")\n",
    "        return 0\n",
    "\n",
    "def fetch_trending_videos():\n",
    "    \"\"\"Fetch top 100 trending videos with details.\"\"\"\n",
    "    videos_data = []\n",
    "    max_results_per_call = 50  # API max per call\n",
    "    page_token = None\n",
    "\n",
    "    try:\n",
    "        while len(videos_data) < TARGET_VIDEOS:\n",
    "            request = youtube.videos().list(\n",
    "                part=\"snippet,statistics,contentDetails\",\n",
    "                chart=\"mostPopular\",\n",
    "                regionCode=REGION_CODE,\n",
    "                maxResults=max_results_per_call,\n",
    "                pageToken=page_token\n",
    "            )\n",
    "            response = request.execute()\n",
    "            print(f\"Fetched {len(response['items'])} videos in this batch\")\n",
    "\n",
    "            for video in response[\"items\"]:\n",
    "                videos_data.append({\n",
    "                    \"Video Name\": video[\"snippet\"][\"title\"],\n",
    "                    \"Views\": int(video[\"statistics\"][\"viewCount\"]),\n",
    "                    \"Likes\": int(video[\"statistics\"].get(\"likeCount\", 0)),\n",
    "                    \"Channel Name\": video[\"snippet\"][\"channelTitle\"],\n",
    "                    \"Post Date\": video[\"snippet\"][\"publishedAt\"],\n",
    "                    \"Duration\": video[\"contentDetails\"][\"duration\"],\n",
    "                    \"Subscribers\": get_subscribers(video[\"snippet\"][\"channelId\"]),\n",
    "                    \"Description\": video[\"snippet\"][\"description\"],\n",
    "                    \"Category\": video[\"snippet\"][\"categoryId\"]\n",
    "                })\n",
    "\n",
    "            page_token = response.get(\"nextPageToken\")\n",
    "            if not page_token or len(videos_data) >= TARGET_VIDEOS:\n",
    "                break\n",
    "\n",
    "        return videos_data[:TARGET_VIDEOS]  # Trim to exactly 100\n",
    "\n",
    "    except Exception as e:\n",
    "        print(f\"Error fetching data: {e}\")\n",
    "        return []\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "16af84e0-22fd-423f-92e5-7018073cc927",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fetched 50 videos in this batch\n",
      "Fetched 50 videos in this batch\n"
     ]
    }
   ],
   "source": [
    "videos_data = fetch_trending_videos()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bd5317e3-e0ea-4a98-a162-98a6d49cf326",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Sample of Top 5 Trending Videos:\n",
      "Title: Murderbot — Official Trailer | Apple TV+, Channel: Apple TV, Views: 1,236,632\n",
      "Title: HIGHLIGHTS - Arsenal vs Real Madrid | UEFA Champions League - 4tos Final 24/25 | TUDN, Channel: TUDN USA, Views: 1,084,716\n",
      "Title: They Didn't Make Dire Wolves, They Made Something…Else, Channel: hankschannel, Views: 984,058\n",
      "Title: Ghost - Lachryma (Trailer), Channel: Ghost, Views: 138,590\n",
      "Title: Commandos Origins Review - Rough Riders Rough as Sh*t, Channel: ACG, Views: 56,877\n",
      "\n",
      "Data saved to trending_videos_20250410_113236.xlsx with 100 rows\n"
     ]
    }
   ],
   "source": [
    "# Display sample output\n",
    "if videos_data:\n",
    "    print(\"\\nSample of Top 5 Trending Videos:\")\n",
    "    for video in videos_data[:5]:\n",
    "        print(f\"Title: {video['Video Name']}, Channel: {video['Channel Name']}, Views: {video['Views']:,}\")\n",
    "\n",
    "    # Save to Excel\n",
    "    timestamp = datetime.now().strftime(\"%Y%m%d_%H%M%S\")\n",
    "    filename = f\"trending_videos_{timestamp}.xlsx\"\n",
    "    df = pd.DataFrame(videos_data)\n",
    "    df.to_excel(filename, index=False)\n",
    "    print(f\"\\nData saved to {filename} with {len(videos_data)} rows\")\n",
    "else:\n",
    "    print(\"No data fetched. Check API key or network.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0565d663-7ae5-42fb-a380-12d4f1026538",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
