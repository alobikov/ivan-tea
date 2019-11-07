from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class MyApp(App):
	def build(self):
		bl = BoxLayout()
		for i in range(9):
			bl.add_widget(Button(text = str(i)), pos_hint={"center_x": 0.5, "center_y": 0.5},)
		return bl

app = MyApp()
app.run()