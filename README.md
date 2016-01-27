# PTTcrawler (PTT文章爬蟲)

A crawler for web PTT 

PTT文章爬蟲
* [Demo Video](https://www.youtube.com/watch?v=qq3kuDU3k50&feature=youtu.be) - Linux

特色
* 抓取PTT 文章

輸出格式
    輸出 .json，格式如下
 

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
    
    
###執行環境
Python 2.7.3

### 執行方法

    $ python pttcrawler.py [版名]  [抓取頁數]
    
### 範例
  爬PTT Gossiping版 2頁 文章內容

    $ python pttcrawler.py  Gossiping  2
    
  假設總共有100頁，則會爬取
  
  https://www.ptt.cc/bbs/Gossiping/index100.html 至 https://www.ptt.cc/bbs/Gossiping/index101.html 之間的內容。
    
