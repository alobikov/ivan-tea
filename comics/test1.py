from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout

class TestKv(AnchorLayout):
	pass


class TestKvApp(App):
	def build(self):
		return TestKv()

app = TestKvApp()
app.run()