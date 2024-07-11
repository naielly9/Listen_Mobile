import flet as ft

class BaseScreen:
    def __init__(self, page: ft.Page):
        self.page = page

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class CadastroScreen(BaseScreen):
    def __init__(self, page: ft.Page):
        super().__init__(page)

    def show(self):
        self.page.title = "listen"
        Cadastro_container = ft.Container(
            width=self.page.window.width,
            height=self.page.window.height,
            gradient=ft.LinearGradient(
                colors=["#09090b", "#18181b"],
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
                    ft.TextField(label="Usuário", width=200,border_color = '#9ca3af',focused_color ='#e5e7eb',focused_bgcolor = ft.colors.TRANSPARENT, filled=False, 
                                 cursor_color='#e5e7eb',color='#e5e7eb'),
                    ft.TextField(label="E-mail", width=200),
                    ft.TextField(label="Senha", password=True, width=200,bgcolor=ft.colors.WHITE),
                    ft.TextField(label="Confirmar senha", password=True, width=200,bgcolor=ft.colors.WHITE)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        
        self.page.add(Cadastro_container)
