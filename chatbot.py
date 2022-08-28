from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import streamlit

bot=ChatBot('Robo')
trainer=ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
def get_bot_response():
    return str(bot.get_response(userText))
userText=st.text_input('Please enter your message')
bot_resp=get_bot_response()
st.write(bot_resp)
