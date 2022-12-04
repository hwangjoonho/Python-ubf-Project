import os
from datetime import datetime
from django.shortcuts import render, redirect

from boards.models import Board

from django.core.paginator import Paginator

# Create your views here.

# index 페이지
def index2(request):
    # 인덱스페이지에 들어갈 내용
    Boards = Board.objects.all()
    return render(request, 'boards/index.html',{
        'Boards' : Boards
    })

def addmsg(request):
    return render(request, 'boards/addmsg.html')

def msg_save(request):
    print(request.FILES)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(request.POST)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

    title = request.POST["title"]
    content = request.POST["content"]
    name = request.POST["name"]

    board = request.FILES["board_file"]
    print(board)
    print("~~~~~~~~~~~~~~~~")
    # print(board.title+"gkggk")
    # print(board.content+"gkggk")
    # print(board.name+"gkggk")
    # print(board.title+"zzzzzzzsfd")

    
    # 파일 저장시 이름
    now = datetime.now()
    folder_path = "{0}/{1}/{2}/{3}/{4}/".format('boardfile','sunmsg',now.year,now.month,now.day)
    board_field_folder_path = "{0}/{1}/{2}/{3}/".format('sunmsg',now.year,now.month,now.day)
    file_name = "{0}_{1}".format(now.strftime("%Y%m%d%H%M%S%f"),board.name)
    full_path = folder_path + file_name

    # 디렉토리 생성 체크
    os.makedirs(folder_path,exist_ok=True)
    # 청킹 저장
    handle_uploaded_file(board,full_path)

    # save origin image in database
    p = Board(title=title,content=content,name=name,boardfile=board_field_folder_path + file_name)
    p.save()

    return redirect('/boards')

    # file 청킹 업로드 방법
def handle_uploaded_file(f,path):
    with open(path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# def paging(request):
def index(request):
    #models.py의 Board함수를 import하여 리스트들을 가져옴
    board_list = Board.objects.all() #models.py Board 클래스의 모든 객체를 board_list에 담음
    # board_list 페이징 처리
    page = request.GET.get('page', '1') #GET 방식으로 정보를 받아오는 데이터
    #Paginator(분할될 객체, 페이지 당 담길 객체수)
    paginator = Paginator(board_list, '1')
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'boards/index.html', {'page_obj':page_obj}) 
