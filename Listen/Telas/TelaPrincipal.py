import flet as ft

class BaseScreen:
    def __init__(self, page: ft.Page):
        self.page = page
        page.window_width = 400
        page.window_height = 800
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

class PrincipalScreen(BaseScreen):
    def __init__(self, page: ft.Page, username: str, email: str):
        super().__init__(page)
        self.username = username
        self.email = email

    def on_back_text_click(self, e):
        
        self.page.clean()
        from .TelaLogin import LoginScreen
        login_screen = LoginScreen(self.page)
        login_screen.show()
    
    def sobre_nos_text_click(self, e):
        
        self.page.clean()
        from .TelaSobreNos import SobreNosScreen
        SobreNos_screen = SobreNosScreen(self.page)
        SobreNos_screen.show()

    def show(self):
        self.page.title = "Listen"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.padding = 0
        self.page.update()
        
        header = ft.Row(
            [
                ft.PopupMenuButton(
                        icon=ft.icons.MENU,
                        items=[
                            ft.PopupMenuItem(
                                text="Sobre Nos", on_click=self.sobre_nos_text_click
                            ),
                            ft.PopupMenuItem(
                                text="Sair", on_click=self.on_back_text_click
                            ),
                        ]
                    ),
                ft.Text("Listen", style="titleLarge"),
                ft.PopupMenuButton(
                    icon=ft.icons.PERSON,
                    items=[
                        ft.PopupMenuItem(
                            text=f"\nUser: {self.username} \nConta: {self.email}\n",
                        ),
                    ]
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        genres_images = ft.Row(
            wrap=False,
            scroll="always",
            spacing=10,
            controls=[
                ft.Stack(
                    controls=[
                        ft.Image(
                            src="Telas/Imagens/rap.webp",
                            fit=ft.ImageFit.COVER,
                            width=300,
                            height=300,
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Container(
                            content=ft.Text("Rap", color="white", style="headlineSmall"),
                            alignment=ft.alignment.center,
                            padding=10,
                        ),
                    ]
                ),
                ft.Stack(
                    controls=[
                        ft.Image(
                            src="Telas/Imagens/rock.jpg",
                            fit=ft.ImageFit.COVER,
                            width=300,
                            height=300,
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Container(
                            content=ft.Text("Rock", color="white", style="headlineSmall"),
                            alignment=ft.alignment.center,
                            padding=10,
                        ),
                    ]
                ),
    
                ft.Stack(
                    controls=[
                        ft.Image(
                            src="Telas/Imagens/eletronica.jpg",
                            fit=ft.ImageFit.COVER,
                            width=300,
                            height=300,
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Container(
                            content=ft.Text("Eletrônica", color="white", style="headlineSmall"),
                            alignment=ft.alignment.center,
                            padding=10,
                        ), 
                    ]
                ),
                ft.Stack(
                    controls=[
                        ft.Image(
                            src="Telas/Imagens/trap.jpg",
                            fit=ft.ImageFit.COVER,
                            width=300,
                            height=300,
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Container(
                            content=ft.Text("Trap", color="white", style="headlineSmall"),
                            alignment=ft.alignment.center,
                            padding=10,
                        ), 
                    ]
                ),
                ft.Stack(
                    controls=[
                        ft.Image(
                            src="Telas/Imagens/sertanejo.jpeg",
                            fit=ft.ImageFit.COVER,
                            width=300,
                            height=300,
                            border_radius=ft.border_radius.all(10),
                        ),
                        ft.Container(
                            content=ft.Text("Sertanejo", color="white", style="headlineSmall"),
                            alignment=ft.alignment.center,
                            padding=10,
                        ), 
                    ]
                ),
            ]
        )
        genres_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Gêneros", style="titleMedium"),
                    genres_images,
                ],
                spacing=10,
            ),
            padding=15
        )

        popular_images = ft.Row(
            wrap=False,
            scroll="always",
            spacing=10,
            controls=[
                ft.Container(
                    content=ft.Image(src="Telas/Imagens/MBDT.jpg", fit=ft.ImageFit.COVER),
                    width=150,
                    height=150,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Container(
                    content=ft.Image(src="Telas/Imagens/MADDCITY.jpg", fit=ft.ImageFit.COVER),
                    width=150,
                    height=150,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Container(
                    content=ft.Image(src="Telas/Imagens/FATG.jpg", fit=ft.ImageFit.COVER),
                    width=150,
                    height=150,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Container(
                    content=ft.Image(src="Telas/Imagens/BORNTODIE.jpg", fit=ft.ImageFit.COVER),
                    width=150,
                    height=150,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Container(
                    content=ft.Image(src="Telas/Imagens/HAPPIERTHANEVER.jpg", fit=ft.ImageFit.COVER),
                    width=150,
                    height=150,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Container(
                    content=ft.Image(src="Telas/Imagens/HMHAS.jpg", fit=ft.ImageFit.COVER),
                    width=150,
                    height=150,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Container(
                    content=ft.Image(src="Telas/Imagens/NOTHINGWASAME.jpg", fit=ft.ImageFit.COVER),
                    width=150,
                    height=150,
                    border_radius=ft.border_radius.all(10),
                ),
                ft.Container(
                    content=ft.Image(src="Telas/Imagens/MISEDUCATION.jpg", fit=ft.ImageFit.COVER),
                    width=150,
                    height=150,
                    border_radius=ft.border_radius.all(10),
                ),
            ]
        )
        popular_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Popular", style="titleMedium"),
                    popular_images,
                ],
                spacing=10,
            ),
            padding=15  
        )

        bottom_nav = ft.NavigationBar(
            selected_index=0,
            on_change=lambda e: print(f"Selected: {e.control.selected_index}"),
            destinations=[
                ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
                ft.NavigationDestination(icon=ft.icons.SEARCH, label="Pesquisar"),
                ft.NavigationDestination(icon=ft.icons.STAR, label="Avaliar"),
                ft.NavigationDestination(icon=ft.icons.NOTIFICATIONS, label="Notificação"),
            ],
        )

        main_content = ft.Container(
            content=ft.Column(
                [
                    genres_section,
                    popular_section,
                ],
                spacing=20,
            ),
            padding=15
        )

        self.page.add(
            ft.Column(
                [
                    header,
                    ft.Divider(), #divide na horizontal a tela
                    main_content,
                    bottom_nav,
                ],
                expand=True,
                spacing=0,
            )
        )
