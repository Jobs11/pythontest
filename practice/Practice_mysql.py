import time
import bs4
import urllib.request
import ssl
import sys
import pymysql
import re
from bs4.element import Tag
from tkinter import *
from tkinter import messagebox


ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
d_num, d_category, d_title, d_nickname, d_regdate, d_view, d_recom, d_link = (
    0,
    "",
    "",
    "",
    "",
    0,
    0,
    "",
)
d_content, d_imgurl = "", ""

null = None


def insertData(
    d_num, d_category, d_title, d_nickname, d_regdate, d_view, d_recom, d_link
):
    con, cur = None, None
    data = ""
    data0, data1, data2, data3, data4, data5, data6, data7, data8 = (
        "",
        0,
        "",
        "",
        "",
        "",
        0,
        0,
        "",
    )
    sql = ""

    con = pymysql.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="inven",
        charset="utf8",
    )
    cur = con.cursor()
    data1 = d_num
    data2 = d_category
    data3 = d_title
    data4 = d_nickname
    data5 = d_regdate
    data6 = d_view
    data7 = d_recom
    data8 = d_link
    #
    try:
        # print(null)
        # print(data1)
        # print(data2)
        # print(data3)
        # print(data4)
        # print(data5)
        # print(data6)
        # print(data7)
        # print(data8)
        sql = (
            "INSERT INTO druid (d_num, d_category, d_title, d_nickname, d_regdate, d_view, d_recom, d_link)  VALUES('"
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
            + "','"
            + data7
            + "','"
            + data8
            + "')"
        )
        cur.execute(sql)

    except Exception as e:
        print("예외 발생:", e)
        print("예외 정보:", sys.exc_info())

    else:
        print("게시판 성공")
    con.commit()
    con.close()


def insertimg(d_num, d_imgurl):
    con, cur = None, None
    data = ""
    data0, data1, data2 = (
        "",
        "",
        "",
    )
    sql = ""

    con = pymysql.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="inven",
        charset="utf8",
    )
    cur = con.cursor()
    data1 = d_num
    data2 = d_imgurl
    #
    try:
        print(null)
        print(data1)
        print(data2)
        sql = (
            "INSERT INTO druidimg (d_num, d_imgurl)  VALUES('"
            + data1
            + "','"
            + data2
            + "')"
        )
        cur.execute(sql)

    except Exception as e:
        print("예외 발생:", e)
        print("예외 정보:", sys.exc_info())

    else:
        print("이미지 성공")
    con.commit()
    con.close()


def insertcontent(d_num, d_content):
    con, cur = None, None
    data = ""
    data0, data1, data2 = (
        "",
        "",
        "",
    )
    sql = ""

    con = pymysql.connect(
        host="localhost",
        user="root",
        password="mysql",
        database="inven",
        charset="utf8",
    )
    cur = con.cursor()
    data1 = d_num
    data2 = d_content
    #
    try:
        # print(null)
        # print(data1)
        # print(data2)
        sql = (
            "INSERT INTO druidcontent (d_num, d_content)  VALUES('"
            + data1
            + "','"
            + data2
            + "')"
        )
        cur.execute(sql)

    except Exception as e:
        print("예외 발생:", e)
        print("예외 정보:", sys.exc_info())

    else:
        print("콘텐츠 성공")
    con.commit()
    con.close()


Url = "https://www.inven.co.kr/board/diablo4/6033?p="
page = 1

while True:
    newsUrl = Url + str(page)
    page += 1
    htmlObject = urllib.request.urlopen(newsUrl, context=ssl_context)
    webPage = htmlObject.read()
    bsObject = bs4.BeautifulSoup(webPage, "html.parser")

    tagdiv = bsObject.find("div", {"class": "board-list"})
    tagtbody = tagdiv.find("tbody")
    tagtr = tagtbody.findAll("tr", {"class": ""})
    # print(tagtr)
    for tag in tagtr:
        numcheck = tag.find("td", {"class": "num"})
        d_num = numcheck.find("span").text
        d_category = tag.find("span", {"class": "category"}).text
        d_titlecheck = tag.find("a", {"class": "subject-link"}).text
        d_nickname = tag.find("span", {"class": "layerNickName"}).text
        d_regdate = tag.find("td", {"class": "date"}).text
        d_view = tag.find("td", {"class": "view"}).text.replace(",", "")
        d_recom = tag.find("td", {"class": "reco"}).text
        d_link = tag.find("a", {"class": "subject-link"})["href"]

        pattern = r"\[(.*?)\]\s*(.*)"
        match = re.search(pattern, d_titlecheck)
        if match:
            d_title = match.group(2).rstrip()

            # print(d_title)
        insertData(
            d_num, d_category, d_title, d_nickname, d_regdate, d_view, d_recom, d_link
        )

        # print("번호 = %d" % d_num)
        # print("카테고리 = %s" % d_category)
        # print("제목 = %s" % d_title)
        # print("닉네임 = %s" % d_nickname)
        # print("등록일 = %s" % d_regdate)
        # print("조회 = %d" % d_view)
        # print("추천 = %d" % d_recom)
        # print("링크 = %s" % d_link)

        # html_object2 = urllib.request.urlopen(d_link, context=ssl_context)
        # encoding = html_object2.headers.get_content_charset()
        # web_page2 = html_object2.read().decode(encoding, errors="replace")
        # bs_object2 = bs4.BeautifulSoup(web_page2, "html.parser")

        # tagdiv = bs_object2.find("div", {"id": "powerbbsContent"})

        # # print(tagtr)
        # for tag in tagdiv:
        #     if isinstance(tag, Tag):  # 태그 객체인지 확인
        #         divtag = tag.find_all("div")
        #         for tagd in divtag:
        #             d_content = tagd.text
        #             # print(d_content)
        #             insertcontent(d_num, d_content)

        #         imgtag = tag.find_all("img")
        #         if len(imgtag) > 0:
        #             for tagi in imgtag:
        #                 if "src" in tagi.attrs:
        #                     d_imgurl = tagi["src"]
        #                 elif "data-src" in tagi.attrs:
        #                     d_imgurl = tagi["data-src"]
        #                 else:
        #                     d_imgurl = None

        #                 if d_imgurl:
        #                     # print(d_imgurl)
        #                     insertimg(d_num, d_imgurl)
