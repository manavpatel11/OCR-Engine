from django.shortcuts import render,redirect
from gtts import gTTS
from pyscreeze import locate
from .models import gujrati_files
from PIL import Image
import pytesseract
import os
import datetime
from pdf2image import convert_from_path
from PIL import Image
import cv2
import requests
import base64
import shutil
from requests import get
from .models import ip as ip_tr

# poppler_path=r'C:\Program Files\poppler-22.04.0\Library\bin'


def scanhompage(request):
    return render(request,'scan.html')

def check_endwith(child_dir):
    
    end = 1
    c_dir = child_dir + f'_{end}'
    end=end+1
    if(os.path.exists(c_dir)):
                c_dir = check_endwith(c_dir)
    return c_dir
    
def check_pdf_path(filename,filename2):
    if(os.path.exists('Uploaded_Data/pdf/')):
            
            child_dir = 'Uploaded_Data/pdf/'+f'{filename}'
            if(os.path.exists(child_dir)):
                child_dir = check_endwith(child_dir)
            os.mkdir(child_dir)
            tex = pdf_to_image(filename2,child_dir)
            return tex
           
    else:
            parent = 'Uploaded_Data'
            p_dir = 'pdf'
            pdf_dir = os.path.join(parent,p_dir)
            child_dir = pdf_dir+"/" + f'{filename}'
            os.mkdir(pdf_dir)
            os.mkdir(child_dir)

            tex = pdf_to_image(filename2,child_dir)
            return tex


def pdf_to_image(location,child_dir):
        tex = ""
        images = convert_from_path(f'Uploaded_Data/{location}',500)
        for i in range(len(images)):
                f_name = child_dir+'/page'+ str(i) +'.jpg'
                images[i].save(f_name)
                tex = tex + pdf_data(f_name)
        return tex
            



def pdf_data(filename):
    
    API_KEY = "AIzaSyB8gm7-cGZVBwxDYcCORBvYfWXn3o4quOo"
    # The URL for the Vision API
    VISION_URL = "https://vision.googleapis.com/v1/images:annotate?key=" + API_KEY

    # The image you want to analyze
    image_path = f'{filename}'

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
    return tex
    # # for i in os.listdir(child_dir):
    # tex= pytesseract.image_to_string(Image.open(),lang='guj')
    # return tex


def save_file(filename,extension,tex):
    locate = ''
    if(extension == 'pdf'):
            with open(f'result/pdf/{filename}.doc', 'w', encoding='utf-8') as f:
                f.write(tex)
                locate = f'pdf/{filename}.doc'
    else:
             with open(f'result/img/{filename}.doc', 'w', encoding='utf-8') as f:
                f.write(tex)
                locate = f'img/{filename}.doc'
    return locate


def recogntion(request):
    user__ = 1 if 'key' in request.session else 0


    ip_data = get("https://api.ipify.org").text
  
    queryset = ip_tr.objects.filter(ip=ip_data)
    number = 0
    if(queryset.exists()):
        for i in queryset:
            d = i.number+1
        data = ip_tr.objects.get(ip=ip_data)
        data.number = d
        number = d
        data.save()
    else:
        time = ip_tr()
        time.ip=ip_data
        time.number=1
        number = 1
        time.save()
        
    if(number<3 or user__==1):
    
        
        text_frontend = {}
        image = request.FILES['image']
        data = gujrati_files()
        data.email = request.session.get('key', None)
        data.time = datetime.datetime.now().date()
        # data.email = request.session('key')
        data.image = image
        data.save()
        
        filename = str(image)
        filename2 = str(image)
        filename = filename.split(".")
        extension = filename[1]
        filename = filename[0]
        
        tex = ''
        
        
        
        if(extension == 'pdf'):
            tex = tex + check_pdf_path(filename,filename2)
                        
        else:
            im = Image.open(f'Uploaded_Data/{filename2}')
            width = im.size[0]
            height = im.size[1]
            if(width<=1280 and height<=720):
                size = width*3,height*3
            else:
                size = width,height
            im_resized = im.resize(size, Image.ANTIALIAS)
            im_resized.save(f"Uploaded_Data/{filename2}", quality=100)
            img = cv2.imread(f'Uploaded_Data/{filename2}')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(f'Uploaded_Data/{filename2}',gray)
            # tex= tex + pytesseract.image_to_string(Image.open(f'Uploaded_Data/{filename2}'),lang='guj')
            API_KEY = "AIzaSyB8gm7-cGZVBwxDYcCORBvYfWXn3o4quOo"
        
            VISION_URL = "https://vision.googleapis.com/v1/images:annotate?key=" + API_KEY

            # The image you want to analyze
            image_path = f'Uploaded_Data/{filename2}'

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
            request.session['key2'] = tex
            tts = gTTS(text=tex, lang='en-uk')
            tts.save("static/assets/Audio/output.mp3")
            os.system("mpg123 output.mp3")

            # return tex
        
            
        if(os.path.exists('result/pdf')):
            location = save_file(filename,extension,tex)
            
                    
        else:
                parent='result/'
                i_dir = 'img'
                p_dir = 'pdf'
                img_dir = os.path.join(parent,i_dir)
                pdf_dir = os.path.join(parent,p_dir)
                os.mkdir('result')
                os.mkdir(img_dir)
                os.mkdir(pdf_dir)
                location = save_file(filename,extension,tex)
                
        
            
                old_path = f'Uploaded_Data/{filename2}'
            
                if(os.path.exists(f'history/{filename2}')):
                    os.remove(f'history/{filename2}')
                else:
                    pass
                new_path='history/'
                shutil.move(old_path, new_path)
                
                
                # tts = gTTS(text=tex, lang='en-uk')
                # tts.save("static/assets/Audio/output.mp3")
                # os.system("mpg123 output.mp3")
                
        text_frontend.update({'text':tex,
                                'location':location})

        return render(request,'result.html',text_frontend)
    else:
        return redirect('/login')
            