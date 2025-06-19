from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

# Create your views here.

def index(request):
    #查詢所有資料庫與資料庫裡面的所有資料
    article_records = Post.objects.all()
    #article_records = [(...),(...), (...), ]

    # 處理查詢結果
    article_list = list()
    for count, article in enumerate(article_records):  #用for迴圈處理每一筆資料的內容
        #article_records[count].title => article.title
        article_list.append("#{}: {}<br><hr>".format(str(count), str(article.title)))
        #如果程式碼出錯，先檢查有無縮排
        article_list.append("<small>{}<small><br><hr>".format(article.content))#新增文章內容，縮小文字
        article_list.append("slug: {}<br><hr>".format(str(article.slug)))

    return HttpResponse(article_list)

def about(request):
    return HttpResponse("hello world")


from datetime import datetime
def index_use_template(requests): 
    article_records = Post.objects.all()
    now = datetime.now()
    # return render(requests, "index.html", locals()) #把當前時間變成字串塞入函式裡面

def index_use_template(requests):
    article_records = Post.objects.all()
    now = datetime.now()
    # return render(requests, "index.html", locals())
    return render(requests, 'pages/home.html', locals())

# ... (略: 其他程式碼維持不變) ...
def showPost(requests, slug):
    article = Post.objects.get(slug=slug)
    return render(requests, 'pages/post.html', locals())

def login(requests):
    return render(requests, 'pages/login.html')
    # list_data = [
    #     '1',
    #     '2',
    #     '3'
    # ]

    # dict_data = {
    #     'key' : value #key是字串，value看要打甚麼
    # }
    # dict_data['data']



#用locals，把當前變數名稱變為key，把它打包起來

# <br> 空一行
# <hr>分隔線

# def 名稱()
#     計算
#     return 結果
# a = 名稱(參數) 

#使用者可控制url，我們使用url.py去調整

