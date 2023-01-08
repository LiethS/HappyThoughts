import tweepy
from pyChatGPT import ChatGPT
import schedule
import time
#'pip install tweepy'
#'pip install pyChatGPT'
#'pip install schedule'

def execute():
    gpt_api = ChatGPT(session_token=AUTH, conversation_id=CONV_ID)
    #gpt_api = ChatGPT(email=EMAIL, password=PASSWORD, conversation_id=CONV_ID) #You can use login information to authenticate
    prompt = gpt_api.send_message('give me todays positive tweet, start it by saying \"Today\'s positive message is:\" and do not create any new lines. MAKE SURE YOU Keep your response under 150 characters')
    twitter_api.update_status(prompt['message'][0:280])
    gpt_api.refresh_chat_page()
    gpt_api.driver.close()

file = open("HappyThoughts\Keys.txt", "r")
credentials = file.read().splitlines()

KEY = credentials[0]
SECRET_KEY = credentials[1]
TOKEN = credentials[2]
TOKEN_SECRET = credentials[3]
EMAIL = credentials[5]
PASSWORD = credentials[6]
AUTH = credentials[7]
CONV_ID = credentials[8]

file.close()

auth = tweepy.OAuthHandler(KEY, SECRET_KEY)
auth.set_access_token(TOKEN, TOKEN_SECRET)
twitter_api = tweepy.API(auth)
schedule.every().day.at("08:00").do(execute)
while True:
    schedule.run_pending()
    time.sleep(60)