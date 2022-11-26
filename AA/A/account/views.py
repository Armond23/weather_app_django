from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from  .forms import UserRegistrationsForm
from django.contrib.auth.models import User
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin

class UserRegisterView(View):
    form_class=UserRegistrationsForm
    template_name = 'account/register.html'
    
    def get(self, request):
        form=self.form_class
        return render(request, self.template_name, {'form':form})
        
        
    def post(self, request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'you registered successfully', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form':form})
            
            
