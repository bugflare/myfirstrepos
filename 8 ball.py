import flet as ft
import random

def main(page: ft.Page):
    page.title = "Magic 8 Ball"
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    responses = {
        "Yes": "green",
        "No": "red",
        "Maybe": "orange",
        "Ask again later": "blue",
        "Definitely": "green",
        "Absolutely not": "red",
        "Possibly": "orange",
        "Cannot predict now": "blue"
    }
    
    def get_response(e):
        question = question_input.value.strip()
        if question:
            answer, color = random.choice(list(responses.items()))
            response_text.value = answer
            response_text.color = color
            page.update()
        else:
            response_text.value = "ask a question"
            response_text.color = "black"
            page.update()

    question_input = ft.TextField(label="put your question here")
    ask_button = ft.ElevatedButton("Ask the 8 Ball", on_click=get_response)
    response_text = ft.Text("", size=20, weight=ft.FontWeight.BOLD)
    
    page.add(question_input, ask_button, response_text)

ft.app(target=main)
