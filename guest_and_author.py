from kivy.uix.boxlayout import BoxLayout
import json
import urllib,urllib2
from urllib import urlopen
from kivy.network.urlrequest import UrlRequest
import requests
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty,ListProperty,NumericProperty,BooleanProperty,StringProperty
from kivy.garden.swipetodelete import SwipeBehavior
import download_pdf

class Card_Container(ScrollView):
    layout_container = ObjectProperty(None)
    '''The container which contains dragable widgets.
    :attr:`layout_container` is a :class:`~kivy.properties.ObjectProperty`,
    defaults to None.
    '''
    
    def __init__(self,**kwargs):
        super(Card_Container,self).__init__(**kwargs)
        print type(self.layout_container)
        print "===================-=-=-=-=-=-==-="
        #self.layout_container.bind(minimum_height=self.layout_container.setter('height'))

class Card_Widget(SwipeBehavior,BoxLayout):
    title = StringProperty('default')
    authorname = StringProperty('default')
    abstract = StringProperty('default abstract')
    download_url = StringProperty('http://0.0.0.0:8000')
    download_extension = StringProperty('pdf')
    full_url=StringProperty()
    

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.move_to = self.x,self.y
            return super(Card_Widget, self).on_touch_down(touch)
    
    def on_touch_move(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.reduce_opacity()
            return super(Card_Widget, self).on_touch_move(touch)
    
    def on_touch_up(self, touch):
        if self.collide_point(touch.x, touch.y):
            self.check_for_left()
            self.check_for_right()
            return super(Card_Widget, self).on_touch_up(touch)

    def open_download_page(self):
        print self.download_url
        self.full_url = "http://0.0.0.0:8000/newsletter/download_help/?experiment={}.pdf".format(self.download_url)
        print self.full_url
        print "=======================" 
        self.parent.parent.parent.parent.parent.current = "download_pdf"
        self.parent.parent.parent.parent.parent.parent.ids.download_pdf.ids.title.text = self.title
        self.parent.parent.parent.parent.parent.parent.ids.download_pdf.ids.abstract.text = self.abstract
        download_pdf.Download_Pdf.download_pdf_method(self.full_url,self.download_extension)

class Guest(BoxLayout):
    pass

class Author(BoxLayout):
    pass
    
class Author_Signup(BoxLayout):
    pass

class Guest_and_Author(BoxLayout):
    cc = ObjectProperty()
    a = NumericProperty()

    def __init__(self,**kwargs):
        super(Guest_and_Author,self).__init__(**kwargs)

    def search(self):
        searched_text = self.ids.searched_text.text
        department = self.ids.department.text
        self.ids.cc.ids.layout_container.clear_widgets()

        try:
            if department == "CSE":
                request_url = 'http://0.0.0.0:8000/newsletter/cse_response/'
            elif department == "CCE":
                request_url = 'http://0.0.0.0:8000/newsletter/cce_response/'
            elif department == "ECE":
                request_url = 'http://0.0.0.0:8000/newsletter/ece_response/'
            else:
                request_url = 'http://0.0.0.0:8000/newsletter/mme_response/'
            url = urlopen(request_url).read()
            result = json.loads(url)
            #print result['area'][0]['authorname']
            #print searched_text
            for i in range(len(result['area'])):
                authorname = result['area'][i]['authorname']
                abstract = result['area'][i]['abstract']
                title = result['area'][i]['title']
                pdf_address = result['area'][i]['address']
                if searched_text in title:
                    self.ids.cc.ids.layout_container.add_widget(Card_Widget(title = title[0:30],authorname = authorname[0:10], abstract = abstract, download_url = pdf_address))
            self.out_file = open("search_result.json","w")
            json.dump(result,self.out_file, indent=4)
            self.out_file.close()
            print "done"
        except:
            print "error occured: follow the traceback"
            import traceback
            traceback.print_exc()