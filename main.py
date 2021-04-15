import kivy
from kivy.metrics import cm
from kivy.uix.gridlayout import GridLayout

from articleScraper import *
from dbh import *

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
import requests

Config.set('graphics', 'resizable', True)


class FactCheckWindow(Screen):
    articleURL = ObjectProperty(None)
    classification = ObjectProperty(None)

    def clearText(self):
        self.txt.text = ''

    def factCheckButtonClick(self):
        if not self.returns404Error():
            if not self.isSatireArticle():
                if not self.isNotAnArticle():
                    try:
                        scrapeArticleInfo(self.articleURL.text)
                        connection = create_server_connection("localhost", "root", pw, "Articles")
                        cursor = connection.cursor(prepared=True)
                        sql_insert_query = "INSERT INTO Article (Title, Text) VALUES (%s, %s)"
                        insert_tuple = (getArticleTitle(self.articleURL.text), getArticleText(self.articleURL.text))

                        cursor.execute(sql_insert_query, insert_tuple)
                        connection.commit()
                        print("Article added to database!")
                        # This is just filler code for now, will need to change this to whatever the algorithm gives us
                        self.classification.text = "Real"
                    except mysql.connector.Error as err:
                        print("Parameterized query failed {}".format(err))

    def isSatireArticle(self):
        satireSources = ["alhudood", "babylonbee", "bbspot", "thebeaverton", "betootaadvocate", "borowitz-report",
                         "burrardstreetjournal",
                         "chaser.com.au", "elchiguirebipolar", "thecivilian", "clickhole", "cracked.com", "dailybonnet",
                         "thedailymash", "dailysquib", "thedailywtf", "speld.nl", "der-postillon", "duffelblog",
                         "elmundotoday",
                         "fakingnews", "framleyexaminer", "freewoodpost.net", "thehardtimes", "huzlers.com",
                         "journaldemourreal",
                         "khabaristantimes", "landoverbaptist", "legorafi.fr", "nationalreport.net", "newsbiscuit",
                         "newsthump",
                         "njuz.net", "nordpresse.be", "theonion", "theoxymoron", "thepoke.co.uk", "private-eye.co.uk",
                         "reductress.com", "rochdaleherald.co.uk", "scrappleface.com", "sensacionalista",
                         "southendnewsnetwork.net",
                         "topekasnews.com", "truenorthtimes.ca", "waterfordwhispersnews.com", "weeklyworldnews.com",
                         "worldnewsdailyreport.com"]
        x = 0
        articleIsSatire = False
        while x < len(satireSources):
            if satireSources[x] in self.articleURL.text:
                satireArticle()
                articleIsSatire = True
                break
            else:
                x += 1

        return articleIsSatire

    def returns404Error(self):
        notFound = False
        r = requests.head(self.articleURL.text)
        if r.status_code == 404:
            error404()
            notFound = True

        return notFound

    def isNotAnArticle(self):
        notArticle = False
        if not getArticleAuthors(self.articleURL.text):
            notAnArticle()
            notArticle = True

        return notArticle


    def backButtonClick(self):
        sm.current = "main"


class MainWindow(Screen):

    def checkButtonClick(self):
        sm.current = "factcheck"

    def recentButtonClick(self):
        sm.current = "recentlychecked"

    def aboutButtonClick(self):
        sm.current = "about"


class RecentlyCheckedWindow(Screen):
    layout = ObjectProperty(None)

    def displayArticles(self):
        try:
            connection = create_server_connection("localhost", "root", pw, "Articles")
            cursor = connection.cursor(buffered=True)
            sql_query = "SELECT Title, Label FROM Article ORDER BY ID DESC LIMIT 8"
            cursor.execute(sql_query)
            connection.commit()
            rows = cursor.fetchall()
            for row in rows:
                self.layout.add_widget(Label(text=str(row[0]), halign='center', text_size=(350, None)))
                self.layout.add_widget(Label(text=str(row[1]), halign='center', text_size=(350, None)))
        except mysql.connector.Error as err:
            print("Error {}".format(err))

    def backButtonClick(self):
        sm.current = "main"


class AboutWindow(Screen):
    def backButtonClick(self):
        sm.current = "main"


class WindowManager(ScreenManager):
    pass


def satireArticle():
    pop = Popup(title='Satire Detected',
                content=Label(
                    text='This article comes from a known satire source\n and thus should be treated as fake.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def error404():
    pop = Popup(title='Article Not Found',
                content=Label(
                    text='Unfortunately we couldn\'t find that article.\n Please check your link and try again.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


def notAnArticle():
    pop = Popup(title='Not an Article',
                content=Label(text='The link you provided is not an article\n and thus cannot be checked.'),
                size_hint=(None, None), size=(400, 400))
    pop.open()


kv = Builder.load_file("my.kv")
sm = WindowManager()

screens = [FactCheckWindow(name="factcheck"), RecentlyCheckedWindow(name="recentlychecked"), AboutWindow(name="about"),
           MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"


class FakeNewsDetector(App):
    def build(self):
        return sm


mainGUI = FakeNewsDetector()
mainGUI.run()
