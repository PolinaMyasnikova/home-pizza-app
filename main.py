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
			Color(.44, .15, .16, 1)
			Rectangle(pos = (0, 0), size=(411, 730))

		with self.canvas:
			Color(.92, .90, .77, 1)
			Rectangle(pos = (69, 348), size=(273, 3))

		with self.canvas:
			Color(.92, .90, .77, 1)
			Rectangle(pos = (69, 238), size=(273, 3))

class BoxApp(App):
	def build(self):
		painterW = Back() 
		bl = BoxLayout(orientation='vertical', size=(411, 730))

#картинка	
		widgetImg = BoxLayout(orientation='vertical', size_hint=(1, .42)) #размер места
		widgetImg.add_widget(
			Image(source='img/logo.png'))
		bl.add_widget( widgetImg)

#поля ввода 
		widgetINF = BoxLayout(orientation='vertical', size_hint=(1, .28), 
			padding=(69, 0, 69, 25), spacing=40)
		#Первое поле ввода
		widgetINF1=BoxLayout(orientation='vertical')
		widgetINF1.add_widget(
			Label(text='Номер телефна', color=(.92, .90, .77, 1),
				size_hint=(None, None), size=(95, 28), #??? откуда считает
				font_size='13sp')) 
				
		widgetINF1.add_widget(
			TextInput(size_hint=(None, None), size=(273, 30), 
				background_color=[.44, .15, .16, 1], font_size='13sp',
				foreground_color=(.92, .90, .77, 1)))	

		#widgetINF1.add_widget(Image(source='img/logo.png')) как нибудь здесь вставить жёлтую линию
		
		widgetINF.add_widget(widgetINF1)
		#Второе поле ввода

		widgetINF2=BoxLayout(orientation='vertical')
		widgetINF2.add_widget(
			Label(text='Пароль', color=(.92, .90, .77, 1),
				size_hint=(None, None), size=(45, 28), #??? откуда считает
				font_size='13sp')) 
		widgetINF2.add_widget(
			TextInput(size_hint=(None, None), size=(273, 30),
				password='True',
				background_color=[.44, .15, .16, 1], font_size='13sp',
				foreground_color=(.92, .90, .77, 1)))
		widgetINF.add_widget(widgetINF2)
		
		bl.add_widget(widgetINF)

#кнопки
		widgetWB = BoxLayout(orientation='vertical', size_hint=(1, .3), #размер места
			padding=(111, 30, 0, 0), spacing=19)
		#Певая кнопка
		widgetWB.add_widget( 
			Button(text='Вход', background_normal ='',
				background_color=[.92, .90, .77, 1], color=(.44, .15, .16, 1),
				size_hint=(None, None), size=(190, 50),
				font_size='26sp'))
		#вторая кнопка
		widgetWB.add_widget( 
			Button(text='Регистрация', background_normal ='',
				background_color=[.92, .90, .77, 1], color=(.44, .15, .16, 1),
				size_hint=(None, None), size=(190, 50),
				font_size='26sp'))
		widgetWB.add_widget(Widget(size_hint=(None, None), size=(411, 55)))
		bl.add_widget(widgetWB)


		painterW.add_widget(bl)
		return painterW
		
"""
рахмеры 
		bl.add_widget( Button(size=(411, 310))  (1, .42)) size_hint=(1, .42)
		bl.add_widget( Button(size=(411, 200))  (1, .28)) size_hint=(1, .28)
		bl.add_widget( Button(size=(411, 220))  (1, .3))  size_hint=(1, .3)
		


		widgetWB.add_widget( 
			Button(text='Вход', background_normal ='',
				background_color=[.92, .90, .77, 1], color=(.44, .15, .16, 1),
				size_hint=(None, None), size=(190, 50),
				font_size='26sp'))
		widgetWB.add_widget( 
			Button(text='Регистрация', background_normal ='',
				background_color=[.92, .90, .77, 1], color=(.44, .15, .16, 1),
				size_hint=(None, None), size=(190, 50),
				font_size='26sp'))
		widgetWB.add_widget(Widget(size_hint=(None, None), size=(411, 55)))
		bl.add_widget(widgetWB)
		"""

if __name__ == '__main__':
	BoxApp().run()