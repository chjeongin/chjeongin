import article_mod as am
import article_mod as am
# 함수와 변수가 너무 많으면 코드를 읽기 어려워지고 관리가 힘들어진다.
# 일련의 코드들을 외부 파일로 빼서 관리하면 이를 해결할 수 있다.
# 외부코드를 모듈이라고 부르고 필요하면 import로 불러와서 사용할 수 있다.

while True :
    cmd = input(">> ")
    
    if cmd == "help" :
        am.print_help()
        
    elif cmd == "exit":
        print("프로그램을 종료합니다.")
        break 
    
    elif cmd == "add" :
        am.add_article() 
        
    elif cmd == "list" :
        am.print_articles()
            
    elif cmd == "update" :
        am.update_article()
            
    elif cmd == "delete" :     
        am.delete_article()
        
    else :
        print("알 수 없는 명령어. 명령어 목록을 보시려면 help를 입력하세요")


