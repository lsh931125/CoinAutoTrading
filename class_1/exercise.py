# 책을 표현하는 book 클래스 정의.
# book 클래스에는 책 제목, 저자, 역자, 출판사와 같은 정보가 저장.
class book:
    def __init__(self, title, author, translator, publisher):
        self.title = title
        self.author = author
        self.translator = translator
        self.publisher = publisher
        self.all = [self.title, self.author, self.translator,self.publisher]


book1 = book('실전 투자강의','앙드레 코스톨라니','최병연','미래의창')
print(book1.all)