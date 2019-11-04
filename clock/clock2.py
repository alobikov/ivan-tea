from kivy.app import App
from kivy.clock import Clock
from time import strftime
from kivy.utils import get_color_from_hex
#from kivy.uix.boxlayout import BoxLayout

class Clock2App(App):

	sw_started = False
	sw_seconds = 0

	def on_start(self):
		Clock.schedule_interval(self.update, 0)

	def update(self, nap):
		self.root.ids.current_time.text = strftime('[b]%H[/b]:%M:%S')

		if self.sw_started: 
			self.sw_seconds += nap
		minutes, seconds = divmod(self.sw_seconds,60)
		ml_seconds = int(seconds * 100 % 100)
		self.root.ids.timer.text = ('%02d:%02d.[size=40]%02d[/size]'%(int(minutes), int(seconds), ml_seconds))

	def reset(self):
		if self.sw_started:
			self.root.ids.start_but.text = 'Start'
			self.sw_started = False

		self.sw_seconds = 0

	def start_stop(self):
		if self.sw_started: 
			self.sw_started = False
			self.root.ids.start_but.text = 'Start'
		else:
			self.sw_started = True
			self.root.ids.start_but.text = 'Stop'

if __name__ == '__main__':
	
	Clock2App().run()