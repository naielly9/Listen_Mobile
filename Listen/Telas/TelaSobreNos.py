import flet as ft

class BaseScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        page.window_width = 400
        page.window_height = 800

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class SobreNosScreen(BaseScreen):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.audio_player = None

    def on_back_text_click(self, e):
        
        if self.audio_player:
            self.audio_player.pause()
        
        self.page.clean()
        from .TelaLogin import LoginScreen  
        login_screen = LoginScreen(self.page)
        login_screen.show()

    def show(self):
        self.page.title = "Listen"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 0
        
        popular_images = ft.Row(
            wrap=False,
            scroll="always",
            spacing=10,
            controls=[
                ft.Container(
                    content=ft.Image(
                        src="Telas/Imagens/HOTLINEBLING.png", 
                        fit=ft.ImageFit.COVER
                    ),
                    width=350,
                    height=350,
                    border_radius=ft.border_radius.all(10),
                ),
            ],
        )

        popular_section = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Image(
                        src="Telas/Imagens/logo.png",
                        width=200,
                        height=300
                    ),
                    popular_images,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            ),
            padding=20
        )

        # Player de música
        self.audio_player = ft.Audio(
            src="audio/hotline_bling.mp3",
            autoplay=True,
        )

        self.page.add(
            ft.Column(
                controls=[
                    popular_section,
                    self.audio_player,
                    ft.ElevatedButton(
                        "Sair",
                        on_click=self.on_back_text_click,
                        style=ft.ButtonStyle(
                            color='#C73EAF',
                            bgcolor=ft.colors.WHITE,
                            shape=ft.RoundedRectangleBorder(radius=5)
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10
            )
        )
        self.page.update()