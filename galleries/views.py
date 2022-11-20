from django.shortcuts import render

# Create your views here.

# index 페이지
def index(request):
    # 인덱스페이지에 들어갈 내용
    title = "사진첩"
    return render(request, 'galleries/index.html', {
        "page_title": title
    })