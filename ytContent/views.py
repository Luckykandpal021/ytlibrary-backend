from django.http import JsonResponse
import requests
import googleapiclient.discovery
from django.conf import settings


def videoSearch(request):
    if request.method=='GET':
        query=request.GET.get('query','')
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=settings.YOUTUBE_DATA_API)
        # Search for videos
        response = youtube.search().list(q=query, type="video", part="id,snippet",maxResults=40).execute()
        # Extract video IDs from the search results
        video_ids = []
        for item in response["items"]:
            video_ids.append(item["id"]["videoId"])

        print(f'video_ids:- {video_ids}')    

        return JsonResponse({'search_query_videoes': video_ids})




