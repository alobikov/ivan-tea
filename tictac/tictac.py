from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class tictacApp(App):
    def build(self):
        self.title = 'TicTac'
        bl = BoxLayout(orientation = 'vertical')
        bl.add_widget(Button(text = 'Stat the Game', pos = (20, 1), size_hint = [1, .2]))
        gl = GridLayout(rows = 3, padding = 0, spacing = 1, size_hint = [1, .8])
        for i in range(9):
            gl.add_widget(Button(on_press = move, text = ''))
        bl.add_widget(gl)
        return bl


def move(self):
    self.text='X'


if __name__ == '__main__':
    tictacApp().run()
