from django.shortcuts import render

# Create your views here.


# index 페이지
def index(request):
    # 인덱스페이지에 들어갈 내용
    return render(request, 'contents/index.html')