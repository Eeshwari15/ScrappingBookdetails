import requests
from pages.all_books_page import AllBooksPage
page_content=requests.get("http://books.toscrape.com/").content
page=AllBooksPage(page_content)
books=page.books
#for book in books:
 #   print(book)
for page_number in range(1,page.page_count):
    url=f'http://books.toscrape.com/catalogue/page-{page_number+1}.html'
    page_content=requests.get(url).content
    page=AllBooksPage(page_content)
    books.extend(page.books)
