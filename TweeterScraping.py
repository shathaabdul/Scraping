import pandas as pd 
from tqdm.notebook import tqdm
import snscrape.modules.twitter as sntwitter

userr=input("Enter the scraping way (tweet , username  ) : ")
Sword=input("what is the word or username do you want to scrap : ")
count=int(input("how many tweet do you want to apper : "))
CsvName=str(input("Enter the csv file name following (.csv) :"))

if userr == "tweet":
    scraper = sntwitter.TwitterSearchScraper(Sword)
elif userr == "username":
    scraper = sntwitter.TwitterUserScraper(Sword)


tweets=[]
for i,tweet in enumerate(scraper.get_items()):
    data= [
    tweet.date,
    tweet.id,
    tweet.rawContent,
    tweet.user.username,
    tweet.likeCount,
    tweet.retweetCount,]

    tweets.append(data)

    if i > count :
        break

tweet_df = pd.DataFrame(
    tweets , columns=[' date ',' id ', ' content ', ' username ',' like_count ' , ' retweet_count ']
)
    
print (tweet_df.to_csv(CsvName))

