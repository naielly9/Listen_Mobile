import flet as ft
from Telas.TelaSplash import SplashScreen

def main(page: ft.Page):
    splash_screen = SplashScreen(page)
    splash_screen.show()

ft.app(target=main)
    