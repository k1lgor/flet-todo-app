import flet as ft
from modules.todo import TodoApp


def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = "center"

    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        c.label = (
            "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        page.update()

    page.theme_mode = ft.ThemeMode.LIGHT
    c = ft.Switch(label="Light theme", on_change=theme_changed)
    page.update()

    app = TodoApp()

    page.add(c, app)


ft.app(target=main, view=ft.WEB_BROWSER, port=5000)
