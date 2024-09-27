import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.bgcolor = "yellow"
    
    txtPeso = ft.TextField(label="Ingresa tu peso (kg)")
    txtAltura = ft.TextField(label="Ingresa tu altura (m)")
    lblIMC = ft.Text("Tu IMC es de: ")
    
    img = ft.Image(
        src="https://github.com/Prof-Luis1986/Recursos/raw/main/Bascula.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN
    )
    
    def calcular_imc(e):
        try:
            peso = float(txtPeso.value)
            altura = float(txtAltura.value)
            imc = peso / (altura ** 2)
            lblIMC.value = f"Tu IMC es de: {imc:.2f}"
            lblIMC.update()
        except ValueError:
            lblIMC.value = "Por favor, ingresa valores válidos."
            lblIMC.update()
    
    def limpiar(e):
        txtPeso.value = ""
        txtAltura.value = ""
        lblIMC.value = "Tu IMC es de: "
        txtPeso.update()
        txtAltura.update()
        lblIMC.update()

    btnCalcular = ft.ElevatedButton(text="Calcular", on_click=calcular_imc)
    btnLimpiar = ft.ElevatedButton(text="Limpiar", on_click=limpiar)
    
    page.add(
        ft.Column(
            controls=[
                txtPeso,
                txtAltura,
                lblIMC
            ],
            alignment="CENTER"
        ),
        ft.Row(
            controls=[
                img
            ],
            alignment="CENTER"
        ),
        ft.Row(
            controls=[
                btnCalcular,
                btnLimpiar
            ],
            alignment="CENTER"
        )
    )

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
