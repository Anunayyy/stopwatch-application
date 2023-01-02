import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class Stopwatch(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = 0
        self.running = False
        self.label = Label(text='00:00', font_size=40)
        self.add_widget(self.label)
        self.start_button = Button(text='Start', font_size=20)
        self.start_button.bind(on_press=self.start)
        self.add_widget(self.start_button)
        self.stop_button = Button(text='Stop', font_size=20)
        self.stop_button.bind(on_press=self.stop)
        self.add_widget(self.stop_button)
        self.reset_button = Button(text='Reset', font_size=20)
        self.reset_button.bind(on_press=self.reset)
        self.add_widget(self.reset_button)
    
    def start(self, instance):
        if not self.running:
            self.running = True
            Clock.schedule_interval(self.update, 0.01)
    
    def stop(self, instance):
        if self.running:
            self.running = False
            Clock.unschedule(self.update)
    
    def reset(self, instance):
        self.time = 0
        self.label.text = '00:00'
    
    def update(self, dt):
        self.time += dt
        minutes, seconds = divmod(self.time, 60)
        self.label.text = '{:02d}:{:02d}'.format(int(minutes), int(seconds))

class StopwatchApp(App):
    def build(self):
        return Stopwatch()

if __name__ == '__main__':
    StopwatchApp().run()
