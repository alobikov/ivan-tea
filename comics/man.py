# file name: main.py

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
#from kivy.uix.relativelayout import RelativeLayout

Builder.load_file('toolbox.kv')
Builder.load_file('drawingspace.kv')
Builder.load_file('generalops.kv')
Builder.load_file('statusbar.kv')

class ComicCreator(AnchorLayout):
	pass

class ComicCreatorApp(App):
	def build(self):
		return ComicCreator()

if __name__ == '__main__':
	ComicCreatorApp().run()
