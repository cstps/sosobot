from django.shortcuts import render

# Create your views here.
def index(request):
    item = {x for x in range(20)}
    content = {'content':item}
        
    return render(request, 'index.html',content)