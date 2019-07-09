from django.shortcuts import render

# Create your views here.
def home_page(request):
	context= {
	"msg": "Hello World",
	}
	return render(request, 'home_page.html',context)