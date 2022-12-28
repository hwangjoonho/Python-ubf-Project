import os
from datetime import datetime
from django.shortcuts import render, redirect
from boards.models import Board

from django.core.paginator import Paginator

import logging
# Create your views here.

# index 페이지
logger = logging.getLogger('mylogger')


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

    # if request.FILES["board_file"]:
    #     board = request.FILES["board_file"]

    #     # 파일 저장시 이름
    #     now = datetime.now()
    #     folder_path = "{0}/{1}/{2}/{3}/{4}/".format('boardfile','sunmsg',now.year,now.month,now.day)
    #     board_field_folder_path = "{0}/{1}/{2}/{3}/".format('sunmsg',now.year,now.month,now.day)
    #     file_name = "{0}_{1}".format(now.strftime("%Y%m%d%H%M%S%f"),board.name)
    #     full_path = folder_path + file_name

    #     # 디렉토리 생성 체크
    #     os.makedirs(folder_path,exist_ok=True)
    #     # 청킹 저장
    #     handle_uploaded_file(board,full_path)

    # # save origin image in database
    #     p = Board(title=title,content=content,name=name,boardfile=board_field_folder_path + file_name)
    # else:
    p = Board(title=title,content=content,name=name)

    p.save()
    print("여기까지완료 successfully uploaded")

    return redirect('/boards/')

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
    paginator = Paginator(board_list, '10')
    page_obj = paginator.page(page) #페이지 번호를 받아 해당 페이지를 리턴 get_page 권장
    return render(request, 'boards/index.html', {'page_obj':page_obj}) 

def detail(request):
    # detail_board = Board.objects.get(name=request.GET.get('name'))
    # detail_board = Board.objects.all()
    no = request.GET.get('no')
    print(no)
    if no != '':
        # objects.all() objects.get 은 querySet타입으로 반환
        # detail_board = Board.objects.filter(boardno = no)
        # print("~~~~~~~~~~~~~s~~s~~~~~info~~~~~~~~~~~")
        # print(detail_board)

        # objects.get() 은 객체타입으로 반환
        detail = Board.objects.get(boardno=no)
        print(request.GET.get('update'))
        print("~~~~~~~~~~~~~~~~")
        print(detail)
        updateyn=request.GET.get('update')
        print("~~~~~~updateyn~~~~~~~~~~")
        print(updateyn)
        print(type(detail))
        print(detail)
        # print("~~~~~~~~~~~~~~~~")
        # print(detail)

    #     print(detail_board)
    #     print(detail_board.values())
    #     print("~~~~~~~~~~~~~s~~~~~~~border~~~~~~~~~~~")
    #     print(detail_board.get('boardno   '))

    # for i in detail_board.boardno:
    #     print(i.boardno)
    #     print("~~~~~~~~~~~~~s~~~~~~~border~~~~~~~~~~~")
    #     print(no)
    #     if i.boardno == no:
    #         print('hi')
            # print(i)
            # board_list = i.values()
            # print(board_list)
    # context = {'detail_board':detail_board,}
    context = {'detail_board':detail,'update':updateyn,}
    return render(request, 'boards/boardDetail.html',context)
    # return render(request, 'boards/boardDetail.html',{'detail_board':detail,})
    # return render(request, 'boards/boardDetail.html',{'detail_board':detail_board,})
