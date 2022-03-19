# -*- coding: utf-8 -*-

import tweepy
import os

bearer_token = os.environ["TWITTERBTC_BEARER_TOKEN"]
consumer_key = os.environ["TWITTERBTC_CONSUMER_KEY"]
consumer_secret = os.environ["TWITTERBTC_CONSUMER_SECRET"]
access_token = os.environ["TWITTERBTC_TOKEN_KEY"]
access_token_secret = os.environ["TWITTERBTC_TOKEN_SECRET"]

query = '(biotec OR #biotec OR biotecnologia OR #BIOTEC) (unila OR #UNILA OR #unila OR UNILA) -is:retweet -lixo -comunista -ridiculo'

tweet_text = "\U0001F947 Você sabia que o Curso de Bacharelhado em Biotecnologia - UNILA é nota 5 na avaliação do MEC? https://portal.unila.edu.br/noticias/cursos-da-unila-obtem-notas-4-e-5-em-avaliacao-do-mec Você pode conferir mais sobre o curso aqui: https://portal.unila.edu.br/graduacao/biotecnologia/ppc"
tweet_text2 = "Além disso, você pode conversar com estudantes de diferentes iniciativas (pelo Instagram), como: Centro Acadêmico (cabiotec.unila), Time de Biologia Sintética (igem_synfronteras), Empresa Junior (latinabiotecjr), Atlética Esportiva (atleticaacbio) e a LiNA (Liga Nac. de Estudantes de Biotec - biotecnologiaunila)"
Myusername = "BiotecUnilaBOT"

#Utilitarios
def getClient():
  client = tweepy.Client(bearer_token=bearer_token, consumer_key= consumer_key, 
                       consumer_secret = consumer_secret, access_token=access_token, 
                       access_token_secret=access_token_secret)
  return client

def SearchTweet(query):
  return getClient().search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=10)

def Retweet(ID):
  return getClient().retweet(ID)

def ReplyTweet(ID, tweet):
  return getClient().create_tweet(text= tweet , in_reply_to_tweet_id=ID)

def Retweeters(ID):
  return getClient().get_retweeters(id=ID)


#Functions
def Found_Reply_NewTweets(query):
  tweets_data = SearchTweet(query).data
  if tweets_data is not None and len(tweets_data) > 0:
    for tweet in tweets_data:
      print(tweet)
      rts= Retweeters(tweet.id).data
      
      if rts is None:
        continue
      
      rt_list = []
      for rt in rts:
        rt_list.append(rt.username)

      if Myusername not in rt_list:
        Retweet(tweet.id)
        ReplyTweet(tweet.id, tweet_text)
        ReplyTweet(tweet.id, tweet_text2)
        ReplyTweet(tweet.id, tweet_text2)
    return 

Found_Reply_NewTweets(query)

print("\U0001F947")
