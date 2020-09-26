import requests, bs4
#res = requests.get('http://up.illusion.jp/honey_upload/scene/index.php/cPath/26/page/1')
#res.raise_for_status()

html = """
<html>
<body>
<ul class="uc_img">				
	<li>			
		<a href="http://up.illusion.jp/honey_upload/scene/download.php/security/honey0004115/products_id/4115/cPath/26">		
			<img src=http://up.illusion.jp/honey_upload/scene/upimg/honey0004115.png class="wider">	
		</a>		
	</li>			
	<li>ジャンプ回転斬り</li>			
	<li>			
		<a href="http://up.illusion.jp/honey_upload/scene/download.php/security/honey0004115/products_id/4115/cPath/26">		
			<img src="images/contest_list/dl26.png" width="240" height="30" border="0" alt="download">	
		</a>		
	</li>			
	<li>			
		<a href="http://up.illusion.jp/honey_upload/scene/index.php/cPath/26/check_id/4115/page/1">		
			<img src="images/contest_list/evaluation.png" width="60" height="20" border="0"	>
		</a><br>20		
	</li>			
	<li>			
		<a href="http://up.illusion.jp/honey_upload/scene/index.php/cPath/26/name/%25C9%25D4%25C7%25D4%25A4%25CE%25B5%25ED%25BB%25B3/">不敗の牛山</a>		
	</li>			
	<li>剣の重さを意識した風にしてます。</li>			
</ul>				
</body>
</html>
"""

soup = bs4.BeautifulSoup(html, "html.parser")
#soup = bs4.BeautifulSoup(res.text, "html.parser")
#elems = soup.select('h2')
elems = soup.select('.uc_img')
for elem in elems:
    #画像のパスを取得
    link_pass = elem.find_all("li")[0]
    png_pass = link_pass.find_all("img")[0]
    print(png_pass.get('src'))
    
    #タイトルを取得
    tytle_txt = elem.find_all("li")[1].getText()
    print(tytle_txt)
    #コメントを取得
    comment_txt = elem.find_all("li")[5].getText()
    print(comment_txt)

    author_txt = elem.find_all("li")[4]
    author_txt = author_txt.find_all("a")[0].getText()
    print(author_txt)

    #print(elem.find_all("li")[0])

    
