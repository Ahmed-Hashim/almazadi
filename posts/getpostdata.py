import requests
x=requests.get("https://graph.facebook.com/v14.0/110331861785733_114717991347120?fields=shares.summary(true)%2Clikes.limit(0).summary(true)%2Ccomments.limit(0).summary(true)&access_token=EAAuuB0sUZCZAABAGJeckK7GZAzv194trQLr5I5Bkel8uEYSxIpFzKDessllFsLwQvzgnc51g7NVZAK3ZCD6La3eKWch66LmX0j1xStZBPxYZA7T5mOizR28h7XxfBZA0ojrbpGpCbpBdK8Skab0pSUSQ8zy53XGABxppK6XjcjFwZBoKBh30iYrEkd7A9UlVZCglII7EG27ZCRIrAZDZD")
y=x.json()

shares=y['shares']['count']
likes= y['likes']['summary']['total_count']
comments=y['comments']['summary']['total_count']
print(shares)
print(likes)
print(comments)
110331861785733/feed?pretty=0&fields=shares.summary(true)%2Clikes.limit(0).summary(true)%2Ccomments.limit(0).summary(true)&limit=100&after=QVFIUlREeTR4M2ZAWUUdHQklvRkU4TXRzdnlHY09tMlEyQXNsUTBlS0FDcE53MC1DWDJaTHBfWFlqMUctSjlqdlV0RFRnQlVEc0JCb1Vsd3VrVFBZATnl2Ykw1VzZAKR3otS2h0SG50NmpoYTZAUSklDSXFJTnpoTXFNam5nMW1rWXZArMG8ydmxBSnZABTkU3LXo3dUgwS3UtS0J2UEpicjNQVFU5c2FxV0ZAsbXhoXzBONFd4QkJyRXZAIdWFJemJFRWxUb3FmSAZDZD