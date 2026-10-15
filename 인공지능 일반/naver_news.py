from bs4 import BeautifulSoup
import requests
import pandas as pd


def naver_news_store(result):
    url = 'https://news.naver.com/breakingnews/section/105/229'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
    
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    news_items = soup.select('li.sa_item')

    for item in news_items[:10]:
        title_tag = item.select_one('strong.sa_text_strong')
        link_tag = item.select_one('a.sa_text_title')
        press_tag = item.select_one('div.sa_text_press')

        if not title_tag or not link_tag:
            continue

        title = title_tag.text.strip()
        link = link_tag['href']
        press = press_tag.text.strip() if press_tag else "언론사 미상"

        print(f"URL: {link}")

        result.append([title, press, link])

    return


def main():
    result = []
    print('Naver News crawling >>>>>>>>>>>>>>>>>>>>>>>>>')
    naver_news_store(result)

    news_tbl = pd.DataFrame(result, columns=('title', 'press', 'link'))
    news_tbl.to_csv('./naver_news_top10.csv', encoding='utf-8-sig', index=True)
    print('./naver_news_top10.csv 파일저장 완료 >>>>>>>>>>>>>>>>>>')


if __name__ == '__main__':
    main()