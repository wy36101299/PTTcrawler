PTTcrawler
==========

A crawler for web PTT Gossiping

ptt八卦版的網路爬蟲，解析其中資料，爬完會自動產生 data.json 
json的格式如下

    "a_ID": 編號,
    "b_作者": 作者名,
    "c_標題": 標題,
    "d_日期": 發文時間,
    "e_ip": 發文ip,
    "f_內文": 內文,
    "g_推文": {
        "推文編號": {
            "狀態": 推 or 噓 or →,
            "留言內容": 留言內容,
            "留言時間": 留言時間,
            "留言者": 留言者
        }
    },
    "h_推文總數": {
        "all": 推文數目,
        "b": 噓數,
        "g": 推數,
        "n": →數
    }

###如何使用
--------------

    $ python pttcrawler.py start end

start 和 end 是網址index的數字
https://www.ptt.cc/bbs/Gossiping/index.html
可自由決定要爬取的index範圍
example

--------------

    $ python pttcrawler.py 200 500
    
則會爬取
https://www.ptt.cc/bbs/Gossiping/index200.html 至
https://www.ptt.cc/bbs/Gossiping/index500.html
之間的內容。
    
