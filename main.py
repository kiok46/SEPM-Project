from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder

import action_and_status
import guest_and_author
import download_pdf

Builder.load_file('home_page.kv')
Builder.load_file('signup.kv')
Builder.load_file('action_bar.kv')
Builder.load_file('guest_and_author.kv')
Builder.load_file('download_pdf.kv')


class Home_Page(BoxLayout):
    pass

class Home(BoxLayout):
    pass
    '''
    def __init__(self,**kwargs):
        super(Sample,self).__init__(**kwargs)
        btn = Button(text = "Hi again!")
        self.add_widget(btn)
    '''
class MainApp(App):
    def build(self):
        return Home()

if __name__ in ('__main__','android'):
    app = MainApp()
    app.run()