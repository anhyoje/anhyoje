#class

title1 = "개발"
author1 = "안효제"
content1 = "개발 공부"
view_count1 = 0

title2 = "복습"
author2 = "안효제"
content2 = "복습 공부"
view_count2 = 0

# class Article:
#     title = "개발"
#     author = "안효제"
#     content = "파이썬 공부"
#     view_count = 0

# article1 = Article()
# article2 = Article()
# print(article1.title)
# article2.view_count = 99
# print(article1.view_count)
# print(article2.view_count)

class Article:
    author = "안효제"
    view_count =  0

    def __init__(self, title, content):
        self.title = title
        self.content = content
    def read(self):
        self.view_count = self.view_count + 1

article1 = Article("개발", "개발 공부")
article1.read()
print(article1.view_count)
