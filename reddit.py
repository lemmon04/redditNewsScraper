import praw
import cookielib
from cookielib import CookieJar
import urllib2
import time
import re
from re import sub

#Fill in client_id & client_secret
reddit = praw.Reddit(client_id='ix5wCAjGqQrXmQ',
                     client_secret='XC19Gng-5R3PQf2OorSf29DlnWY',
                     user_agent='sumac')

#get 10 submissions from hot
#print url and id number
subreddit = reddit.subreddit('politics')
for submission in subreddit.hot(limit=10):
    print submission.url + "\n\n"
    #print submission.id
    
#Get comments from submission  
#URL guidelines ('https://www.reddit.com/r/subreddit/comments/ID/page
#submission = reddit.submission(url='http://thehill.com/homenews/administration/388855-60-minutes-correspondent-trump-said-he-attacks-the-press-so-no-one8lcv0g')
#for top_level_comment in submission.comments:
 #   print(top_level_comment.body) + "\n"


cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')]

def NYT():
    try:
        sourceCode = opener.open('https://www.nytimes.com/aponline/2018/05/22/us/politics/ap-us-pruitt-epa-the-latest.html').read()
        splitSource = re.findall(r'<p class="css-1cy1v93 e2kc3sl0">(.*?)</p>',sourceCode)
        for item in splitSource:
            item = item.replace("&quot;", '"')
            item = item.replace("&#x27;", "'")
            aTweet = re.sub(r'<.*?>','',item) + "\n"
            print aTweet

    except Exception, e:
        print str(e)
        print 'errored in the main try'
        time.sleep(555)

def Jpost ():
    try:
        sourceCode = opener.open('https://www.jpost.com/American-Politics/US-Special-Counsel-Robert-Mueller-sent-agents-to-Israel-in-Trump-probe-557903').read()
        splitSource = re.findall(r'<br/><br/>(.*?)<br/><br/>',sourceCode)
        for item in splitSource:
            item = item.replace("&rdquo;", '"')
            item = item.replace("&rsquo;", "'")
            item = item.replace("&ldquo;", '"')
            item = item.replace("&ndash;", '-')
            aTweet = re.sub(r'<.*?>','',item) + "\n"
            print aTweet

    except Exception, e:
        print str(e)
        print 'errored in the main try'
        time.sleep(555)

def TheAtlantic ():
    try:
        sourceCode = opener.open('https://www.theatlantic.com/politics/archive/2018/05/collusion-happened/560894/').read()
        splitSource = re.findall(r'<p>(.*?)</p>',sourceCode)
        for item in splitSource:
            item = item.replace("&rdquo;", '"')
            item = item.replace("â€™", "'")
            item = item.replace("&ldquo;", '"')
            item = item.replace("&ndash;", '-')
            aTweet = re.sub(r'<.*?>','',item) + "\n"
            print aTweet

    except Exception, e:
        print str(e)
        print 'errored in the main try'
        time.sleep(555)

def WaPo ():
    try:
        sourceCode = opener.open('https://www.washingtonpost.com/news/global-opinions/wp/2018/05/24/surprise-donald-trump-is-terrible-at-diplomacy/?utm_term=.1ed964fe3f80').read()
        print sourceCode
        splitSource = re.findall(r'<p>(.*?)</p>',sourceCode)
        for item in splitSource:
            item = item.replace("&rdquo;", '"')
            item = item.replace("â€™", "'")
            item = item.replace("&ldquo;", '"')
            item = item.replace("&ndash;", '-')
            aTweet = re.sub(r'<.*?>','',item) + "\n"
            print aTweet

    except Exception, e:
        print str(e)
        print 'errored in the main try'
        time.sleep(555)

def WA_Monthly ():
    try:
        sourceCode = opener.open('https://washingtonmonthly.com/2018/05/24/why-i-hold-trump-voters-accountable-for-the-mess-were-in/').read()
        splitSource = re.findall(r'<p>(.*?)</p>',sourceCode)
        for item in splitSource:
            item = item.replace("&#8220;", '"')
            item = item.replace("&#8217;", "'")
            item = item.replace("&#8221;", '"')
            item = item.replace("â€”", '-')
            item = item.replace("&#8230;", '...')
            aTweet = re.sub(r'<.*?>','',item) + "\n"
            print aTweet

    except Exception, e:
        print str(e)
        print 'errored in the main try'
        time.sleep(555)


def WSJ ():
    try:
        sourceCode = opener.open('https://www.wsj.com/articles/roger-stone-sought-information-on-clinton-from-assange-emails-show-1527191428?mod=searchresults&page=1&pos=1').read()
        splitSource = re.findall(r'<p>(.*?)</p>',sourceCode)
        for item in splitSource:
            item = item.replace("&#8220;", '"')
            item = item.replace("â€™", "'")
            item = item.replace("&#8221;", '"')
            item = item.replace("â€”", '-')
            item = item.replace("&#8230;", '...')
            aTweet = re.sub(r'<.*?>','',item) + "\n"
            print aTweet

    except Exception, e:
        print str(e)
        print 'errored in the main try'
        time.sleep(555)
WSJ()


