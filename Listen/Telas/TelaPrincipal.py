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
        self.page.title = "Cadastro"

        def on_register_click(e):
            # Logic to register the user can be added here
            self.page.go('/principal')

        def on_login_click(e):
            self.page.go('/principal')

        Cadastro_container = ft.Container(
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
                    ft.TextField(label="E-mail", width=200),
                    ft.TextField(label="Senha", password=True, width=200),
                    ft.TextField(label="Confirmar senha", password=True, width=200, bgcolor=ft.Colors.WHITE),
                    ft.ElevatedButton(text="Registrar", on_click=on_register_click),
                    ft.TextButton(text="Iniciar sessão", on_click=on_login_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

        self.page.add(Cadastro_container)

# Example usage
def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 600
    cadastro_screen = CadastroScreen(page)
    cadastro_screen.show()

ft.app(target=main)
