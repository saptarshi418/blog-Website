from django.shortcuts import redirect, render
from .models import WriteBlog 
from .models import Categories
from .forms import BlogForm , UserRegistrationForm , UserLoginForm
from django.shortcuts import get_object_or_404
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login , authenticate , logout
from django.contrib import messages



def index(request ):
    category = Categories.objects.all()
    blogs = WriteBlog.objects.all().order_by('-created_at')
    data = {
        'categories': category ,
        'blogs':blogs,
    }

    if request.method == 'POST':
        blogs = WriteBlog.objects.filter(category=category).order_by('-created_at')
        return render(request, 'index.html',data)

    return render(request, 'index.html',data)






@login_required
def create_blog(request):
    
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
          blog = form.save(commit=False)
          blog.user = request.user
        #   blog.user = User.objects.first()
          blog.save()
          return redirect('home')
   
    else:
        form = BlogForm()
    return render(request,'blog_form.html',{'form':form})

@login_required
def blog_edit(request , blog_id):
    blog = get_object_or_404(WriteBlog , pk = blog_id ,user = request.user)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES , instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            
            blog.user = request.user
            blog.save()
            return redirect('home')
    else:
        form = BlogForm(instance=blog)
    return render(request,'blog_form.html',{'form':form})


@login_required
def blog_delete(request, blog_id):
    blog = get_object_or_404(WriteBlog , pk = blog_id , user = request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect ('home') 
    return render(request,'blog_confirm_delete.html',{'blog':blog})


def register(request):
    if request.user.is_authenticated:
        return redirect('home')   #redirect the user if loggedin
     
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegistrationForm()

    return render(request,'registrations/register.html',{'form':form})
        
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')   #redirect the user if loggedin
    
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()  # Initialize the form for GET requests

    return render(request, 'registrations/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home') 
           
def blog_view(request, blog_id):
    blog = get_object_or_404(WriteBlog, id=blog_id)
    return render(request, 'blog_view.html', {'blog': blog})
