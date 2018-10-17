import telepot
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import time
import sys
import urllib.request
import bs4 as bs
import emoji
from pprint import pprint

siti = []
answer = []

def fill_news():
    sauce = urllib.request.urlopen('http://www.comune.barletta.bt.it/retecivica/avvisi18.htm').read()
    soup = bs.BeautifulSoup(sauce, 'html.parser')
    #Cercare i tag
    for items in soup.find_all('div','bordo_aran piccolo'):
        for item in items.find_all('tr',limit=6):
            for td in item.find_all('td'):
                answer.append(td.get_text())
            for link in item.find_all('a'):
                siti.append("http://www.comune.barletta.bt.it/retecivica/"+link.get('href'))
def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    #Bottoni
    sitonews1 = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=emoji.emojize('Sito :memo:'),
                                  callback_data='sitonews1',
                                  url=siti[0])],])
    #Bottoni
    sitonews2 = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=emoji.emojize('Sito :memo:'),
                                  callback_data='sitonews2',
                                  url=siti[1])],])
    #Bottoni
    sitonews3 = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=emoji.emojize('Sito :memo:'),
                                  callback_data='sitonews3',
                                  url=siti[2])],])
    #Bottoni
    sitonews4 = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=emoji.emojize('Sito :memo:'),
                                  callback_data='sitonews4',
                                  url=siti[3])],])
    #Bottoni
    sitonews5 = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text=emoji.emojize('Sito :memo:'),
                                  callback_data='sitonews5',
                                  url=siti[4])],])
    
    #Risposte ai messaggi digitati
    if msg['text'] == '/stop':
         quit
    
    if msg['text'] == '/eraclio':
        furl = urllib.request.urlopen('https://barletta.gocity.it/library/media/barletta5.jpg')
        bot.sendPhoto(chat_id, ('eraclio.jpg',furl))
        bot.sendMessage(chat_id, "Eraclio")
        return
        
    if msg['text'] == '/castello':
        furl = urllib.request.urlopen('https://www.viaggiareinpuglia.it/img/Castello/barletta__castello_biffani_1499337642952.jpg')
        bot.sendPhoto(chat_id, ('castello.jpg',furl))
        bot.sendMessage(chat_id, "Castello Svevo di Barletta")
        return
    
    if msg['text'] == '/news':
        bot.sendMessage(chat_id, answer[1]+"\n"+answer[2],reply_markup=sitonews1)
        bot.sendMessage(chat_id, answer[3]+"\n"+answer[4],reply_markup=sitonews2)
        bot.sendMessage(chat_id, answer[5]+"\n"+answer[6],reply_markup=sitonews3)
        bot.sendMessage(chat_id, answer[7]+"\n"+answer[8],reply_markup=sitonews4)
        bot.sendMessage(chat_id, answer[9]+"\n"+answer[10],reply_markup=sitonews5)
            
        bot.sendMessage(chat_id, "Ultime 5 news dal Comune di Barletta")
        return
    
    bot.sendMessage(chat_id, "Credo di non aver capito")
    
def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print(query_id, from_id, query_data)
    
#    if query_data == 'sitonews1':
#        urllib.urlopen('http://example.com')
    
fill_news()
bot = telepot.Bot("679953746:AAECClhSHfKwnBDfnwO4yO5KWvkccOelWEo")
#bot.message_loop({'chat': on_chat_message,
#                  'callback_query': on_callback_query})
MessageLoop(bot, {'chat': on_chat_message,
				  'callback_query': on_callback_query}).run_as_thread() 
print('Listening ...')

#bot.getUpdates()

while 1:
    time.sleep(3)
