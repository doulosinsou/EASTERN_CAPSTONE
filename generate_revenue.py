from generate_stats import generateTime 
import customSQL
from customSQL import custom_SQL
import random
import string

def makeSubscriber():
    letters = string.ascii_letters
    numbers = string.digits
    name = ''.join(random.choice([random.choice(letters),random.choice(numbers)]) for i in range(15))
    com = random.choice(['com','org','net','web'])
    email = name+"@subscriber."+com
    return email

def subscribe(email_list,topic_list,membership):
    Q = custom_SQL()
    price_list = [*[10 for r in range(75)],*[20 for r in range(15)], *[40 for r in range(10)]]
    random.shuffle(price_list)

    for email in email_list:
        customSQL.put_subscriber(Q,email)
        randTopic = random.choice(topic_list)
        randDate = generateTime()
        customSQL.put_subscribes(Q,email,randTopic,membership,randDate)
        if membership == 'Premium':
            if email=='premiumSubscriber2@subs.org':
                continue
            customSQL.put_revenue(Q,email,random.choice(price_list))
    
    Q.commit()
    Q.close()

num_of_subscribers = 400
email_list = [makeSubscriber() for i in range(num_of_subscribers)]


Q = custom_SQL()
topics = customSQL.grab_all_topics(Q)['topic_name']
premium_subs = Q.select("sub_email","Subscribes",{"membership":"Premium"})['sub_email']
Q.close()

num_premium = random.randint(80,150)

basic_subs = email_list[num_premium:]
premium_subs = email_list[:num_premium]



subscribe(basic_subs,topics,'Subscriber')
subscribe(premium_subs,topics,'Premium')