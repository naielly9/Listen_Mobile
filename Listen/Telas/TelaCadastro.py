import flet as ft
from .TelaPrincipal import PrincipalScreen
from database import Database

class BaseScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class CadastroScreen(BaseScreen):
    def __init__(self, page: ft.Page):
        super().__init__(page)
        self.db = Database()
        
    def on_register_click(self, e):
        username = self.username_field.value
        email = self.email_field.value
        password = self.password_field.value

        if username and email and password:
            self.db.add_user(username, email, password)
            # Transição para a tela principal
            self.page.clean() 
            Principal_Screen = PrincipalScreen(self.page)
            Principal_Screen.show()
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Preencha os dados de usúario, e-mail e a senha"), open=True)

    def show(self):
        self.page.title = "listen"
        self.username_field =   ft.TextField(
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
        self.email_field = ft.TextField(
                        label="E-mail", 
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
                    self.username_field,
                    self.email_field,
                    self.password_field,
                    ft.TextField(
                        label="Confirmar senha", 
                        width=200,
                        border_color='#9ca3af',
                        focused_color='#e5e7eb',
                        focused_bgcolor=ft.colors.TRANSPARENT, 
                        filled=False, 
                        cursor_color='#e5e7eb',
                        color='#e5e7eb',
                        password=True,
                        label_style=ft.TextStyle(color='#e5e7eb')  
                    ),
                    ft.ElevatedButton(
                        "Registrar", 
                        on_click=self.on_register_click,
                        style=ft.ButtonStyle(
                            color='#e5e7eb',
                            bgcolor='#9ca3af',
                            shape=ft.RoundedRectangleBorder(radius=5)  
                        )
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
        
        self.page.add(Cadastro_container)
