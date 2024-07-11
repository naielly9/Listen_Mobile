import flet as ft
from Telas.TelaSplash import SplashScreen
from Telas.TelaCadastro import CadastroScreen


def main(page: ft.Page):
    # splash_screen = SplashScreen(page)
    # splash_screen.show()

    splash_screen = CadastroScreen(page)
    splash_screen.show()
ft.app(target=main)
