from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Rectangle, Ellipse, RoundedRectangle)
from kivy.uix.image import Image
from kivy.uix.label import Label

from kivy.config import Config
Config.set('graphics', 'resizable','0')
Config.set('graphics', 'width','411')
Config.set('graphics', 'height','730')

from kivy.uix.textinput import TextInput

class Back(Widget): 
	def __init__(self, **kwargs):
		super(Back, self).__init__(**kwargs)


		with self.canvas:
			Color(.78, .75, .69, 1) #серый
			Rectangle(pos = (0, 0), size=(411, 730))



		with self.canvas:
			Color(.92, .90, .77, 1) #жёлтый
			Rectangle(pos = (0, 0), size=(411, 131))

		with self.canvas:
			Color(.92, .90, .77, 1) #жёлтый
			Rectangle(pos = (0, 133), size=(411, 131))

		with self.canvas:
			Color(.92, .90, .77, 1) #жёлтый
			Rectangle(pos = (0, 266), size=(411, 131))

		with self.canvas:
			Color(.92, .90, .77, 1) #жёлтый
			Rectangle(pos = (0, 399), size=(411, 131))



		with self.canvas:
			Color(.94, .69, .06, 1) #ораньжевый 
			Rectangle(pos = (0, 531), size=(411, 43))

		with self.canvas:
			Color(.44, .15, .16, 1) #коричнивый
			Rectangle(pos = (0, 574), size=(411, 158))


class BoxApp(App):
	def build(self):
		painterW = Back() 
		bl = BoxLayout(orientation='vertical', size=(411, 730))
		blButton = BoxLayout(orientation='vertical', size=(411, 730))

		header = BoxLayout(orientation='horizontal', 
			size_hint=(None, None), size=(411, 158),
			spacing=257, padding=(5, 0, 5, 95))

		#header.add_widget(Image(source='img/catalog.png', size_hint=(None, None)))
		header.add_widget(Button(background_normal='img/catalog.png', 
			size_hint=(None, None), size=(72, 55)))
		bl.add_widget(Image(source='img/logo.png', 
			size_hint=(1, 1)))
		header.add_widget(Button(background_normal='img/basket.png', 
			size_hint=(None, None), size=(72, 61)))
		blButton.add_widget(header)


		blButton.add_widget(Widget(size_hint=(None, None), size=(411, 41)))
		menu = BoxLayout(size_hint=(None, None), size=(411, 41))
		menu.add_widget(Label(text=('МЕНЮ ДОСТАВКИ'), font_size='17sp',
			color=(0, 0, 0, 1)))
		bl.add_widget(menu)


#кнопки 
		
		catalog1 = BoxLayout(orientation='horizontal',
			size_hint=(None, None), size=(411, 131), 
			spacing=63, padding=(15, 0, 0, 14))
		catalog1.add_widget(Image(source='img/pizza.png', size_hint=(None, None)))
		catalog1.add_widget(Label(text='ПИЦЦА', font_size='26sp',
			color=(.44, .15, .16, 1), size_hint=(None, None)))
		button1 = Button(background_color=[0, 0, 0, 0], 
			size_hint=(None, None), size=(411, 131))
		blButton.add_widget(button1)
		bl.add_widget(catalog1)

		
		bl.add_widget(Widget(size_hint=(None, None), size=(411, 2)))
		catalog2 = BoxLayout(orientation='horizontal',
			size_hint=(None, None), size=(411, 131), 
			spacing=62, padding=(15, 0, 0, 14))
		catalog2.add_widget(Image(source='img/rolls.png', size_hint=(None, None)))
		catalog2.add_widget(Label(text='РОЛЛЫ', font_size='26sp',
			color=(.44, .15, .16, 1), size_hint=(None, None)))
		blButton.add_widget(Widget(size_hint=(None, None), size=(411, 2)))
		button2 = Button(background_color=[0, 0, 0, 0],
			size_hint=(None, None), size=(411, 131))
		blButton.add_widget(button2)
		bl.add_widget(catalog2)
		

		bl.add_widget(Widget(size_hint=(None, None), size=(411, 2)))
		catalog3 = BoxLayout(orientation='horizontal',
			size_hint=(None, None), size=(411, 131), 
			spacing=69, padding=(15, 0, 0, 14))
		catalog3.add_widget(Image(source='img/salads.png', size_hint=(None, None)))
		catalog3.add_widget(Label(text='САЛАТЫ', font_size='26sp',
			color=(.44, .15, .16, 1), size_hint=(None, None)))
		blButton.add_widget(Widget(size_hint=(None, None), size=(411, 2)))
		button3 = Button(background_color=[0, 0, 0, 0],
			size_hint=(None, None), size=(411, 131))
		blButton.add_widget(button3)
		bl.add_widget(catalog3)
		

		bl.add_widget(Widget(size_hint=(None, None), size=(411, 2)))
		catalog4 = BoxLayout(orientation='horizontal',
			size_hint=(None, None), size=(411, 131), 
			spacing=77, padding=(15, 0, 0, 14))
		catalog4.add_widget(Image(source='img/dessert.png', size_hint=(None, None)))
		catalog4.add_widget(Label(text='ДЕСЕРТЫ', font_size='26sp',
			color=(.44, .15, .16, 1), size_hint=(None, None)))
		blButton.add_widget(Widget(size_hint=(None, None), size=(411, 2)))
		button4 = Button(background_color=[0, 0, 0, 0], #Проверить есть ли она 
			size_hint=(None, None), size=(411, 131))
		blButton.add_widget(button4)
		bl.add_widget(catalog4)

		painterW.add_widget(bl)
		painterW.add_widget(blButton)
		return painterW
		


if __name__ == '__main__':
	BoxApp().run()