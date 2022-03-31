# 수정된 프로그램
articles = []

while True :
    cmd = input("=> : ")
    
    if cmd == "help" :
        print("add : 게시물 등록" )
        print("list : 게시물 목록 조회")
    
    elif cmd == "add" :
        title = input("제목을 입력해주세요 : ")
        print(title)
        
        # titles.append(title)
        body = input("내용을 입력해주세요 : ")
        print(body)
        
        # bodys.append(body)
        article = {"title" : title, "body" : body}
        articles.append(article)
        
        
        print("게시물이 저장되었습니다")
    elif cmd == "list" :
        #리스트 필요
        for i in range(len(articles)) :
            target = articles[i]
            print("번호 : {}".format(i+1))
            print("제목 : {}".format(target["title"]))
            print("="*10)
            # print("내용 : {}".format(bodys[i]))
    elif cmd == "update" :                 
        # 3. 내용은 길이가 매우 길 수도 있기 때문에 게시물 목록을 보여줄 때는 보통 보여주지 않습니다. 목록에서 내용을 지워주세요.
        # 4. 올바르지 않은 게시물을 선택하면 게시물이 없다고 나와야 합니다.
        
        re = input("수정할 게시물의 번호를 입력하세요 :")
        re = int(re)
        target_idx = int(re) - 1
        update_target = articles[target_idx]
        if target_idx >= len(articles) :
            print("해당 게시물은 없음")
        else :
            print("번호 : {}".format(re))
            print("제목 : {}".format(articles[target_idx]))
            
        
            retitle = input("새제목 : ")
            rebody = input("새내용 : ")
            update_target["title"] = retitle
            update_target["body"] = rebody
            print("="*10)
           
            print("수정이 완료되었습니다.")  
            print("번호 : {}".format(re))
            print("수정된 제목 : {}".format(articles[target_idx]))
    elif cmd == "delete" :
        no = input("삭제할 게시물 번호를 입력하세요 : ")
        target_idx = int(no) - 1
        if target_idx >= len(articles) :
            print("없는 게시물입니다")
        else :
            del(articles[target_idx])
            print("삭제가 완료되었습니다.")
            
        
            
    elif cmd == "exit" :
        print("프로그램을 종료합니다.")
        break


