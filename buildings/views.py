from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from .models import *
from .forms import *


def main(request):
    form = TellSomething()
    data = MainPageData.objects.all().values
    projects = ProjectsDone.objects.all().values
    template = loader.get_template("main.html")
    context = {
        "data": data,
        "projects": projects,
        "email": "kemuntoJudy@gmail.com",
        "tel_no": "0718703405",
        "form": form,
    }
    if request.method == 'POST':
    	form = TellSomething(request.POST)
    	if form.is_valid():
    		userInput = form.cleaned_data['userInput']
    		send_mail(
    			subject=userInput[:10],
    			message=userInput,
    			recipient_list=['kemuntoJudy@gmail.com']
    		)
    return HttpResponse(template.render(context, request))

