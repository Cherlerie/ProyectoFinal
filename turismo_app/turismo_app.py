import reflex as rx

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.center(  # Centrado del contenido
                rx.vstack(
                    imgprincipal(),
                    compact_filter(),
                    spacing="0",
                ),
                width="100%",
            ),
            position="relative",
            width="100%",
            padding_bottom="5em",  # Para que el filtro no quede pegado abajo
        ),
        font_family="Arial, sans-serif",
        color="#333",
        bg="#2C3949",
        width="100%",
        min_height="100vh",
    )

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.heading("SDExperience", size="6", color="white"),
            flex="1",
        ),
        
        rx.center(
            rx.hstack(
                rx.link("Inicio", href="/", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
                rx.link("Packs", href="#descripcion.py", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
                rx.link("Sobre Nosotros", href="#", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
                rx.link("Contactamos", href="#", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
                spacing="0",
            ),
            width="100%",
            position="absolute",
            left="50%",
            transform="translateX(-50%)",
        ),
        
        rx.box(
            rx.button(
                "Reservar",
                color_scheme="blue",
                size="4",
                border_radius="full",
                _hover={"transform": "scale(1.05)"},
                padding_x="2em",
            ),
            flex="1",
            display="flex",
            justify_content="flex-end",
        ),
        
        padding_x="2em",
        padding_y="2em",
        bg="#2C3949",
        position="sticky",
        top="0",
        z_index="1000",
        width="100%",
        height="80px",
        align="center",
    )

def imgprincipal() -> rx.Component:
    return rx.image(
        src="/imagenes/imgprincipal.png",
        width="100%",
        max_width="1200px",
        height="auto",
        border_radius="4",
        margin_y="3em",
    )

def compact_filter() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.vstack(
                rx.text("Destino", color="black", font_weight="bold"),
                rx.select(
                    ["Punta Cana", "Santo Domingo", "Samaná"],
                    placeholder="Selecciona un destino",
                    size="2",
                    width="180px",
                    variant="classic",
                    bg="white",
                    border_radius="3",
                    box_shadow="2"
                ),
            ),
            rx.vstack(
                rx.text("Fecha de Entrada", color="black", font_weight="bold"),
                rx.input(
                    placeholder="Fecha entrada",
                    type="date",
                    size="2",
                    width="140px",
                    bg="white",
                    border_radius="3",
                    box_shadow="2"
                ),
            ),
            rx.vstack(
                rx.text("Fecha de Salida", color="black", font_weight="bold"),
                rx.input(
                    placeholder="Fecha salida",
                    type="date",
                    size="2",
                    width="140px",
                    bg="white",
                    border_radius="3",
                    box_shadow="2"
                ),
            ),
            rx.vstack(
                rx.text("Personas", color="black", font_weight="bold"),
                rx.select(
                    ["1 adulto", "2 adultos", "3 adultos"],
                    size="2",
                    width="130px",
                    variant="classic",
                    bg="white",
                    border_radius="3",
                    box_shadow="2"
                ),
            ),
            rx.vstack(
                rx.text(""),
                rx.button(
                    "Buscar",
                    size="2",
                    width="100px",
                    variant="classic",
                    color_scheme="blue",
                    border_radius="3",
                    box_shadow="3",
                    margin_top="1.7em",
                ),
            ),
            spacing="4",
            width="100%",
            max_width="900px",
        ),
        padding="1.5em",
        bg="white",
        border_radius="8px",
        box_shadow="lg",
        position="absolute",
        top="68%",  # <-- Ajusta este valor si quieres subirlo más o menos
        left="50%",
        transform="translateX(-50%)",
        z_index="5",
    )

# app = rx.App(assets_path="../assets")
app = rx.App()
app.add_page(index, route="/", title="SDExperience - Turismo RD")
