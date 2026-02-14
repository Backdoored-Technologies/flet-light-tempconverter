# Light Temperature App  (lt_app.py)

import flet as ft



#app structure
def main(page: ft.Page):
    page.title = "Temperature Conversion Tool"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 1080
    page.window_height = 720
    page.window_resizeable = True
    page.padding = 20

    #input fields for temperature
    c_input = ft.TextField(
        expand=1,
        label="Celsius (°C)",
        hint_text = "Input Temperature in Celsius",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.GREY,
        # border_color=ft.Colors.BLACK,
    )

    f_input = ft.TextField(
        expand=1,
        label="Fahrenheit (°F)",
        hint_text = "Input Temperature in Fahrenheit",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.GREY,
    )

    k_input = ft.TextField(
        expand=1,
        label="Kelvin (K)",
        hint_text = "Input Temperature in Kelvin",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.GREY,
    )
    
    r_input = ft.TextField(
        expand=1,
        label="Rankine (°R)",
        hint_text = "Input Temperature in Rankine",
        keyboard_type=ft.KeyboardType.NUMBER,
        color=ft.Colors.GREY,
    )

    c_output = ft.Text(f"", size=16, color=ft.Colors.BLUE_600)
    f_output = ft.Text(f"", size=16, color=ft.Colors.RED_600)
    k_output = ft.Text(f"", size=16, color=ft.Colors.GREEN_600)
    r_output = ft.Text(f"", size=16, color=ft.Colors.ORANGE)

    #c f k r

    def color_change():
        c_output.color=ft.Colors.BLUE_600
        f_output.color=ft.Colors.BLUE_600
        k_output.color=ft.Colors.BLUE_600
        r_output.color=ft.Colors.BLUE_600
        page.update()

    def invalid_input():
        c_output.value = "Invalid Input"
        f_output.value = "Invalid Input"
        k_output.value = "Invalid Input"
        r_output.value = "Invalid Input"

    def handle_c_input(e):
        try:
            c_value = float(e.control.value)
            print(f"Celsius value entered: {c_value}")

            f_value = float((c_value * (9/5)) + 32)
            k_value = float(c_value + 273.15)
            r_value = float((c_value * 9/5) + 491.67)
            print(f"F defined as: {f_value}, K defined as: {k_value}, R defined as {r_value}")
            
            #color shit here
            color_change()
            c_output.color = ft.Colors.RED_600

            c_output.value = f"Output - Celsius: {c_value:.3f}°C"
            f_output.value = f"Output - Fahrenheit: {f_value:.3f}°F"
            k_output.value = f"Output - Kelvin: {k_value:.3f}K"
            r_output.value = f"Output - Rankine {r_value:.3f}°R"
            page.update()
        except ValueError:
            print("Invalid input")

            invalid_input()
            page.update()

    
    def handle_f_input(e):
        try:
            f_value = float(e.control.value)
            print(f"Fahrenheit value entered: {f_value}")

            c_value = float((f_value - 32) * (5/9))
            k_value = float((f_value + 459.67) * (5/9))
            r_value = float(f_value + 459.67)

            color_change()
            f_output.color = ft.Colors.RED_600

            c_output.value = f"Output - Celsius: {c_value:.3f}°C"
            f_output.value = f"Output - Fahrenheit: {f_value:.3f}°F"
            k_output.value = f"Output - Kelvin: {k_value:.3f}K"
            r_output.value = f"Output - Rankine {r_value:.3f}°R"
            page.update()
        except ValueError:
            invalid_input()
            page.update()

    def handle_k_input(e):
        color_change()
        k_output.color = ft.Colors.RED_600
        
        try:
            k_value = float(e.control.value)
            print(f"Kelvin value entered: {k_value}")

            c_value = float(k_value - 273.15)
            f_value = float((k_value * (9/5)) - 459.67)
            r_value = float(k_value * (9/5))

            #how can I reuse these 4 lines below? solve later
            c_output.value = f"Output - Celsius: {c_value:.3f}°C"
            f_output.value = f"Output - Fahrenheit: {f_value:.3f}°F"
            k_output.value = f"Output - Kelvin: {k_value:.3f}K"
            r_output.value = f"Output - Rankine {r_value:.3f}°R"

            page.update()
        except ValueError:
            invalid_input()
            page.update()

    def handle_r_input(e):
        color_change()
        r_output.color = ft.Colors.RED_600

        try:
            r_value = float(e.control.value)
            print(f"Rankine value entered: {r_value}")

            c_value = float((r_value - 491.67) * (5/9))
            f_value = float(r_value - 459.67)
            k_value = float(r_value * (5/9))

            c_output.value = f"Output - Celsius: {c_value:.3f}°C"
            f_output.value = f"Output - Fahrenheit: {f_value:.3f}°F"
            k_output.value = f"Output - Kelvin: {k_value:.3f}K"
            r_output.value = f"Output - Rankine {r_value:.3f}°R"
        except ValueError:
            invalid_input()
            page.update()


    c_input.on_submit = handle_c_input
    f_input.on_submit = handle_f_input
    k_input.on_submit = handle_k_input
    r_input.on_submit = handle_r_input

    def clear_all(e):
        c_output.value=""
        f_output.value = ""
        k_output.value = ""
        r_output.value = ""

        c_input.value = ""
        f_input.value = ""
        k_input.value = ""
        r_input.value = ""
        page.update()


    #main ui /  container
    page.add(
        ft.Column([
            ft.Text(
                "Temperature Conversion Tool",
                size=30,
                weight=ft.FontWeight.BOLD,
                text_align=ft.TextAlign.CENTER,
                # color=ft.Colors.BLUE_700,
            ),
            ft.Divider(height=5),
            
            c_input,
            ft.Divider(height=10),
            f_input,
            ft.Divider(height=10),
            k_input,
            ft.Divider(height=10),
            r_input,
            ft.Divider(height=10),

            ft.Button(
                "Clear All",
                icon=ft.Icons.CLEAR,
                style=ft.ButtonStyle(
                    bgcolor=ft.Colors.RED_400,
                    color=ft.Colors.BLACK,
                ),
                on_click=clear_all,
            ),

            ft.Divider(height=10),
            c_output,
            f_output,
            k_output,
            r_output,
            ft.Divider(height=10),

            #div
            ft.Container(
                content=ft.Column([
                    ft.Text("Unit Conversion Formulas Below:", weight=ft.FontWeight.BOLD, size=16),
                    ft.Text(" - Celsius (°C) to X", weight=ft.FontWeight.BOLD, size = 14),
                    ft.Text(" - Celsius (°C) to Fahrenheit (°F)   =>   °F = °C × 9/5 + 32"),
                    ft.Text(" - Celsius (°C) to Kelvin (K)       =>   K = °C + 273.15"),
                    ft.Text(" - Celsius (°C) to Rankine (°R)       =>   °R = °C × 9/5 + 491.67"),
                    ft.Divider(height=5),
                    ft.Text(" - Fahrenheit (°F) to X", weight=ft.FontWeight.BOLD, size = 14),
                    ft.Text(" - Fahrenheit (°F) to Celsius (°C)    =>   °C = (°F − 32) × 5/9"),
                    ft.Text(" - Fahrenheit (°F) to Kelvin (K)     =>   K = (°F + 459.67) × 5/9"),
                    ft.Text(" - Fahrenheit (°F) to Rankine (°R)       =>   °R = °F + 459.67"),
                    ft.Divider(height=5),
                    ft.Text(" - Kelvin (K) to X", weight=ft.FontWeight.BOLD, size = 14),
                    ft.Text(" - Kelvin (K) to Celsius (°C)        =>   °C = K − 273.15"),
                    ft.Text(" - Kelvin (K) to Fahrenheit (°F)     =>   °F = K × 9/5 − 459.67"),
                    ft.Text(" - Kelvin (K) to Rankine (°R)       =>   °R = K × 9/5"),
                    ft.Divider(height=5),
                    ft.Text(" - Rankine (°R) to X", weight=ft.FontWeight.BOLD, size = 14),
                    ft.Text(" - Rankine (°R) to Celsius (°C)        =>   °C = K − 273.15"),
                    ft.Text(" - Rankine (°R) to Fahrenheit (°F)     =>   °F = K × 9/5 − 459.67"),
                    ft.Text(" - Rankine (°R) to Kelvin (K)       =>   K = °R × 5/9"),
                    ft.Divider(height=5),
                ])
            ),
            
            # can use column or container, have to specify content= with container

        ])
    )

if __name__ == "__main__":
    ft.run(main)

    # put input fields and output fields at the bottom
    # code logic