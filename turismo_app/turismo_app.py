import reflex as rx
from typing import List, Dict



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
            popular_places(),
            provinces_carousel(),
           #  trending_destinations(),
            packages_section(),
           
            max_width="1200px",
            width="100%",
            margin="0 auto",
            padding_x="1em",
        ),
        footer(),
        font_family="Arial, sans-serif",
        color="#333",
        bg="#2C3949",
        width="100%",
        min_height="100vh",
    )


def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.heading("RDExperience", size="6", color="white"),
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

def packages_section() -> rx.Component:
    packages = [
        {
            "name": "Aventura en Punta Cana",
            "description": "Todo incluido con excursiones acuáticas",
            "rating": 4.8,
            "price_dop": 12500,
            "duration": "3 días / 2 noches",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Alojamiento 5 estrellas", "Transporte incluido", "Guía turístico"]
        },
        {
            "name": "Cultural Santo Domingo",
            "description": "Tour histórico por la Zona Colonial",
            "rating": 4.6,
            "price_dop": 8500,
            "duration": "2 días / 1 noche",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Visita a museos", "Comidas típicas", "Transporte privado"]
        },
        {
            "name": "Relax en Samaná",
            "description": "Escape a las playas vírgenes",
            "rating": 4.9,
            "price_dop": 15000,
            "duration": "4 días / 3 noches",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Cabaña frente al mar", "Masajes incluidos", "Tour a Salto El Limón"]
        },
        {
            "name": "Montañas de Jarabacoa",
            "description": "Aventura en el corazón de RD",
            "rating": 4.7,
            "price_dop": 9800,
            "duration": "3 días / 2 noches",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Rafting incluido", "Cena campestre", "Caminatas guiadas"]
        },
        {
            "name": "City Tour Santiago",
            "description": "Lo mejor de la ciudad corazón",
            "rating": 4.5,
            "price_dop": 6500,
            "duration": "1 día completo",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Visita a monumentos", "Degustación de ron", "Guía especializado"]
        },
        {
            "name": "Paraíso en Bahía de las Águilas",
            "description": "Experiencia en playa virgen",
            "rating": 4.9,
            "price_dop": 13500,
            "duration": "3 días / 2 noches",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Camping premium", "Comida gourmet", "Snorkeling incluido"]
        },
        {
            "name": "Eco-Tour Los Haitises",
            "description": "Naturaleza y cuevas milenarias",
            "rating": 4.8,
            "price_dop": 11000,
            "duration": "2 días / 1 noche",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Tour en lancha", "Avistamiento de aves", "Almuerzo tradicional"]
        },
        {
            "name": "Lujo en Cap Cana",
            "description": "Experiencia exclusiva en resort VIP",
            "rating": 5.0,
            "price_dop": 22000,
            "duration": "4 días / 3 noches",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Villa privada", "Golf incluido", "Spa ilimitado"]
        },
        {
            "name": "Ruta del Café Barahona",
            "description": "Conoce el proceso del café dominicano",
            "rating": 4.4,
            "price_dop": 7500,
            "duration": "1 día completo",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Tour de café", "Degustación", "Comida campesina"]
        },
        {
            "name": "Aventura Extrema Constanza",
            "description": "Para los amantes de la adrenalina",
            "rating": 4.7,
            "price_dop": 12800,
            "duration": "2 días / 1 noche",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Parapente", "Rappel", "Ciclismo de montaña"]
        },
        {
            "name": "Romántico Bayahibe",
            "description": "Escape para parejas",
            "rating": 4.9,
            "price_dop": 16500,
            "duration": "3 días / 2 noches",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Cena en la playa", "Masaje para dos", "Tour privado"]
        },
        {
            "name": "Familiar Boca Chica",
            "description": "Diversión para toda la familia",
            "rating": 4.3,
            "price_dop": 9500,
            "duration": "2 días / 1 noche",
            "image": "/imagenes/parque3ojos.jpg",
            "features": ["Actividades infantiles", "Piscina familiar", "Show nocturno"]
        }
    ]
    

    rows = [packages[i:i + 3] for i in range(0, len(packages), 3)]

    return rx.box(
        rx.vstack(
            rx.heading(
                "Paquetes Turísticos",
                size="6",
                color="white",
                margin_top="4em",
                margin_bottom="1em",
            ),
            rx.text(
                "Descubre las mejores experiencias que ofrecemos en la República Dominicana",
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
                                    src=pkg["image"],
                                    width="100%",
                                    height="200px",
                                    object_fit="cover",
                                    border_radius="8px 8px 0 0",
                                ),
                                rx.box(
                                    rx.vstack(
                                        rx.hstack(
                                            rx.text(
                                                pkg["name"],
                                                font_weight="bold",
                                                color="white",
                                                size="3",
                                            ),
                                            rx.spacer(),
                                            rx.badge(
                                                f"{pkg['rating']} ★",
                                                color_scheme="green",
                                                variant="soft",
                                            ),
                                            width="100%",
                                        ),
                                        rx.text(
                                            pkg["description"],
                                            color="rgba(255, 255, 255, 0.8)",
                                            size="2",
                                        ),
                                        rx.text(
                                            pkg["duration"],
                                            color="rgba(255, 255, 255, 0.7)",
                                            size="1",
                                        ),
                                        rx.vstack(
                                            *[
                                                rx.hstack(
                                                    rx.box(
                                                        width="8px",
                                                        height="8px",
                                                        bg="blue.400",
                                                        border_radius="full",
                                                        margin_right="8px",
                                                    ),
                                                    rx.text(
                                                        feature,
                                                        color="rgba(255, 255, 255, 0.8)",
                                                        size="1",
                                                    ),
                                                    align_items="center",
                                                )
                                                for feature in pkg["features"]
                                            ],
                                            spacing="1",
                                            margin_y="1em",
                                        ),
                                        rx.hstack(
                                            rx.text(
                                                f"RD${pkg['price_dop']:,}",
                                                color="white",
                                                font_weight="bold",
                                                size="4",
                                            ),
                                            rx.spacer(),
                                            rx.button(
                                                "Reservar",
                                                size="1",
                                                variant="solid",
                                                color_scheme="blue",
                                            ),
                                            width="100%",
                                        ),
                                        align_items="flex-start",
                                        spacing="2",
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
                            for pkg in row
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

def popular_places() -> rx.Component:
    places = [
        {"name": "Punta Cana", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Santo Domingo", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Samaná", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Santiago", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "La Romana", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Puerto Plata", "image": "/imagenes/parque3ojos.jpg"}
    ]

    first_row = places[:3]
    second_row = places[3:]

    return rx.box(
        rx.vstack(
            rx.heading(
                "Lugares Más Visitados",
                size="6",
                color="white",
                margin_top="4em",
                margin_bottom="1em",
            ),
            rx.text(
                "Los destinos más populares de República Dominicana",
                color="rgba(255, 255, 255, 0.8)",
                size="3",
                margin_bottom="3em",
            ),
            rx.hstack(
                *[
                    rx.box(
                        rx.image(
                            src=place["image"],
                            width="100%",
                            height="200px",
                            object_fit="cover",
                            border_radius="8px",
                        ),
                        rx.center(
                            rx.heading(
                                place["name"],
                                size="4",
                                color="white",
                                position="absolute",
                                bottom="20px",
                                left="0",
                                right="0",
                                text_shadow="0 2px 4px rgba(0,0,0,0.5)",
                            ),
                        ),
                        position="relative",
                        border_radius="8px",
                        box_shadow="md",
                        overflow="hidden",
                        _hover={
                            "transform": "scale(1.03)",
                            "transition": "transform 0.3s",
                        },
                        flex="1",
                        min_width="200px",
                        margin_x="0.5em",
                    )
                    for place in first_row
                ],
                width="100%",
                max_width="1200px",
                spacing="4",
                justify="center",
            ),
            rx.hstack(
                *[
                    rx.box(
                        rx.image(
                            src=place["image"],
                            width="100%",
                            height="200px",
                            object_fit="cover",
                            border_radius="8px",
                        ),
                        rx.center(
                            rx.heading(
                                place["name"],
                                size="4",
                                color="white",
                                position="absolute",
                                bottom="20px",
                                left="0",
                                right="0",
                                text_shadow="0 2px 4px rgba(0,0,0,0.5)",
                            ),
                        ),
                        position="relative",
                        border_radius="8px",
                        box_shadow="md",
                        overflow="hidden",
                        _hover={
                            "transform": "scale(1.03)",
                            "transition": "transform 0.3s",
                        },
                        flex="1",
                        min_width="200px",
                        margin_x="0.5em",
                    )
                    for place in second_row
                ],
                width="100%",
                max_width="1200px",
                spacing="4",
                justify="center",
                margin_top="1em",
            ),
            width="100%",
            align="center",
            padding_bottom="4em",
        ),
        width="100%",
        bg="#2C3949",
    )


class State(rx.State):
    current_slide: int = 0
    provinces: List[Dict[str, str]] = [
        {"name": "Santo Domingo", "lodgings": "75 Paquetes", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Punta Cana", "lodgings": "1,45 Paquetes", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Puerto Plata", "lodgings": "42 Paquetes", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Santiago", "lodgings": "38 Paquetes", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Las Terrenas", "lodgings": "51 Paquetes", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Boca Chica", "lodgings": "20 Paquetes", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "La Romana", "lodgings": "31 Paquetes", "image": "/imagenes/parque3ojos.jpg"},
        {"name": "Jarabacoa", "lodgings": "15 Paquetes", "image": "/imagenes/parque3ojos.jpg"},
    ]

    @rx.var
    def visible_provinces(self) -> List[Dict[str, str]]:
        return self.provinces[self.current_slide:self.current_slide+4]

    def next_slide(self):
        if self.current_slide < len(self.provinces) - 4:
            self.current_slide += 1

    def prev_slide(self):
        if self.current_slide > 0:
            self.current_slide -= 1

def province_card(province: Dict[str, str]) -> rx.Component:
    return rx.box(
        rx.image(
            src=province["image"],
            width="180px",
            height="120px",
            object_fit="cover",
            border_radius="8px",
        ),
        rx.vstack(
            rx.text(
                province["name"],
                font_weight="bold",
                color="white",
                size="2",
            ),
            rx.text(
                province["lodgings"],
                color="rgba(255, 255, 255, 0.8)",
                size="1",
            ),
            align_items="flex-start",
            spacing="1",
            padding="0.5em",
            bg="rgba(0, 0, 0, 0.6)",
            border_radius="0 0 8px 8px",
            width="100%",
        ),
        position="relative",
        width="180px",
        margin_x="0.5em",
    )

def provinces_carousel() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading(
                "Explora Todas las Provincias",
                size="5",
                color="white",
                margin_bottom="1em",
            ),
            rx.hstack(
                rx.button(
                    rx.icon(tag="chevron-left", size=24),
                    on_click=State.prev_slide,
                    variant="ghost",
                    color="white",
                    _hover={"bg": "rgba(255,255,255,0.1)"},
                ),
                rx.box(
                    rx.hstack(
                        rx.foreach(
                            State.visible_provinces,
                            province_card
                        ),
                        spacing="2",
                    ),
                    width="800px",
                    overflow="hidden",
                ),
                rx.button(
                    rx.icon(tag="chevron-right", size=24),
                    on_click=State.next_slide,
                    variant="ghost",
                    color="white",
                    _hover={"bg": "rgba(255,255,255,0.1)"},
                ),
                align="center",
                spacing="2",
            ),
            align="center",
            padding_y="2em",
        ),
        width="100%",
        bg="#2C3949",
    )

def footer_item(text: str, href: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="3", color="rgba(255, 255, 255, 0.8)"),
        href=href,
        _hover={"color": "white"}
    )

def footer_items_destinations() -> rx.Component:
    return rx.flex(
        rx.heading(
            "DESTINOS", size="4", weight="bold", as_="h3", color="white"
        ),
        footer_item("Punta Cana", "/#"),
        footer_item("Santo Domingo", "/#"),
        footer_item("Samaná", "/#"),
        footer_item("Santiago", "/#"),
        footer_item("Puerto Plata", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def footer_items_services() -> rx.Component:
    return rx.flex(
        rx.heading(
            "SERVICIOS", size="4", weight="bold", as_="h3", color="white"
        ),
        footer_item("Paquetes Turísticos", "/#"),
        footer_item("Tours Privados", "/#"),
        footer_item("Transporte", "/#"),
        footer_item("Alojamiento", "/#"),
        footer_item("Excursiones", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def footer_items_company() -> rx.Component:
    return rx.flex(
        rx.heading(
            "EMPRESA", size="4", weight="bold", as_="h3", color="white"
        ),
        footer_item("Sobre Nosotros", "/#"),
        footer_item("Nuestro Equipo", "/#"),
        footer_item("Testimonios", "/#"),
        footer_item("Blog", "/#"),
        footer_item("Contacto", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def social_link(icon: str, href: str) -> rx.Component:
    return rx.link(
        rx.icon(icon, color="rgba(255, 255, 255, 0.8)", size=20),
        href=href,
        _hover={"color": "white", "transform": "scale(1.1)"},
        transition="all 0.2s"
    )

def socials() -> rx.Component:
    return rx.flex(
        social_link("instagram", "/#"),
        social_link("twitter", "/#"),
        social_link("facebook", "/#"),
        social_link("youtube", "/#"),
        spacing="4",
        justify="center",
        flex_shrink="0",
    )

def footer() -> rx.Component:
    return rx.el.footer(
        rx.container(
            rx.vstack(
                rx.flex(
                    rx.vstack(
                        rx.hstack(
                            rx.heading(
                                "RDExperience",
                                size="7",
                                weight="bold",
                                color="white",
                            ),
                            align_items="center",
                        ),
                        rx.text(
                            "Tu mejor experiencia turística en República Dominicana",
                            size="3",
                            color="rgba(255, 255, 255, 0.7)",
                            text_align=["center", "center", "start"],
                            max_width="250px",
                            line_height="1.5",
                        ),
                        rx.text(
                            "© 2024 RDExperience. Todos los derechos reservados.",
                            size="2",
                            color="rgba(255, 255, 255, 0.6)",
                            white_space="nowrap",
                            weight="medium",
                        ),
                        spacing="4",
                        align_items=[
                            "center",
                            "center",
                            "start",
                        ],
                        flex_shrink="0",
                    ),
                    footer_items_destinations(),
                    footer_items_services(),
                    footer_items_company(),
                    justify="between",
                    spacing="8",
                    flex_direction=["column", "column", "row"],
                    flex_wrap="wrap",
                ),
                rx.divider(color_scheme="gray", opacity="0.3"),
                rx.hstack(
                    rx.hstack(
                        footer_item("Política de Privacidad", "/#"),
                        footer_item("Términos y Condiciones", "/#"),
                        footer_item("Preguntas Frecuentes", "/#"),
                        spacing="6",
                        align="center",
                        flex_wrap="wrap",
                    ),
                    socials(),
                    justify="between",
                    align="center",
                    flex_direction=["column", "column", "row"],
                    spacing="4",
                ),
                spacing="6",
                align="center",
            ),
            max_width="1200px",
            padding_x="2em",
        ),
        bg="#1a2332",
        padding_y="3em",
        border_top="1px solid rgba(255, 255, 255, 0.1)",
    )


# app = rx.App(assets_path="../assets")
app = rx.App()
app.add_page(index, route="/", title="RDExperience - Turismo RD")