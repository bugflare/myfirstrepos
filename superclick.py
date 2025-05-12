import flet as ft

def main(page: ft.Page):
    page.title = "click Counter"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    count = ft.Text("0", size=20, weight=ft.FontWeight.BOLD)
    
    def increment(e):
        count.value = str(int(count.value) + 1)
        page.update()
    
    def reset(e):
        count.value = "0"
        page.update()
    
    increment_button = ft.ElevatedButton("click me", on_click=increment)
    reset_button = ft.ElevatedButton("reset", on_click=reset)
    
    page.add(count, increment_button, reset_button)

ft.app(target=main)
