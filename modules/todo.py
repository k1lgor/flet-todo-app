import flet as ft
from modules.task import Task


class TodoApp(ft.UserControl):
    def build(self):
        self.new_task = ft.TextField(hint_text="Whats needs to be done?", expand=True)
        self.tasks = ft.Column()

        self.filter = ft.Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[
                ft.Tab(text="All", icon=ft.icons.BOOK),
                ft.Tab(text="Active", icon=ft.icons.NOTIFICATIONS_ACTIVE),
                ft.Tab(text="Completed", icon=ft.icons.DONE),
            ],
        )

        return ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.new_task,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.add_clicked
                        ),
                    ],
                ),
                ft.Column(
                    spacing=25,
                    controls=[
                        self.filter,
                        self.tasks,
                    ],
                ),
            ],
        )

    def add_clicked(self, e):
        task = Task(self.new_task.value, self.task_status_change, self.task_delete)
        self.tasks.controls.append(task)
        self.new_task.value = ""
        self.update()

    def task_status_change(self, task):
        self.update()

    def task_delete(self, task):
        self.tasks.controls.remove(task)
        self.update()

    def update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        for task in self.tasks.controls:
            task.visible = (
                status == "All"
                or (status == "Active" and task.completed is False)
                or (status == "Completed" and task.completed)
            )
        super().update()

    def tabs_changed(self, e):
        self.update()
