import flet as ft
from database import Database
from .TelaPrincipal import PrincipalScreen
from .TelaCadastro import CadastroScreen

class BaseScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        page.window_width = 400
        page.window_height = 800
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class LoginScreen(BaseScreen):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.db = Database()

    def on_login_click(self, e):
        username = self.username_field.value
        password = self.password_field.value
        
        user = self.db.validate_user(username, password)
        if user:
            username, email = user[1], user[2]
            self.page.clean()
            #prox. pagina
            principal_screen = PrincipalScreen(self.page, username, email)
            principal_screen.show()
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Usuário ou senha inválidos"), open=True)
            self.page.update()

    def on_register_text_click(self, e):
        #prox. pagina
        self.page.clean()
        cadastro_screen = CadastroScreen(self.page)
        cadastro_screen.show()

    def show(self):
        self.page.title = "listen"
        self.username_field =  ft.TextField(
                        label="Usuário", 
                        width=200,
                        border_color='#9ca3af',
                        focused_color='#e5e7eb',
                        focused_bgcolor=ft.colors.TRANSPARENT, 
                        filled=False, 
                        cursor_color='#e5e7eb',
                        color='#e5e7eb',
                        label_style=ft.TextStyle(color='#e5e7eb')
        )
        self.password_field = ft.TextField(
                        label="Senha", 
                        width=200,
                        border_color='#9ca3af',
                        focused_color='#e5e7eb',
                        focused_bgcolor=ft.colors.TRANSPARENT, 
                        filled=False, 
                        cursor_color='#e5e7eb',
                        color='#e5e7eb',
                        password=True,
                        label_style=ft.TextStyle(color='#e5e7eb')
        )
        
        login_container = ft.Container(
            width=self.page.window.width,
            height=self.page.window.height,
            gradient=ft.LinearGradient(
                colors=["#150c14", "#150c14"],
                begin=ft.Alignment(-1, -1),  
                end=ft.Alignment(1, 1)  
            ),
            content=ft.Column(
                controls=[
                    ft.Image(
                        src="Telas/Imagens/logo.png",
                        width=200,
                        height=300
                    ),
                    ft.Container(height=20),  # Espaço entre a imagem e os campos
                    self.username_field,
                    self.password_field,
                    ft.ElevatedButton(
                        "Login", 
                        on_click=self.on_login_click,
                        style=ft.ButtonStyle(
                            color='#C73EAF',
                            bgcolor=ft.colors.WHITE,
                            shape=ft.RoundedRectangleBorder(radius=5)  
                        )
                    ),
                    ft.TextButton(
                        "Não tem cadastro? Cadastre-se",
                        on_click=self.on_register_text_click,
                        style=ft.ButtonStyle(
                            color='#C73EAF',
                            shape=ft.RoundedRectangleBorder(radius=5)  
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )

        self.page.add(login_container)
        
        # Adiciona um Snackbar, barra aviso.
        self.page.snack_bar = ft.SnackBar(content=ft.Text(""))

