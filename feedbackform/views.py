from django.shortcuts import render
from .form import FeedbackForm
from .models import Formdata

# Create your views here.
def feedback(request):
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']

            formdata=Formdata()
            formdata.name=name
            formdata.email=email
            formdata.save()

            return render(request, "feedbackform.html", {'form':form})
        else:
            return render(request, "feedbackform.html", {'form':form}) 
    else:
        form=FeedbackForm()
        return render(request, "feedbackform.html", {'form':form})


