import flet as ft
from database import Database
from .TelaPrincipal import PrincipalScreen

class BaseScreen:
    def __init__(self, page: ft.Page):
        self.page = page

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class LoginScreen(BaseScreen):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.db = Database()

    def on_login_click(self, e):
        username = self.username_field.value
        password = self.password_field.value

        if self.db.validate_user(username, password):
            # Login bem-sucedido, redirecionar para a tela principal
            self.page.clean()
            principal_screen = PrincipalScreen(self.page)
            principal_screen.show()
        else:
            # Exibir mensagem de erro
            self.page.snack_bar = ft.SnackBar(ft.Text("Usuário ou senha inválidos"), open=True)
            self.page.update()

    def show(self):
        self.page.title = "listen"

        self.username_field = ft.TextField(label="Usuário", width=200)
        self.password_field = ft.TextField(label="Senha", password=True, width=200)

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
                    self.username_field,
                    self.password_field,
                    ft.ElevatedButton("Login", on_click=self.on_login_click),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

        self.page.add(login_container)
        # Adiciona um Snackbar ao Page
        self.page.snack_bar = ft.SnackBar(content=ft.Text(""))
