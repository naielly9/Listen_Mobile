import flet as ft

class BaseScreen:
    def __init__(self, page: ft.Page):
        self.page = page

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class LoginScreen(BaseScreen):
    def __init__(self, page: ft.Page):
        super().__init__(page)

    def show(self):
        self.page.title = "listen"
        login_container = ft.Container(
            width=self.page.window.width,
            height=self.page.window.height,
            gradient=ft.LinearGradient(
                colors=["#000000", "#000000"],
                begin=ft.Alignment(-1, -1),  # top-left
                end=ft.Alignment(1, 1)  # bottom-right
            ),
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(),
                            ft.Image(
                                src="Telas/Imagens/logoHeader.png",
                                width=200,
                                height=200
                            ),
                            ft.Container()
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER
                    ),
                    ft.TextField(label="Usuário", width=200),
                    ft.TextField(label="Senha", password=True, width=200)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        
        self.page.add(login_container)
