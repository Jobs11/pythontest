import time
import bs4
import urllib.request
import ssl
import sys
import pymysql
import re
from tkinter import *
from tkinter import messagebox


ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE
content = ""

null = None


url = "https://www.inven.co.kr/board/diablo4/6033/8713"

while True:
    html_object2 = urllib.request.urlopen(url, context=ssl_context)
    encoding = html_object2.headers.get_content_charset()
    web_page2 = html_object2.read().decode(encoding, errors="replace")
    bs_object2 = bs4.BeautifulSoup(web_page2, "html.parser")

    tagdiv = bs_object2.find("div", {"id": "powerbbsContent"})

    # print(tagtr)
    for tag in tagdiv:
        divtag = tag.find_all("div")
        for tagd in divtag:
            d_content = tagd.text
            # print(tagd.text)

        imgtag = tag.find_all("img")
        print(imgtag)
        if len(imgtag) > 0:
            for tagi in imgtag:
                d_imgurl = tagi["src"]
                # print("이미지: ", img)

        # iframetag = tag.find_all("iframe")
        # print(iframetag)
        # if len(iframetag) > 0:
        #     for tagf in iframetag:
        #         d_imgurl = tagf["src"]
        #         # print("프레임: ", iframe)

    # content = tag.find("div").text
    # print(content)

    # print("번호 = %d" % d_num)
    # print("카테고리 = %s" % d_category)
    # print("제목 = %s" % d_title)
    # print("닉네임 = %s" % d_nickname)
    # print("등록일 = %s" % d_regdate)
    # print("조회 = %d" % d_view)
    # print("추천 = %d" % d_recom)
    # print("링크 = %s" % d_link)

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

    time.sleep(1)
