from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

# Plain text response
def simple_text_view(request):
    return HttpResponse("Hello, this is a simple text response!")

# JSON response
def simple_json_view(request):
    data = {
        'message': 'Hello, this is a JSON response!',
        'status': 'success'
    }
    return JsonResponse(data)

# No content response
def no_content_view(request):
    return HttpResponse(status=204)

# Redirect response
def simple_redirect_view(request):
    return redirect('https://www.example.com')
