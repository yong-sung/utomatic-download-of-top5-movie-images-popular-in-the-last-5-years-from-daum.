import requests
from bs4 import BeautifulSoup

for year in range(2017, 2022): # 2017부터 2021까지의 연도 범위를 반복
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    # 'class' 속성이 "thumb_img" 인 모든 '<img>' 태그들을 찾아 리스트로 가져옴
    images = soup.find_all("img", attrs={"class":"thumb_img"})
    
    for idx, image in enumerate(images):
        #print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):
            image_url = "https:" + image_url
            
        print(image_url)
        image_res = requests.get(image_url)
        image_res.raise_for_status()
        
        with open("movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
            f.write(image_res.content)
            
        if idx >= 4: # 상위 5개 이미지까지만 다운로드
            break