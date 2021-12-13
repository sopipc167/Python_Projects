import requests
from bs4 import BeautifulSoup as bs

class GoogleWeather():
    url='https://www.google.com/search?q={}&rlz=1C1EJFA_enKR770KR770&oq=%EC%86%A1%ED%8C%8C%EA%B5%AC+%EB%82%A0%EC%94%A8&aqs=chrome..69i57.2835j0j8&sourceid=chrome&ie=UTF-8'
    headers = {
        'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }
    result = []
    def __init__(self, keyword=None):
        self.keyword = keyword

    def set_keyword(self, keyword):
        self.keyword = keyword

    def run(self):
        res = requests.get(self.url.format(self.keyword), headers = self.headers)
        self.parse_html(res.text)
        return res
    
    def parse_html(self, text):
        html = bs(text, 'html.parser')
        loc = html.find('div',{'id':'wob_loc'})
        loc = loc.string if loc else loc
        time = html.find('div',{'id':'wob_dts'})
        time = time.string if time else time
        status = html.find('span',{'id':'wob_dc'})
        status = time.string if status else status
        self.result.append({
            'loc':loc,
            'time':time,
            'status':status
        })

    def get_result(self):
        if self.result:
            return self.result[-1]
        else:
            return None

if  __name__ == '__main__':
    crawler = GoogleWeather()
    while True:
        k=input('지역명 >>')
        crawler.set_keyword(k+'날씨')
        crawler.run()
        r=crawler.get_result()
        for v in r.values(): print(v)
        print('-'*50)
