# MADE BY HASH-002

import sys
import time
import random
import requests
import json
import imdb
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


# Function to search the contact which is not present in the recent List
def new_chat(user_name):

    # Click on the List
    search_chat = chrome_browser.find_element_by_xpath('//div[@class="_3LX7r"]')
    search_chat.click()

    # Search the Contact
    new_user = chrome_browser.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"]')
    new_user.send_keys(user_name)

    time.sleep(1)  # pause to get the content loaded

    try:
        user = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        chrome_browser.close()
        print(e)
        sys.exit()


if __name__ == '__main__':

    # load web driver for selenium : chrome
    chrome_browser = webdriver.Chrome(executable_path='C:\\Users\\hp\\Downloads\\chromedriver_win32\\chromedriver')
    chrome_browser.get('https://web.whatsapp.com/')

    time.sleep(15)  # wait to scan QR code

    # List of the users you want to respond
    user_name_list = ['']

    for user_name in user_name_list:
        try:
            user_name = chrome_browser.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
            user_name.click()
        except NoSuchElementException:
            new_chat(user_name)

        # most recent message in the chat
        msg_list = chrome_browser.find_elements_by_css_selector("span._3-8er.selectable-text.copyable-text")
        msg = [message.text for message in msg_list]

        if msg[-1].upper() == "HI BOT":

            reply = chrome_browser.find_element_by_xpath('//div[@class="_2A8P4"]')
            reply.send_keys("Hello! How may I help you today?\n"
                            "Press 1 for a learning a fun fact about any number.\n"
                            "Press 2 to get to know about Top news in the country.\n"
                            "Press 3 to get the list of Top Movies.\n"
                            "Press q to quit")
            press = chrome_browser.find_element_by_xpath('//button[@class="_1E0Oz"]')
            press.click()

            run = True
            while run == True:

                time.sleep(5)
                msg_list = chrome_browser.find_elements_by_css_selector("span._3-8er.selectable-text.copyable-text")
                msg = [message.text for message in msg_list]
                entry = msg[-1]

                if (entry == "Hello! How may I help you today?\n"
                             "Press 1 for a learning a fun fact about any number.\n"
                             "Press 2 to get to know about Top news in the country.\n"
                             "Press 3 to get the list of Top Movies.\n"
                             "Press q to quit"):
                    time.sleep(5)
                    continue

                elif entry == "1":

                    # Number Api Loading a fun fact for the number
                    s = "http://numbersapi.com/"
                    reply.send_keys("Enter any number")
                    press = chrome_browser.find_element_by_xpath('//button[@class="_1E0Oz"]')
                    press.click()
                    time.sleep(10)

                    msg_list = chrome_browser.find_elements_by_css_selector("span._3-8er.selectable-text.copyable-text")
                    msg = [message.text for message in msg_list]
                    n = str(random.randint(0, 100000))

                    if msg[-1] == "Enter any number":
                        reply.send_keys("No Number let me tell you something myself")
                        time.sleep(1)
                        press = chrome_browser.find_element_by_xpath('//button[@class="_1E0Oz"]')
                        press.click()
                        time.sleep(1)
                    else:
                        n = msg[-1]

                    s = s + n
                    req = requests.get(s)
                    reply.send_keys(req.text)
                    time.sleep(1)
                    press = chrome_browser.find_element_by_xpath('//button[@class="_1E0Oz"]')
                    press.click()
                    time.sleep(1)
                    continue

                elif entry == "2":

                    # News Api Loading the most recent news
                    r = requests.get("****** REMOVED API KEY FOR SECURITY REASONS ******")
                    data = json.loads(r.content)
                    full_news = ''
                    for i in range(5):
                        title = "News: " + str(i + 1) + " " + data['articles'][i]['title'] + "     "
                        url = "Tap to read more: " + data['articles'][i]['url'] + "     "
                        news = title + url + "     "
                        full_news += news

                    reply.send_keys(full_news)
                    time.sleep(5)
                    press = chrome_browser.find_element_by_xpath('//button[@class="_1E0Oz"]')
                    press.click()
                    time.sleep(5)

                elif entry == "3":

                    # Getting top movies from imdbpy python package
                    moviesDB = imdb.IMDb()
                    movies = moviesDB.get_top250_movies()
                    top_movies = ''
                    rand1 = random.randint(0, 250)
                    for m in movies[rand1:rand1 + 10]:
                        top_movies = top_movies + str(m)

                    reply.send_keys(top_movies)
                    time.sleep(5)
                    press = chrome_browser.find_element_by_xpath('//button[@class="_1E0Oz"]')
                    press.click()
                    time.sleep(5)
                    continue

                elif entry == "q":

                    reply.send_keys("Have a good day. Bye!")
                    time.sleep(3)
                    press = chrome_browser.find_element_by_xpath('//button[@class="_1E0Oz"]')
                    press.click()
                    time.sleep(3)
                    run = False
                    continue

                else:
                    continue

    chrome_browser.close()