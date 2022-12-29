import flet as ft
from modules.todo import TodoApp


def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = "center"
    page.update()

    app = TodoApp()

    page.add(app)


ft.app(target=main, view=ft.WEB_BROWSER, port=5000)
