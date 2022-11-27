from django.shortcuts import render

# Create your views here.

# index 페이지
def index(request):
    # 인덱스페이지에 들어갈 내용
    title = "사진첩"
    span = "경성2부의 추억이 담긴 사진첩"
    return render(request, 'galleries/index.html', {
        "page_title": title,
        "span" : span
    })

def events(request):
    title = "주제별 사진"
    span = "원하는 주제를 선택하세요"
    return render(request, 'galleries/events.html', {
        "page_title": title,
        "span" : span
    })