import time
import bs4
import urllib.request
import ssl
import pymysql
from tkinter import *
from tkinter import messagebox


ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
n_imgurl, n_name, n_writer, n_rating, n_day, n_link = "", "", "", "", "", ""

null = None


def insertData(n_imgurl, n_name, n_writer, n_rating, n_day, n_link):
    con, cur = None, None
    data = ""
    data0, data1, data2, data3, data4, data5, data6 = "", "", "", "", "", "", ""
    sql = ""

    con = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="mysql",
        database="webtoon",
        charset="utf8",
    )
    cur = con.cursor()
    data1 = n_imgurl
    data2 = n_name
    data3 = n_writer
    data4 = n_rating
    data5 = n_day
    data6 = n_link
    #
    try:
        print(null)
        print(data1)
        print(data2)
        print(data3)
        print(data4)
        print(data5)
        sql = (
            "INSERT INTO naver (n_imgurl, n_name, n_writer, n_rating, n_day,n_link)  VALUES('"
            + data1
            + "','"
            + data2
            + "','"
            + data3
            + "','"
            + data4
            + "','"
            + data5
            + "','"
            + data6
            + "')"
        )
        print("sql 실행전 ")
        cur.execute(sql)

    except:
        print("예외 발생")
    else:
        print("성공")
    con.commit()
    con.close()


Url = "https://www.inven.co.kr/board/diablo4/6033?p=1"
page = 1

while True:
    newsUrl = Url + str(page)
    page += 1
    htmlObject = urllib.request.urlopen(newsUrl, context=ssl_context)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, "html.parser")

    tagdiv = bsObject.find("div", {"class": "board-list"})
    tagtr = tagdiv.findAll("tr")
    for tag in tagtr:
        num = tag.find("td", {"class": "user"})
        num1 = num.find("span", {"class": "layerNickName"}).text
        print(num1)

    #     print(num1)
    # tag_list = bsObject.findAll("li", {"class": "item"})

    # for tag in tag_list:
    #     n_imgurl = tag.find("img")["src"]
    #     n_namecheck = tag.find("span", {"class": "ContentTitle__title--e3qXt"})
    #     n_name = n_namecheck.find("span", {"class": "text"}).text
    #     n_writer = tag.find("a", {"class": "ContentAuthor__author--CTAAP"}).text
    #     n_ratingcheck = tag.find("span", {"class": "Rating__star_area--dFzsb"})
    #     n_rating = n_ratingcheck.find("span", {"class": "text"}).text
    #     n_link = tag.find("a", {"class": "Poster__link--sopnC"})["href"]
    #     n_link = "https://comic.naver.com/" + n_link

    #     print("이미지 URL:", n_imgurl)
    #     print("웹툰 제목:", n_name)
    #     print("작가:", n_writer)
    #     print("별점:", n_rating)
    #     print("링크:", n_link)

    time.sleep(5)
