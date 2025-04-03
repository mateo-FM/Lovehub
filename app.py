import os
import webbrowser
import random
from kivy.resources import resource_add_path
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.textinput import TextInput



# Añadir la carpeta assets
resource_add_path(os.path.join(os.path.dirname(__file__), 'assets'))


# Registrar la carpeta 'assets' para que Kivy pueda acceder a la fuente
asset_folder = os.path.join(os.path.dirname(__file__), 'assets')
resource_add_path(asset_folder)

# Usar la ruta absoluta para la fuente
font_path = os.path.join(asset_folder, 'CuteFont.ttf')


# Configurar la ventana
Window.size = (400, 600)
Window.clearcolor = (1, 0.8, 1, 1)  # Fondo rosa claro

# Pantalla principal
class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        title = Label(text="LoveHub",font_name=font_path, font_size='30sp', bold=True, halign="center", color=(0.2, 0.2, 0.2, 1))
        layout.add_widget(title)

        # Botón para la calculadora de compatibilidad
        btn_calculator = Button(text="Calculadora de Compatibilidad",font_name=font_path, size_hint=(1, None), height=50,
                                background_color=(1, 0.4, 0.4, 1))
        btn_calculator.bind(on_press=self.go_to_calculator)
        layout.add_widget(btn_calculator)

        # Botón para las citas románticas
        btn_love_quotes = Button(text="Recomendacion de canciones",font_name=font_path, size_hint=(1, None), height=50,
                                 background_color=(0.7, 0.4, 0.8, 1))
        btn_love_quotes.bind(on_press=self.go_to_love_quotes)
        layout.add_widget(btn_love_quotes)

        # Botón para las citas bíblicas
        btn_bible_quotes = Button(text="Citas Biblicas",font_name=font_path, size_hint=(1, None), height=50,
                                  background_color=(0.4, 0.7, 0.4, 1))
        btn_bible_quotes.bind(on_press=self.go_to_bible_quotes)
        layout.add_widget(btn_bible_quotes)

        self.add_widget(layout)

    def go_to_calculator(self, instance):
        self.manager.current = "calculator"

    def go_to_love_quotes(self, instance):
        self.manager.current = "love_quotes"

    def go_to_bible_quotes(self, instance):
        self.manager.current = "bible_quotes"

# Pantalla para la calculadora de compatibilidad
class CalculatorScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Título
        label = Label(text="Calculadora de Compatibilidad", font_name=font_path, font_size='30sp', color=(0.2, 0.2, 0.2, 1))
        layout.add_widget(label)

        # Campos para ingresar nombres
        self.name_input = TextInput(hint_text="Ingresa tu nombre", size_hint=(1, None), height=40, font_name=font_path)
        self.crush_input = TextInput(hint_text="Ingresa el nombre de tu crush", size_hint=(1, None), height=40, font_name=font_path)
        layout.add_widget(self.name_input)
        layout.add_widget(self.crush_input)

        # Botón para calcular compatibilidad
        btn_calculate = Button(text="Calcular",font_name=font_path, size_hint=(1, None), height=50, background_color=(0.9, 0.6, 0.6, 1))
        btn_calculate.bind(on_press=self.calculate_compatibility)  # Vínculo al método
        layout.add_widget(btn_calculate)

        # Etiqueta para mostrar el resultado
        self.result_label = Label(text="La compatibilidad aparecerá aquí", font_size='20sp', color=(0.2, 0.2, 0.2, 1))
        layout.add_widget(self.result_label)

        # Botón para volver al menú principal
        btn_back = Button(text="Volver al Menú", size_hint=(1, None), height=50, background_color=(0.7, 0.7, 0.9, 1))
        btn_back.bind(on_press=self.go_to_home)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    # Definir el método calculate_compatibility
    def calculate_compatibility(self, instance):
        name = self.name_input.text
        crush_name = self.crush_input.text

        if name and crush_name:
            # Fórmula de compatibilidad basada en los valores ASCII de los nombres
            compatibility = self.calculate_scientific_compatibility(name, crush_name)
            self.result_label.text = f"La compatibilidad entre {name} y {crush_name} es: {compatibility}%"
        else:
            self.result_label.text = "Por favor, ingresa ambos nombres."

    def calculate_scientific_compatibility(self, name, crush_name):
        # Convertir los nombres a minúsculas y calcular la suma de los valores ASCII
        name = name.lower()
        crush_name = crush_name.lower()

        # Sumar el valor ASCII de cada letra en los nombres
        sum_name = sum(ord(c) for c in name)
        sum_crush_name = sum(ord(c) for c in crush_name)

        # Calcular la compatibilidad como el promedio de la suma de los valores ASCII, normalizado a 100
        compatibility = (sum_name + sum_crush_name) % 101
        return compatibility

    def go_to_home(self, instance):
        self.manager.current = "home"

