import requests
from bs4 import BeautifulSoup

def which_team(team_name):
    """Alexa Stuff...utterances and stuff """
    team_name = int(team_name)
    return teams[team_name]

def which_stat(stat_name):
    """Alexa Stuff...utterances and stuff """

    #record              | Num points
    #num rating offense
    #num rating defence
    #conference
    #num record wins
    #num record ties
    #num record losses
    #num record goals
    #num record points
    #pct border-left mls  |  Make Playoffs %
    #pct drop-last mls    |  First-Round by %
    #pct drop-first mls   |  Supporter' Shield %
    #pct mls              |  Win MLS %
    stat_name = int(stat_name)
    return stats[stat_name]

url = "https://projects.fivethirtyeight.com/soccer-predictions/mls/"
print "Scraping: ", url, "\n"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

stats = ["record", "num rating offense","num rating defense",
    "conference","num record wins","num record ties","num record losses",
    "num record goals", "num record points","pct border-left mls",
    "pct drop-last mls","pct drop-first mls","pct mls"]

teams = ["Atlanta", "Chicago", "Colorado", "Columbus", "D.C. United",
    "FC Dallas", "Houston", "LA Galaxy", "Minnesota", "Montreal",
    "NY Red Bulls", "NYCFC", "New England", "Orlando City", "Philadelphia",
    "Portland", "Real Salt Lake", "San Jose", "Seattle", "Sporting KC",
    "Toronto FC", "Vancouver"]

for idx, t in enumerate(teams):
    print idx, ":", t
team = raw_input("\nChoose Team: ")

for idx, s in enumerate(stats):
    if(idx == 0):
        print "\n\nStats Over an Average Simulated Season \n______________________________________"
    if(idx == 8):
        print "\nEnd-Of-Season Probabilities\n___________________________"
    print idx, s
stat = raw_input("\nChoose Stat: ")


table = soup.find(id="table")
all_teams = table.find_all(class_="team-div")
order = []

for f in all_teams:
    order.append(f.get_text(separator=u'\n').split('\n')[0])
    # print f.prettify()

# print "\n\n\n\n\nList: ", order
# print "Index: ", order.index(which_team(team))
# print "Stat: ", which_stat(stat)
name = which_team(team)
value = which_stat(stat)
info_row = all_teams[order.index(which_team(team))].parent.parent

print name,value, info_row.find(class_= which_stat(stat)).get_text()
