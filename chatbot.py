from googlesearch import search
import requests
import string
from lxml import html
from bs4 import BeautifulSoup

def chatbot_question(query,index=0):
    fallback = 'Sorry,There are no results'
    result = ''
    try:
        search_result_list = list(search(query,tld="co.in",num=10,stop=3,pause=1))
        page = requests.get(search_result_list[index])
        tree = html.fromstring(page.content)
        soup = BeautifulSoup(page.content,features="lxml")

        article_text = ''
        article = soup.findAll('p')
        for element in article:
            article_text += '\n' + ''.join(element.findAll(text=True))
        article_text = article_text.replace('\n','')
        first_sentence = article_text.split('.')
        first_sentence = first_sentence[0].split('?')[0]

        chars_without_whitespace = first_sentence.translate(
            {ord(c):None for c in string.whitespace}
        )

        if len(chars_without_whitespace) > 0:
            result = first_sentence
        else:
            result = fallback
        return result 
    
    except:
        if len(result) == 0: result=fallback
        return result