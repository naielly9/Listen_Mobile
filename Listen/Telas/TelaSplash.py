import flet as ft
import time
#from .TelaLogin import LoginScreen

class BaseScreen:
    def __init__(self, page: ft.Page):
        self.page = page

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class SplashScreen(BaseScreen):
    def __init__(self, page: ft.Page):
        super().__init__(page)

    def show(self):
        self.page.title = "listen"
        gradient_container = ft.Container(
            width=self.page.window.width,
            height=self.page.window.height,
            gradient=ft.LinearGradient(
                colors=["#ec4899", "#db2777", "#be185d"],
                begin=ft.Alignment(-1, -1),  # top-left
                end=ft.Alignment(1, 1)  # bottom-right
            ),
            content=ft.Column(
                [
                    ft.Image(
                        src="Telas/Imagens/logoPreto.png",
                        width=200,
                        height=200
                    ),
                    ft.Text("Listen", style=ft.TextThemeStyle.DISPLAY_LARGE, color=ft.colors.WHITE),
                    ft.Text("Carregando...", style=ft.TextThemeStyle.DISPLAY_LARGE, color=ft.colors.WHITE),
                    ft.ProgressBar(width=200, color=ft.colors.WHITE)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        
        self.page.add(gradient_container)
        
        progress_bar = gradient_container.content.controls[3]
        for i in range(100):
            progress_bar.value = i / 100
            self.page.update()
            time.sleep(0.05)
        
        # Transição para a tela de login
       # self.page.clean()
       # login_screen = LoginScreen(self.page)
       # login_screen.show()
