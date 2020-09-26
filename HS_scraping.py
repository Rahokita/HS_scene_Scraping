import requests, bs4
import csv


#file = open('hs_scene.csv', 'w',newline="")
file = open('hs_neo_scene.csv', 'a',newline="")
writer = csv.writer(file)
writer.writerow(['png_pass', 'author','tytle','comment','vote'])
    
#res = requests.get('http://up.illusion.jp/honey_upload/scene/index.php/cPath/26/page/1')

for page in reversed(range(1,50)):
    # ループを逆順で回す
    res = requests.get("http://up.illusion.jp/honey_upload/scene02/index.php/cPath/26/page/"+str(page))
           
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    elems = soup.select('.uc_img')



    for elem in elems:
        #画像のパスを取得
        link_pass = elem.find_all("li")[0]
        png_pass = link_pass.find_all("img")[0]
        png_pass = png_pass.get('src')
        print(png_pass)
        png_filename = png_pass.rsplit("/",1)
        print(png_filename[1])

        #作成者を取得
        author_txt = elem.find_all("li")[4]
        author_txt = author_txt.find_all("a")[0].getText()
        tmpstring = author_txt.encode('cp932', "ignore")
        author_txt = tmpstring.decode('cp932')
        print(author_txt)
    
        #タイトルを取得
        tytle_txt = elem.find_all("li")[1].getText()
        tmpstring = tytle_txt.encode('cp932', "ignore")
        tytle_txt = tmpstring.decode('cp932')
        print(tytle_txt)

        #コメントを取得
        comment_txt = elem.find_all("li")[5].getText()
        tmpstring = comment_txt.encode('cp932', "ignore")
        comment_txt = tmpstring.decode('cp932')
        print(comment_txt)

        #拍手数を取得
        vote_txt = elem.find_all("li")[3].getText()
        print(vote_txt)

        writer.writerow([png_filename[1], author_txt,tytle_txt,comment_txt,vote_txt])
    
        r = requests.get(png_pass)
        with open(str('neo_picture/')+str(png_filename[1]),'wb') as png_file:
            png_file.write(r.content)

file.close()

    
