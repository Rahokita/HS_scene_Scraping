import requests, bs4
import csv
#res = requests.get('http://up.illusion.jp/honey_upload/scene/index.php/cPath/26/page/1')
#res.raise_for_status()

#出力用ファイルの設定
file = open('ai_scene.csv', 'a',newline="")
writer = csv.writer(file)
writer.writerow(['date','png_pass', 'author','tytle','comment'])

#htmlファイルの読み込み
testfile = open('AI_source_all.txt','r',encoding = 'utf_8')
html = testfile.read()
testfile.close()

soup = bs4.BeautifulSoup(html, "html.parser")

#elems = soup.select('.caption')
elems = soup.select("[class='list_area clearfix']")
for elem in elems:
    #画像のパスを取得
    link_pass = elem.find(class_="picture")
    tmpstring = link_pass['style']
    png_pass = tmpstring[22:-1]
    print(png_pass)
    png_filename = png_pass.rsplit("/",1)
    tmpstring = png_filename[1]
    png_filename = tmpstring[2:]
    print(png_filename)

    #作成者を取得
    author_tag = elem.find(class_="col-xs-8 handle_name text-right scene_handle_name")
    author_txt = author_tag['title']
    author_txt = author_txt[0:-8] #先頭から末尾８文字までを取り出す
    print(author_txt)

    #タイトルを取得
    tytle_txt = elem.find_all("h3")[0].getText()
    tytle_txt = tytle_txt.strip() #先頭と末尾の不要な空白文字を削除
    print(tytle_txt)

    #コメントを取得
    comment_tag = elem.find(class_="pricebox comment")
    comment_txt = comment_tag['title']
    print(comment_txt)

    #投稿日時を取得
    uploadday_txt = elem.find_all("span")[0].getText()
    tmpstring = uploadday_txt.encode('cp932', "ignore")
    uploadday_txt = tmpstring.decode('cp932')
    uploadday_txt = uploadday_txt.strip() #先頭と末尾の不要な空白文字を削除
    print(uploadday_txt)

    writer.writerow([uploadday_txt,png_filename, author_txt,tytle_txt,comment_txt])

file.close()