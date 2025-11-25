import pandas as pd
from googleapiclient.discovery import build

def video_comments(video_id):
    replies = []
    limit = 500  # batas total komentar
    count = 0

    youtube = build('youtube', 'v3', developerKey=api_key)

    video_response = youtube.commentThreads().list(
        part='snippet,replies',
        videoId=video_id,
        maxResults=100
    ).execute()

    while video_response and count < limit:

        for item in video_response['items']:

            if count >= limit:
                break

            published = item['snippet']['topLevelComment']['snippet']['publishedAt']
            user = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            likeCount = item['snippet']['topLevelComment']['snippet']['likeCount']

            replies.append([published, user, comment, likeCount])
            count += 1

            # reply comment
            replycount = item['snippet']['totalReplyCount']
            if replycount > 0:
                for reply in item['replies']['comments']:

                    if count >= limit:
                        break

                    published = reply['snippet']['publishedAt']
                    user = reply['snippet']['authorDisplayName']
                    repl = reply['snippet']['textDisplay']
                    likeCount = reply['snippet']['likeCount']

                    replies.append([published, user, repl, likeCount])
                    count += 1

        # next page only if still below limit
        if 'nextPageToken' in video_response and count < limit:
            video_response = youtube.commentThreads().list(
                part='snippet,replies',
                pageToken=video_response['nextPageToken'],
                videoId=video_id,
                maxResults=100
            ).execute()
        else:
            break

    return replies

# isikan dengan api key Anda
api_key = 'API Key'

# Enter video id
# contoh url video = https://www.youtube.com/watch?v=5tucmKjOGi8
video_id = "wiIdWIgmevw" #isikan dengan kode / ID video

# Call function
comments = video_comments(video_id)

comments

df = pd.DataFrame(comments, columns=['publishedAt', 'authorDisplayName', 'textDisplay', 'likeCount'])
df

df.to_csv('youtube-comments.csv', index=False)