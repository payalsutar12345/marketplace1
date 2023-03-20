from django.shortcuts import render,redirect
from item.models import Category,Item

from .forms import SignupForm

# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()

    return render(request,'core/index.html',{
        'categories':categories,
        'items':items,
    })

def contact(request):
    return render(request,'core/contact.html')

# def signup(request):
#     if request.method =='POST':
#         form=SignupForm(request.POST)

#         if form.is_valid():
#             form.save()

#             return redirect('/login/')
#     else:
#         form=SignupForm()    

#     return render(request,'core/signup.html',{'form':form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)

            # redirect user to home page
            return redirect('/login')
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})
     