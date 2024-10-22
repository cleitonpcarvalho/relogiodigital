from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
import datetime

Window.size = (300, 200)

class Horario(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Agendar a função update_clock para ser chamada a cada segundo
        Clock.schedule_interval(self.update_clock, 1)
        
    def update_clock(self, dt):
        # Atualiza o horário atual
        horario = datetime.datetime.now()
        relogio = horario.time()
        # Atualiza o texto do label com o horário atual formatado
        self.ids.horario_atual.text = f'{relogio.hour:02d} : {relogio.minute:02d} : {relogio.second:02d}'

class Relogio(App):
    def build(self):
        return Horario()

# Corrigir a chamada do método run()
if __name__ == "__main__":
    Relogio().run()
