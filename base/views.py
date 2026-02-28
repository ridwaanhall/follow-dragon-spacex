from django.conf import settings
from django.shortcuts import redirect, render
from django.views import View
from django.http import JsonResponse, HttpResponse
import requests
import datetime
import logging

logging.basicConfig(level=logging.ERROR)

class DragonPublicView(View):
    def get(self, request):
        if not getattr(settings, 'IS_AVAILABLE', True):
            return JsonResponse({
                "status": "unavailable",
                "message": "The service is temporarily unavailable due to high traffic or maintenance. Please try again later.",
                "code": 503
            }, status=503)
        url = settings.DRAGON_PUBLIC_URL
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
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            json_data = response.json()
            return JsonResponse(json_data, safe=False)
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data: {e}")
            return HttpResponse("An internal error has occurred.", status=500)

class EarthTextureView(View):
    def get(self, request):
        return render(request, 'base/texture.html')

class EarthMapView(View):
    def get(self, request):
        if not getattr(settings, 'IS_AVAILABLE', True):
            return JsonResponse({
                "status": "unavailable",
                "message": "The service is temporarily unavailable due to high traffic or maintenance. Please try again later.",
                "code": 503
            }, status=503)
        return render(request, 'base/map.html')
