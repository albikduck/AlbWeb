from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
import webbrowser

Window.size = (1920, 1080)
Window.fullscreen = 'auto'

class AlbWebApp(App):
    def build(self):
        self.title = 'AlbWeb'
        
        main = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        title = Label(text='⚡ AlbWeb', font_size='70sp', size_hint_y=0.12, color=(0, 1, 0.25, 1))
        main.add_widget(title)
        
        search_box = BoxLayout(size_hint_y=0.1, spacing=15)
        
        self.search_input = TextInput(hint_text='Введите URL или поиск...', font_size='32sp', multiline=False)
        search_box.add_widget(self.search_input)
        
        go_btn = Button(text='ПЕРЕЙТИ', font_size='28sp', size_hint_x=0.25)
        go_btn.bind(on_press=self.go_to_url)
        search_box.add_widget(go_btn)
        
        main.add_widget(search_box)
        
        fav_label = Label(text='ИЗБРАННОЕ', font_size='40sp', size_hint_y=0.08, color=(0, 1, 0.25, 1))
        main.add_widget(fav_label)
        
        sites_grid = GridLayout(cols=3, spacing=20, size_hint_y=0.45)
        
        sites = [
            ('YouTube', 'https://www.youtube.com'),
            ('Google', 'https://www.google.com'),
            ('RuTube', 'https://rutube.ru'),
            ('Kinopoisk', 'https://www.kinopoisk.ru'),
            ('IVI', 'https://www.ivi.tv'),
            ('Twitch', 'https://www.twitch.tv')
        ]
        
        for name, url in sites:
            btn = Button(text=name, font_size='28sp', size_hint_y=None, height=150)
            btn.bind(on_press=lambda x, u=url: self.open_site(u))
            sites_grid.add_widget(btn)
        
        main.add_widget(sites_grid)
        
        bottom = BoxLayout(size_hint_y=0.07, spacing=20)
        version = Label(text='AlbWeb v1.0 | Сгенерировано ИИ', font_size='18sp', color=(0.5, 0.5, 0.5, 1))
        bottom.add_widget(version)
        main.add_widget(bottom)
        
        return main
    
    def go_to_url(self, instance):
        url = self.search_input.text.strip()
        if url:
            if not url.startswith('http'):
                url = 'https://www.google.com/search?q=' + url.replace(' ', '+')
            self.open_site(url)
    
    def open_site(self, url):
        webbrowser.open(url)

if __name__ == '__main__':
    AlbWebApp().run()
