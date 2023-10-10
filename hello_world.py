import flet as ft

def main(page: ft.Page):
    # add/update controls on Page
    page.add(ft.Text("Hola, Flet!"))

ft.app(main, view=ft.WEB_BROWSER)