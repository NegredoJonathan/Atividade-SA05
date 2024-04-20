from django.shortcuts import render, redirect
from atividade_sa05_app.forms import UserForm
from atividade_sa05_app.models import User

# Create your views here.
def addnew(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = UserForm()
    return render(request, "index.html",{'form':form})
    
def index(request):
    users = User.objects.all()
    return render(request, "show.html",{'users': users})
    
def edit(request, id):
    user = User.objects.get(id=id)
    return render(request,'edit.html',{'user':user})

def update(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST, instance = user)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request,'edit.html', {'user': user})

def destroy(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect("/")
