import pywhatkit as kit
from googlesearch import search

def youtube_search(query):
    try:
        video_url = kit.playonyt(query)
        return video_url
    except Exception as e:
        print("An error occurred while performing the YouTube search:", e)
        return []

def google_search(query, num_results=5):
    try:
        search_results = list(search(query, num_results=num_results))
        return search_results
    except Exception as e:
        print("An error occurred while performing the Google search:", e)
        return []