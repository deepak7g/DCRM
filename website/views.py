from django.shortcuts import render,redirect
from django.contrib.auth  import authenticate, login, logout 
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import dcrmDb2
# Create your views here.

def home(request):
    records = dcrmDb2.objects.all()
    #checking to see loging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticatiing
        user = authenticate(request,  username = username,password = password)
        if user is not None:
            login(request, user)
            messages.success(request, "Success fully loged in....")
            return redirect('home')
        else:
            messages.success(request, "There was an error please try again" )
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logoutUser(request):
    logout(request)
    messages.success(request, "you are loged out...")
    return redirect('home')

def registerUser(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customerRecord(request, pk):
    if request.user.is_authenticated:
        customerRecord = dcrmDb2.objects.get(id=pk)
        return render(request, 'record.html', {'customerRecord': customerRecord})
    else:
        messages.success(request, "Must be logged in")
        return redirect('home')


def deleteRecord(request, pk):
    if request.user.is_authenticated:
        deleteIt = dcrmDb2.objects.get(id=pk)
        deleteIt.delete()
        messages.success(request, "Record Deleted ")
        return redirect('home')
    else:
        messages.success(request, "Must be logged in")
        return redirect('home')


def addRecord(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
         if request.method == "POST":
              if form.is_valid():
                   addRecord = form.save()
                   messages.success(request, "Ewcord Added....")
                   return redirect('home')
         return render(request, 'addRecord.html', {'form':form})
    else:
        messages.success(request, "Must be logged in")
        return redirect('home')
    
def UpdateRecord(request, pk):
    if request.user.is_authenticated:
        currentRecord = dcrmDb2.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=currentRecord)
        if form.is_valid():
             form.save()
             messages.success(request, "Record has been Updated.....")
             return redirect('home')
        return render(request, 'UpdateRecord.html', {'form':form})
    else:
        messages.success(request, "Must be logged in")
        return redirect('home')
         