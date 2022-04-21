import customSQL
from customSQL import custom_SQL

import random 
import math 
import numpy as np
import time

def generateTime(startdate='2020-01-01 00:01:01', enddate='2021-12-30 23:59:59'):
    """
    Suggested time module usage by Tom Alsburg 2009-02-16
    https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    """
    def convert(datestr):
        strip = time.strptime(datestr,'%Y-%m-%d %H:%M:%S')
        return time.mktime(strip)

    startdate = convert(startdate)
    enddate = convert(enddate)
    randtime = startdate + random.random() * (enddate - startdate)
    newtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(randtime))
    return newtime


if __name__=="__main__":
    Q = custom_SQL()
    article_ids = Q.select("article_ID","Post")['article_ID']

    print(article_ids)

    num = 2000
    random_IP = ['.'.join([str(random.randrange(200,800,10)) for r in range(4)]) for i in range(num)]

    # two thousand IP_addresses over the course of two years
    # each IP_address visits up to 10 pages up to 10(ish) times each
    # takes about 40minutes. can be faster by better opening/closing cursors
    simulate_update=[]
    for viewer in random_IP:
        num_of_pages = random.randint(1,10)
        for visits in [math.ceil(np.random.normal(0,1)**2) for r in range(num_of_pages)]:
            article = random.choice(article_ids)
            for v in range(visits):
                randtime = generateTime()
                simulate_update.append((viewer,article,randtime))
                customSQL.put_stat(Q,article,viewer,randtime)
    Q.commit()
    Q.close()
    simulate_update.sort()
    print(simulate_update)




