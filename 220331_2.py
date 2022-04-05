# 명령어를 입력해주세요 : (출력) help(입력)
# add  : 게시물 등록 (출력)
# list : 게시물 목록 조회 (출력)
# 명령어를 입력해주세요 : (출력) add(입력)
# 제목을 입력해주세요 : (출력) 안녕하세요(입력)
# 내용을 입력해주세요 : (출력) 반갑습니다(입력)
# 게시물이 저장되었습니다. (출력)
# 명령어를 입력해주세요 : (출력) list(입력)
# 번호 : 1(출력)
# 제목 : 안녕하세요(출력)
# 내용 : 반갑습니다(출력)
# ====================================(출력)
# 명령어를 입력해주세요 : (출력) add(입력)
# 제목을 입력해주세요 : (출력) 안녕하세요2(입력)
# 내용을 입력해주세요 : (출력) 반갑습니다2(입력)
# 게시물이 저장되었습니다. (출력)
# 명령어를 입력해주세요 : (출력) list(입력)
# 번호 : 1(출력)
# 제목 : 안녕하세요(출력)
# 내용 : 반갑습니다(출력)
# ====================================(출력)
# 번호 : 2(출력)
# 제목 : 안녕하세요2(출력)
# 내용 : 반갑습니다2(출력)
# ====================================(출력)



titles = []
bodys = []

while True :
    cmd = input("=> : ")
    
    if cmd == "help" :
        print("add : 게시물 등록" )
        print("list : 게시물 목록 조회")
    elif cmd == "add" :
        title = input("제목을 입력해주세요 : ")
        print(title)
        titles.append(title)
        body = input("내용을 입력해주세요 : ")
        print(body)
        
        bodys.append(body)
        print("게시물이 저장되었습니다")
    elif cmd == "list" :
        #리스트 필요
        for i in range(len(titles)) :
            print("번호 : {}".format(i+1))
            print("제목 : {}".format(titles[i]))
            print("내용 : {}".format(bodys[i]))
    elif cmd == "update" :                 
        # 3. 내용은 길이가 매우 길 수도 있기 때문에 게시물 목록을 보여줄 때는 보통 보여주지 않습니다. 목록에서 내용을 지워주세요.
        # 4. 올바르지 않은 게시물을 선택하면 게시물이 없다고 나와야 합니다.
        
        re = input("수정할 게시물의 번호를 입력하세요 :")
        
        if (re-1) > range(len(titles)) :
            print("해당 게시물은 없음")
        else :
            print("번호 : {}".format(re))
            print("제목 : {}".format(titles[int(re)-1]))
        # print("내용 : {}".format(bodys[int(re)-1]))
        
        retitle = input("현재 제목 : ")
        rebody = input("현재 내용 : ")
        titles[int(re)-1] = retitle
        bodys[int(re)-1] = rebody
        print("수정이 완료되었습니다.")  
        print("번호 : {}".format(re))
        print("수정된 제목 : {}".format(titles[int(re)-1]))
        print("수정된 내용 : {}".format(bodys[int(re)-1]))
    elif cmd == "exit" :
        print("프로그램을 종료합니다.")
        break



# 5개 값 입력받아서 저장하기


