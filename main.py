import requests
from bs4 import *
#pip install lxml
#pip install bs4

def getScore():
    url='https://www.cricbuzz.com/cricket-match/live-scores'
    res = requests.get(url)
    status_code = res.status_code
    data = res.content
    soup = BeautifulSoup(res.content,'lxml')
    league_tab = soup.find('div',{
        'ng-show':"active_match_type == 'league-tab'"
        })
    print("-------------")
    if league_tab:
        # print("inside----")
        match_id=league_tab.find('h3',{'class' : 'cb-lv-scr-mtch-hdr'}).find('a')['href'].split('/')[2]

    cricbuzz_api = 'https://www.cricbuzz.com/api/cricket-match/commentary/{}'.format(match_id)
    # print(match_id)
    res = requests.get(cricbuzz_api)
    commentary = res.json()['commentaryList']
    for comm in commentary:
        try:
            if 'overSeparator' in comm:
                # print(comm,"------")
                score = comm['overSeparator']['score']
                wickets = comm['overSeparator']['wickets']
                summary = comm['overSeparator']['o_summary']
                over = comm['overSeparator']['overNum']
                batteam = comm['overSeparator']['batTeamName']
                break
        except :
            score,summary,over,batteam,wickets = None
    result  = f'{batteam} {score}/{wickets} ({over})\nThis over: {summary}'

    return print(result)
    #test commit


if __name__  == "__main__":
    getScore()