#diccionario de canciones y categoría
SONG_CATEGORIES = {
    "Tristes": [
        "Habits – Tove Lo",
        "Circles – Post Malone",
        "Someone Like You – Adele",
        "The Loneliest – Måneskin"
    ],
    "Romanticas": [
        "Kiss Me More – Doja Cat ft. SZA",
        "Levitating – Dua Lipa",
        "Love Nwantiti – CKay ft. Dj Yo! & AX'EL",
        "Leave The Door Open – Silk Sonic (Bruno Mars & Anderson .Paak)"
    ],
    "Intensas": [
        "Your Best American Girl – Mitski",
        "Best Part – Daniel Caesar ft. H.E.R.",
        "From the Start – Laufey",
        "Electric – Alina Baraz ft. Khalid"
        "Dance With Me! – beabadoobee"
    ],
    "Felices": [
        "Flowers – Miley Cyrus",
        "I'm Good (Blue) – David Guetta & Bebe Rexha",
        "Mi Gente – J Balvin ft. Beyoncé",
        "Uptown Funk – Mark Ronson ft. Bruno Mars"
    ]
}

class SongRecommendationScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Título
        self.title_label = Label(text="Recomendaciones de Canciones",font_name=font_path, font_size="24sp", bold=True, color=(0.2, 0.2, 0.2, 1))
        self.layout.add_widget(self.title_label)
        
        # Botones de categorías
        for category in SONG_CATEGORIES.keys():
            btn = Button(text=category, font_name=font_path, size_hint=(1, None), height=50, background_color=(0.1, 0.1, 0.1, 1)) # Negro
            btn.bind(on_press=self.recommend_song)
            self.layout.add_widget(btn)
        
        # Etiqueta para mostrar la canción recomendada
        self.song_label = Label(text="Elige una categoria para ver una canción: ", font_size="18sp", color=(0.2, 0.2, 0.2, 1))
        self.layout.add_widget(self.song_label)
        
        # Botón para buscar la canción en YouTube
        self.search_button = Button(text="Buscar en YouTube: ",font_name=font_path, size_hint=(1, None), height=50, disabled=True, background_color=(0, 0.5, 1, 1)) # Azul
        self.search_button.bind(on_press=self.search_song)
        self.layout.add_widget(self.search_button)
        
        # Botón para volver al menú principal
        self.back_button = Button(text="Volver al Menu",font_name=font_path, size_hint=(1, None), height=50, background_color=(0.8, 0, 0, 1)) # Rojo oscuro
        self.back_button.bind(on_press=self.go_back)
        self.layout.add_widget(self.back_button)
        
        self.add_widget(self.layout)
        self.current_song = ""
    
    def recommend_song(self, instance):
        category = instance.text
        self.current_song = random.choice(SONG_CATEGORIES[category])
        self.song_label.text = f"Recomendación: {self.current_song}"
        self.search_button.disabled = False
    
    def search_song(self, instance):
        if self.current_song:
            query = self.current_song.replace(" ", "+")
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
    
    def go_back(self, instance):
        self.manager.current = "home"



# Pantalla para las citas bíblicas
class BibleQuotesScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        # Título
        label = Label(text="Citas Biblicas", font_name=font_path, font_size='30sp', color=(0.2, 0.2, 0.2, 1))
        layout.add_widget(label)

        # Aquí puedes agregar una cita bíblica inicial
        self.quote_label = Label(text="El amor es paciente el amor es bondadoso", font_name=font_path, font_size='20sp', color=(0.2, 0.2, 0.2, 1))
        layout.add_widget(self.quote_label)

        # Botón para cambiar la cita bíblica
        btn_next_quote = Button(text="Nueva Cita", size_hint=(1, None), height=50, background_color=(0.4, 0.7, 0.4, 1))
        btn_next_quote.bind(on_press=self.show_new_quote)
        layout.add_widget(btn_next_quote)

        # Botón para volver al menú principal
        btn_back = Button(text="Volver al Menú",font_name=font_path, size_hint=(1, None), height=50, background_color=(0.7, 0.7, 0.9, 1))
        btn_back.bind(on_press=self.go_to_home)
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def show_new_quote(self, instance):
        # Aquí puedes agregar lógica para mostrar citas bíblicas aleatorias o específicas
        quotes = [
            "El amor es paciente, el amor es bondadoso",
            "Amaras al Senor tu Dios con todo tu corazón",
            "El amor nunca dejara de ser",
            "Dios es amor",
            "Amarás a tu projimo como a ti mismo"
        ]
        import random
        new_quote = random.choice(quotes)
        self.quote_label.text = new_quote

    def go_to_home(self, instance):
        self.manager.current = "home"

# Clase principal de la app
class LoveHubApp(App):
    def build(self):
        sm = ScreenManager()

        # Agregar las pantallas
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(CalculatorScreen(name="calculator"))
        sm.add_widget(SongRecommendationScreen(name="love_quotes"))
        sm.add_widget(BibleQuotesScreen(name="bible_quotes"))

        return sm

if __name__ == "__main__":
    LoveHubApp().run()
