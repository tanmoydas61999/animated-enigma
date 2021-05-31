# # API_ID = 5219478
# # API_HASH = 'bcb083163fd8aa70795f8622c9bebc5a'
# from pyrogram import Client

# api_id = 5219478
# api_hash = "bcb083163fd8aa70795f8622c9bebc5a"
# bot_token = '1114840719:AAE53BQlnmss5p49Z7xsAz5fkGesVVF35ME'



# def progress(current, total):
#   print(f"{current * 100 / total:.1f}%")

# with Client("my_account", api_id, api_hash,bot_token=bot_token) as app:
#     for message in app.iter_history('me'):
#       if message.text == '0':
#         break
#       path = app.download_media(message, progress=progress)




from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

body = {
  'name': '1.txt',
  'parents': ''
}

media_body = MediaFileUpload('./a.txt',mimetype='application/vnd.google-apps.document')


service.files().create(
  body=body,
  media_body=media_body,
  fields='id'
).execute()



