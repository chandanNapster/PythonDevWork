from bs4 import BeautifulSoup

html_doc = """<html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
 <body>
  <p class="title">
   <b>
    The Dormouse's story
   </b>
  </p>
  <p class="story">
   Once upon a time there were three little sisters; and their names were
   <a class="sister" href="http://example.com/elsie" id="link1">
    Elsie
   </a>
   ,
   <a class="sister" href="http://example.com/lacie" id="link2">
    Lacie
   </a>
   and
   <a class="sister" href="http://example.com/tillie" id="link3">
    Tillie
   </a>
   ; and they lived at the bottom of a well.
  </p>
  <p class="story">
   ...
  </p>
 </body>
</html>"""

# print(html_doc)
if __name__ == "__main__":

    dom = BeautifulSoup(html_doc, 'html.parser')
    # print(dom.title)
    # #     <title>
    # #    The Dormouse's story
    # #   </title>

    # print(dom.title.name)
    # # 'title'

    # print(dom.title.string)
    # # 'The Dormouse's story'

    # print(dom.title.parent.name)
    # # 'head'

    # print(dom.p)
    # # <p class="title"><b>The Dormouse's story</b></p>

    # print(dom.p['class'])
    # # 'title'

    # print(dom.a)
    # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

    # print(dom.find_all('a'))
    # # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
    # #  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
    # #  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

    # print(dom.find(id="link3"))
    # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

    print(dom.select("p a.sister"))
#     [<a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>, <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>, <a class="sister" href="http://example.com/tillie" id="link3">
#     Tillie
#    </a>]

    print(dom.select("a.sister"))
# [<a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>, <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>, <a class="sister" href="http://example.com/tillie" id="link3">
#     Tillie
#    </a>]
