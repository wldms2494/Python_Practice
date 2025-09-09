# pypi : 패키지 검색
# beautiful soup : 웹 페이지에서 내가 원하는 정보를 스크랩 해올 수 있음.
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
