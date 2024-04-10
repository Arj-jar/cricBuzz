import requests
from bs4 import *
#pip install lxml
#pip install BeautifulSoup

def getScore():
    url='https://www.cricbuzz.com/cricket-match/live-scores'
    res = requests.get(url)
    status_code = res.status_code
    data = res.content
    soup = BeautifulSoup(res.content,'lxml')
    league_tab = soup.find('div',{
        'ng-show':'active_match_type' == 'league-tab'
        })
    print("-------------")
    if league_tab:
        match_id=league_tab.find('h3',{
            'class' : 'cb-lv-scr-mtch-hdr'
        }).find('a')['href'].split('/')[2]

    cricbuzz_api = 'https://www.cricbuzz.com/api/cricket-match/commentary/{}'.format(match_id) 
    res = requests.get(cricbuzz_api)
       
    return 1

if __name__  == "__main__":
    getScore()
