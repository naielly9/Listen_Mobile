# import flet as ft

# class BaseScreen:
#     def __init__(self, page: ft.Page):
#         self.page = page

#     def show(self):
#         raise NotImplementedError("Subclass must implement abstract method")

# class LoginScreen(BaseScreen):
#     def __init__(self, page: ft.Page):
#         super().__init__(page)

#     def show(self):
#         self.page.title = "listen"
#         login_container = ft.Container(
#             width=self.page.window.width,
#             height=self.page.window.height,
#             gradient=ft.LinearGradient(
#                 colors=["#000000", "#000000"],
#                 begin=ft.Alignment(-1, -1),  # top-left
#                 end=ft.Alignment(1, 1)  # bottom-right
#             ),
#             content=ft.Column(
#                 [
#                     ft.Row(
#                         [
#                             ft.Container(),
#                             ft.Image(
#                                 src="Telas/Imagens/logoHeader.png",
#                                 width=200,
#                                 height=200
#                             ),
#                             ft.Container()
#                         ],
#                         alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
#                         vertical_alignment=ft.CrossAxisAlignment.CENTER
#                     ),
#                     ft.TextField(label="Usuário", width=200),
#                     ft.TextField(label="Senha", password=True, width=200)
#                 ],
#                 alignment=ft.MainAxisAlignment.CENTER,
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                 spacing=20
#             )
#         )
        
#         self.page.add(login_container)

""" import flet as ft

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
        username=ft.TextField(label="Usuário", hint_text="Digite seu usuário", width=200), 
        password=ft.TextField(label="Senha", hint_text="Digite sua senha", width=200),
        feedback=ft.Text(value="")
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
                    
                    ft.Row(
                        [
                            username,
                            password,
                            feedback  
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=20
                    ),
                ],
            )
        )
        
    def validate(e):
        if username.value and password.value:
            feedback.value="Bem-vindo de volta!"
            feedback.color="green"
        else:
            feedback.value="Credenciais incorretas!"
            feedback.color="red"
        
    self.page.add(login_container)
 """