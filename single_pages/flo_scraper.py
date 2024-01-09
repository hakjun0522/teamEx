from bs4 import BeautifulSoup
import requests

def get_flo_chart():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }

    url = "https://www.music-flo.com/browse"

    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return []

    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    
    chart_data2 = []

    for items in soup.find_all('tr', {'data-v-44d22190': True}):
        rank = items.find('td',class_='num').get_text(strip=True)
        img = items.find('div',class_='thumb').find('img').get('src')
        title = items.find('p', class_='text_area').find('tit__text').get_text(strip=True)
        artist = items.find('td', class_='artist').find('aritis_link_w').find('aritst__link last').get_text(strip=True)
        album = items.find('p', class_='album').get_text(strip=True)
        chart_data2.append({
            "rank": rank,
            "img": img,
            "title": title,
            "artist": artist,# 여러 가수가 있는 경우를 대비하여 문자열로 결합
            "album": album,
        })
    
    print(chart_data2)
    
    return chart_data2

if __name__ == "__main__":
    print(get_flo_chart())