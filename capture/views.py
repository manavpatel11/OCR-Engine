from django.shortcuts import render
import requests
from gtts import gTTS

def hm(request):
    return render(request, 'capture.html')

import base64
import os
from django.conf import settings
from django.http import JsonResponse


def save_image(request):
    image_data = request.POST.get('image_data')
    if not image_data:
        return JsonResponse({'error': 'No image data provided'}, status=400)

    image_data = image_data.split(',')[1]
    image_data = base64.b64decode(image_data)

    filename = 'capture_img/captured_image.png'
    filepath = os.path.join(settings.MEDIA_ROOT, filename)

    with open(filepath, 'wb') as f:
        f.write(image_data)

    return JsonResponse({'message': 'Image saved successfully'})


def cimg(request):
    
    # if(request.session.get('rl')==1):
    #     cimg(request)
    #     request.session['rl'] = 0
    # else:
    #     request.session['rl'] = 1
    
    API_KEY = "AIzaSyB8gm7-cGZVBwxDYcCORBvYfWXn3o4quOo"
    # The URL for the Vision API
    VISION_URL = "https://vision.googleapis.com/v1/images:annotate?key=" + API_KEY

    # The image you want to analyze
    image_path = f'capture_img/captured_image.png'

    # Read the image and convert it to base64
    with open(image_path, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

    # The request body for the Vision API
    request_body = {
        "requests": [
            {
                "image": {
                    "content": image_base64
                },
                "features": [
                    {
                        "type": "LABEL_DETECTION"
                    },
                    {
                        "type": "DOCUMENT_TEXT_DETECTION"
                    }
                ]
            }
        ]
    }
    
        

    response = requests.post(VISION_URL, json=request_body)

    tex = response.json()['responses'][0]['fullTextAnnotation']['text']
   
    text_frontend = {}
    text_frontend.update({'text':tex})
    request.session['rl'] = 1
    
    tts = gTTS(text=tex, lang='en-uk')
    tts.save("static/assets/Audio/output.mp3")
    os.system("mpg123 output.mp3")
    
    return render(request,'cap_result.html',text_frontend)


def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
                
    return dp[m][n]

    


def match_accuracy(request):
    s1 = request.session.get('key2')
    tex = s1
    s1 = s1.replace(" ","")
    
    s2 = request.POST["message"]
    tex2 = s2
    s2 = s2.replace(" ","")
    
    
    distance = levenshtein_distance(s1, s2)
    max_length = max(len(s1), len(s2))
    ac = 1.0 - float(distance) / max_length
    ac = ac*100
    text_frontend= {
        'acc':ac,
        'text2':tex2,
        'text':tex
    }
    print(text_frontend)
    return render(request,'matchacc.html',text_frontend)