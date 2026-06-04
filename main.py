# Kevin Eduardo Baxin

# main.py

import flet as ft

from login import mostrar_login
from dashboard import mostrar_dashboard
from crud_alumnos import mostrar_crud

def main(page: ft.Page):

```
page.title = "Sistema Integral de Control Escolar"
page.window.width = 1200
page.window.height = 800

page.theme_mode = ft.ThemeMode.LIGHT

page.bgcolor = ft.Colors.BLUE_GREY_50

page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
page.vertical_alignment = ft.MainAxisAlignment.CENTER

# -----------------------------------------
# NAVEGACIÓN
# -----------------------------------------

def ir_login():
    page.clean()
    mostrar_login(page, ir_dashboard)

def ir_dashboard():
    page.clean()
    mostrar_dashboard(
        page,
        ir_crud,
        ir_login
    )

def ir_crud():
    page.clean()
    mostrar_crud(
        page,
        ir_dashboard
    )

# Iniciar en Login
ir_login()

page.update()
```

ft.app(target=main)