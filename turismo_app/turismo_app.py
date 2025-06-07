import reflex as rx

class State(rx.State):
    pass
def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.box(
            rx.center(  
                rx.vstack(
                    imgprincipal(),
                    compact_filter(),
                    spacing="0",
                ),
                width="100%",
            ),
            position="relative",
            width="100%",
            padding_bottom="5em",  
        ),
        rx.box(  
            trending_destinations(),
            max_width="1200px",
            width="100%",
            margin="0 auto",
            padding_x="1em",
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
        box_shadow="4",
        position="absolute",
         margin_top="-3em",
        top="68%",  
        left="50%",
        transform="translateX(-50%)",
        z_index="5",
    )

def trending_destinations() -> rx.Component:
    destinations = [
        {"name": "Santo Domingo", "location": "República Dominicana", "rating": "1230", "comments": "90 comentarios", "hashtag": True, "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Puerto Plata", "location": "República Dominicana", "rating": "1434", "comments": "166 comentarios", "hashtag": True, "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Pedernales", "location": "República Dominicana", "rating": "446", "comments": "148 comentarios", "hashtag": False, "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Punta Cana", "location": "República Dominicana", "rating": "952", "comments": "210 comentarios", "hashtag": True, "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Santiago", "location": "República Dominicana", "rating": "394", "comments": "185 comentarios", "hashtag": False, "image": "/imagenes/parque3ojos.jpg"},
        {"name": "San Juan", "location": "República Dominicana", "rating": "703", "comments": "120 comentarios", "hashtag": False, "image": "/imagenes/parque3ojos.jpg"},
        {"name": "San Pedro", "location": "República Dominicana", "rating": "922", "comments": "95 comentarios", "hashtag": False, "image": "/imagenes/parque3ojos.jpg"},
        {"name": "La Romana", "location": "República Dominicana", "rating": "91", "comments": "88 comentarios", "hashtag": True, "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Bávaro", "location": "República Dominicana", "rating": "90", "comments": "75 comentarios", "hashtag": False, "image": "/imagenes/parque3ojos.jpg"},
    ]

    rows = [destinations[i:i + 3] for i in range(0, len(destinations), 3)]

    return rx.box(
        rx.vstack(
            rx.heading(
                "Destinos de moda",
                size="6",
                color="white",
                margin_top="4em",
                margin_bottom="1em",
            ),
            rx.text(
                "Opciones más populares entre la comunidad viajera de la República Dominicana",
                color="rgba(255, 255, 255, 0.8)",
                size="3",
                margin_bottom="3em",
            ),
            rx.vstack(
                *[
                    rx.hstack(
                        *[
                            rx.box(
                                rx.image(
                                    src=dest["image"],
                                    width="100%",
                                    height="200px",
                                    object_fit="cover",
                                    border_radius="8px 8px 0 0",
                                ),
                                rx.box(
                                    rx.vstack(
                                        rx.hstack(
                                            rx.text(
                                                dest["name"],
                                                font_weight="bold",
                                                color="white",
                                                size="3",
                                            ),
                                            rx.cond(
                                                dest["hashtag"],
                                                rx.text("#", color="blue.400", size="3"),
                                            ),
                                            align_items="center",
                                            spacing="2",
                                        ),
                                        rx.text(
                                            dest["location"],
                                            color="rgba(255, 255, 255, 0.8)",
                                            size="2",
                                        ),
                                        rx.hstack(
                                            rx.text(
                                                dest["rating"],
                                                color="white",
                                                font_weight="bold",
                                                size="3",
                                            ),
                                            rx.text(
                                                "Excelente",
                                                color="rgba(255, 255, 255, 0.8)",
                                                size="2",
                                            ),
                                            spacing="2",
                                        ),
                                        rx.text(
                                            dest["comments"],
                                            color="rgba(255, 255, 255, 0.8)",
                                            size="2",
                                        ),
                                        align_items="flex-start",
                                        spacing="1",
                                    ),
                                    padding="1.5em",
                                    bg="rgba(47, 59, 73, 0.9)",
                                    border_radius="0 0 8px 8px",
                                ),
                                border_radius="8px",
                                box_shadow="md",
                                overflow="hidden",
                                _hover={
                                    "transform": "translateY(-5px)",
                                    "transition": "transform 0.2s",
                                },
                                width="100%",
                                margin_x="1em",
                            )
                            for dest in row
                        ],
                        width="100%",
                        max_width="1200px",
                        justify="center",
                        spacing="4",
                    )
                    for row in rows
                ],
                spacing="4",
                width="100%",
            ),
            width="100%",
            align="center",
            padding_bottom="4em",
        ),
        width="100%",
        bg="#2C3949",
    )

# app = rx.App(assets_path="../assets")
app = rx.App()
app.add_page(index, route="/", title="SDExperience - Turismo RD")
