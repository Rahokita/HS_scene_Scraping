import requests, bs4
#res = requests.get('http://up.illusion.jp/honey_upload/scene/index.php/cPath/26/page/1')
#res.raise_for_status()

html = """
<html>
<body>
        <!--▼作品-->
        <div class="list_area clearfix" >
          <div class="thumbnail row">

            <!--★クリップ★-->
            <div class="scene-img">
              <!--★ダウンロードボタン★-->
              <a href="?path_image=https://aishoujo-img.s3-ap-northeast-1.amazonaws.com/scene/image/upai_scene_0002350.png&idx=2350&mode=download"id="2350"class="download-link">
                <!--★画像★-->
                <div id="img2350"class="picture"style="background-image: url(https://aishoujo-img.s3-ap-northeast-1.amazonaws.com/scene/thumb/s_upai_scene_0002350.png)">
                </div>
              </a>
            </div>

            <!--▼作品ステータス-->
            <div class="caption">
              <!--★作品タイトル★-->
              <h3>体格差H　丼（男なし）</h3>
              <!--★コメント★-->
              <div class="pricebox comment"data-toggle="tooltip"title="久々に遊んだら、勢いでできてしまった…。マップお借りしました。">
                <div class="row">
                  <div class="col-xs-12 short--scene">
                    久々に遊んだら、勢いでできてしまった…。<br />マップお借りしました。
                  </div>
                </div>
              </div>

              <div class="pricebox customer_name">
                <div class="container-fluid">
                  <div class="row">
                    <!--★投稿日時(更新日時)★-->
                      <div  class="col-xs-4 time">
                        <span class="">
                          2020/9/26 - 12:22
                        </span>
                      </div>
                    <!--★ハンドルネーム★-->
                      <div class="col-xs-8 handle_name text-right scene_handle_name" data-toggle="tooltip" title="白帽子の投稿作品を検索">
                        <a href="?&handle_name[]=白帽子">
                          <div>
                            by 白帽子
                          </div>
                        </a>
                      </div>
                  </div>
                </div>
              </div>

            </div>
            <!--▼作品ステータス-->
          </div>
        </div>
        <!--▲作品-->			
</body>
</html>
"""
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
    print(png_filename[1])

    #作成者を取得
    author_tag = elem.find(class_="col-xs-8 handle_name text-right scene_handle_name")
    author_txt = author_tag['title']
    author_txt = author_txt[0:-8] #先頭から末尾８文字までを取り出す
    print(author_txt)

    #タイトルを取得
    tytle_txt = elem.find_all("h3")[0].getText()
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
