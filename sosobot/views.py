from django.shortcuts import render

# Create your views here.
def index(request):
    item = {x:x*x for x in range(1,10)}
    content = {'content':item}
        
    return render(request, 'index.html',content)

