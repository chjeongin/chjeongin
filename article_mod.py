articles = []

def print_articles() :
    for i in range(len(articles)) :
        target = articles[i]
        print("번호 : {}".format(i + 1))
        print("제목 : {}".format(target["title"]))
        print("====================================")


def add_article() :
    
    title = input("제목을 입력해주세요 : ")
    #titles.append(title)
    
    body = input("내용을 입력해주세요 : ")   
    #bodies.append(body)
    
    article = {"title" : title, "body" : body}
    
    articles.append(article)
    print("게시물이 저장되었습니다.")     
    
def update_article() :
    no = input("수정할 게시물 번호 : ")  
    no = int(no)
    target_idx = no - 1 
    
    if target_idx >= len(articles) :
        print("없는 게시물입니다.")
    
    else :
        update_target = articles[target_idx]
        
        new_title = input("새제목 : ")
        new_body = input("새내용 : ")
        
        update_target["title"] = new_title
        update_target["body"] = new_body
        
        print("수정이 완료되었습니다.")
        
        print_articles()

def delete_article() :
    no = input("삭제할 게시물 번호 : ")  
    no = int(no)
    target_idx = no - 1 
    
    if target_idx >= len(articles) :
        print("없는 게시물입니다.")
    
    else :
        del(articles[target_idx])
        print("삭제가 완료되었습니다.")
        
        print_articles()

def print_help() :
    print("add  : 게시물 등록")
    print("list : 게시물 목록 조회")
    print("update : 게시물 수정")
    print("delete : 게시물 삭제")
