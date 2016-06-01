from kivy.uix.boxlayout import BoxLayout
import json
import urllib,urllib2
from urllib import urlopen
from kivy.network.urlrequest import UrlRequest
import requests
from kivy.properties import ObjectProperty,ListProperty,NumericProperty,BooleanProperty

class Download_Pdf(BoxLayout):
	title = ObjectProperty()
	abstract = ObjectProperty()
	pdf_button = ObjectProperty()

	@classmethod
	def download_pdf_method(self,download_url = "http://0.0.0.0:8000/newsletter/download_help/?experiment=/home/kuldeep/Desktop/trydjango18/src/newsletter/Database/CCE/cce1.pdf",extension = 'pdf'):
		try:
			#url = urlopen("http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=2de143494c0b295cca9337e1e96b00e0").read()
			#url = urlopen("http://127.0.0.1:8000").read()
			#download_url = 'http://127.0.0.1:8000'
			#urllib.urlretrieve('http://127.0.0.1:8000', 'file.pdf')
			print download_url
			print "------------------------------------------holihol"
			response = urllib2.urlopen(download_url)
			file_ = open("download.{}".format(extension), 'wb')
			file_.write(response.read())
			file_.close()
			print "done"
		except:
			print "error occured: follow the traceback"
			import traceback
			traceback.print_exc()