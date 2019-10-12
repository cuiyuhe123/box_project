from django.shortcuts import render
# from .models import categoryModels
from . import models
# Create your views here.
def index(request):
    # category = categoryModels.category.objects.get(pk=1)
    category = models.categoryModels.category.objects.get(pk=1)
    print(category);
    print(category.category_name)

    return render(request,'box_app_major/index.html',{'category_name':category.category_name})
