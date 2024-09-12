from django.shortcuts import render
import requests
import datetime
from django.http import JsonResponse, HttpResponse

def dragon_public(request):
    url = "https://sxcontent9668.azureedge.us/cms-assets/dragon_public.json"
    
    # Custom headers (if needed)
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9,mt;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'if-modified-since': datetime.date.today().strftime('%a, %d %b %Y %H:%M:%S GMT'),
        'if-none-match': '"0x8DCD326FC7FE5DE"',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0',
    }

    try:
        # Make the request to the JSON endpoint
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors

        # Parse JSON content
        json_data = response.json()

        # Return the JSON data as a response
        return JsonResponse(json_data, safe=False)

    except requests.exceptions.RequestException as e:
        # Handle any request errors
        return HttpResponse(f"Error fetching data: {e}", status=500)

def follow_dragon_view(request):
    return render(request, 'follow-dragon.html')