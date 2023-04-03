from django.shortcuts import render
from registration.models import users_data
from django.shortcuts import redirect


def register(request):
    if(request.method=="POST"):
        
        try:
            j = users_data.objects.filter(email = request.POST['email'])
            j = dict(j)
            if(j=={}):
                u = users_data()
                u.email = request.POST['email']
                u.password = request.POST['pass']
                u.wallet = request.POST['soltext']
                u.save()
                request.session['key'] = request.POST['email']
                return redirect('/')
        except:
                pass

    else:
        print('hii3')
        pass
        
    return render(request,'registration.html')

    
def login(request):

    if(request.method=="POST"):
        try:
            data = users_data.objects.filter(email=request.POST['email']).values()
            data = dict(data)

            if(data == {}):
                print("hello3")
                return redirect('/register')
            else:
                print("hello2")
                pass
        except:
            if(data[0]['password'] == request.POST['pass']):
                request.session['key'] = request.POST['email']
                
                return redirect('/homepage')
            

    return render(request,'login.html')