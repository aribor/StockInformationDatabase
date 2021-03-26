import request_stocks

url = "https://api.twitter.com/2/tweets/1275828087666679809?tweet.fields=attachments,author_id,created_at,entities,geo,id,in_reply_to_user_id,lang,possibly_sensitive,referenced_tweets,source,text,withheld"

payload = {}
headers= {}

response = request_stocks.request("GET" , url , headers=headers , data = payload)