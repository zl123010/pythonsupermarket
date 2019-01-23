from django.shortcuts import render

# Create your views here.
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'commodity/index.html')

    def post(self, request):
        pass


class DetailView(View):
    def get(self, request):
        return render(request, 'commodity/detail.html')

    def post(self, request):
        pass


class CategoryView(View):
    def get(self, request):
        return render(request, 'commodity/category.html')

    def post(self, request):
        pass