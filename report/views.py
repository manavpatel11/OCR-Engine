from django.shortcuts import render
from recognition_app.models import gujrati_files
def reportpage(request):
    gj = list(gujrati_files.objects.filter(email = request.session.get('key', None)).values())
    date = []
    name = []
    filename = []
    l = []
    for i in range(len(gj)):
        
        date.append(gj[i]['time'])
        name.append(gj[i]['email'])
        filename.append(gj[i]['image'])
        
        
        

    
    prm = zip(date,name,filename)
    
    
    print("---------------------------------------------------------")
    
    data = {
        'pr':prm
    }
    
    
    return render(request,'report.html',data)