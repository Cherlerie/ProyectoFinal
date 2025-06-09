import reflex as rx
from typing import List, Dict
from .lista import lista
from .descripcion_acuario_nacional import desc_acuario
from .reservas_acuario_nacional import reserva_acuario


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
                rx.link("Inicio", href="", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
                rx.link("Packs", href="", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
                rx.link("Sobre Nosotros", href="", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
                rx.link("Contactamos", href="", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
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
            "name": "Acuario Nacional",
            "description": "El Acuario Nacional ofrece una valiosa labor educativa y de conservación.Sus instalaciones están diseñadas para impartir información sobre las especies exhibidas y su hábitat",
            "rating": 4.9,
            "price_dop": 2150,
            "duration": "Recorrido de 2 horas",
            "image": "/imagenes/acuario.jpeg",
            "features": ["Experiencia 5 estrellas", "Transporte incluido", "Guía turístico"]
        },
        {
            "name": "Bahia de las Águilas",
            "description": "Bahía de las Águilas es una de las playas más impresionantes y vírgenes de la República Dominicana.La bahía no solo es un atractivo turístico, sino también un punto clave para la conservación ambiental en la región.",
            "rating": 4.8,
            "price_dop": 3200,
            "duration": "50 minutos en barco",
            "image": "/imagenes/bahiaaguilas.jpg",
            "features": ["Flotadores gratis", "Comidas típicas", "Transporte en barco/ Por tierra"]
        },
        {
            "name": "Cayo Levantado",
            "description": "Cayo Levantado es una pequeña isla ubicada en la Bahía de Samaná, en la República Dominicana. Es conocida por sus playas de arena blanca y aguas cristalinas.",
            "rating": 4.9,
            "price_dop": 2500,
            "duration": "40 minutos en barco",
            "image": "/imagenes/cayolevantado1.jpg",
            "features": ["Paseo en bote", "Comida Gratis", "Tour guiado"]
        },
        {
            "name": "Isla Catalina",
            "description": "Isla Catalina es una pequeña isla ubicada en el Mar Caribe, cerca de la costa de la República Dominicana. Actualmente, es un popular destino turístico.",
            "rating": 4.5,
            "price_dop": 2800,
            "duration": "30 minutos en barco",
            "image": "/imagenes/isla-catalina.jpg",
            "features": ["Snorkeling incluido", "Buceo", "Caminatas guiadas por la isla"]
        },
        {
            "name": "Playa el Valle",
            "description": "Playa El Valle es una playa ubicada en la República Dominicana, conocida por su belleza natural y tranquilidad.",
            "rating": 4.8,
            "price_dop": 3500,
            "duration": "45 minutos",
            "image": "/imagenes/playavalle.jpeg",
            "features": ["Caminata por la montaña", "Comida gratis", "Guía especializado"]
        },
        {
            "name": "Isla Saona",
            "description": "La Isla Saona es uno de los destinos turísticos más emblemáticos y visitados de la República Dominicana. A pesar de su popularidad, Isla Saona sigue siendo un paraíso natural relativamente bien conservado.",
            "rating": 4.9,
            "price_dop": 4500,
            "duration": "1 hora",
            "image": "/imagenes/saona2.jpeg",
            "features": ["Paseo en barco", "Comida gourmet", "Snorkeling incluido"]
        },
        {
            "name": "Ruinas de Engombre",
            "description": " Este sitio es significativo porque se cree que fue un asentamiento indígena que formó parte de la cultura taína antes de la llegada de los europeos.",
            "rating": 4.5,
            "price_dop": 1100,
            "duration": "2 horas",
            "image": "/imagenes/ruinassdo.jpg",
            "features": ["Tour por el lugar", "Guía especializado", "Historia indígena"]
        },
        {
            "name": "Las cuevas de Pomier",
            "description": "El Monumento Natural Reserva Antropológica Cuevas de Borbón o del Pomier, es un área protegida que comprende un conjunto de 54 cuevas y está localizada en el paraje Pomier del municipio San Cristóbal de la provincia San Cristóbal ",
            "rating": 5.0,
            "price_dop": 2200,
            "duration": "2 horas",
            "image": "/imagenes/pomier 05.jpg",
            "features": ["Tour", "Buffet Incluido", "Guía especializado"]
        },
        {
            "name": "Parque Colón",
            "description": "El Parque Colón es uno de los parques o plazas históricas de la Ciudad Colonial de Santo Domingo, el cual sirvió como centro principal de fiesta en la sociedad de la época colonial.",
            "rating": 4.7,
            "price_dop": 4000,
            "duration": "3 horas",
            "image": "/imagenes/colon.jpeg",
            "features": ["Tour", "Degustación", "Comida campesina"]
        },
        {
            "name": "Salto Del Limón",
            "description": "es una impresionante cascada ubicada en la Península de Samaná, República Dominicana, conocida por su espectacular belleza y su altura de aproximadamente 50 metros.",
            "rating": 4.7,
            "price_dop": 1800,
            "duration": "3 días / 2 noches",
            "image": "/imagenes/saltoellimon.jpg",
            "features": ["Cascada", "Rappel", "Flora y Fauna"]
        },
        {
            "name": "Dunas de Baní",
            "description": " Paisaje desértico único en el Caribe, con dunas que alcanzan hasta 35 metros de altura, Buen sitio para senderismo, fotografía y excursiones educativas. Vista impresionante del mar Caribe desde lo alto de las dunas.",
            "rating": 5.9,
            "price_dop": 16500,
            "duration": "1 días / 0 noches",
            "image": "/imagenes/dunasdebani.jpg",
            "features": ["Almuerzo en la playa", "Masaje para dos", "Tour privado"]
        },
        {
            "name": "Cabo Rojo",
            "description": "Playa de aguas turquesas intensas y arena clara y casi virgen, cercano a la Bahía de las Águilas, considerada una de las playas más hermosas del Caribe. Ideal para turismo ecológico, relajación y contacto con la naturaleza.",
            "rating": 4.3,
            "price_dop": 9500,
            "duration": "2 días / 1 noche",
            "image": "/imagenes/caborojo.png",
            "features": ["Actividades infantiles", "Playa familiar", "Show nocturno"]
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
                                                on_click=lambda: rx.redirect("/desc_acuario")
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
        {"name": "Punta Cana", "image": "/imagenes/puntacana.jpg"},
        {"name": "Santo Domingo", "image": "/imagenes/santodomingo.jpg"},
        {"name": "Samaná", "image": "/imagenes/samana.jpg"},
        {"name": "Santiago", "image": "/imagenes/santiago.jpg"},
        {"name": "La Romana", "image": "/imagenes/laromana.jpg"},
        {"name": "Puerto Plata", "image": "/imagenes/puertoplata.jpg"}
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
                    rx.link(
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
                            width="100%",
                            height="100%",
                        ),
                        href="/lista",
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
                    rx.link(
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
                            width="100%",
                            height="100%",
                        ),
                        href="/lista",
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
        {"name": "Santo Domingo", "lodgings": "75 Paquetes", "image": "imagenes/santodomingo.jpg"},
        {"name": "Punta Cana", "lodgings": "1,45 Paquetes", "image": "imagenes/puntacana.jpg"},
        {"name": "Puerto Plata", "lodgings": "42 Paquetes", "image": "imagenes/puertoplata.jpg"},
        {"name": "Santiago", "lodgings": "38 Paquetes", "image": "imagenes/santiago.jpg"},
        {"name": "Las Terrenas", "lodgings": "51 Paquetes", "image": "imagenes/Lasterrenas.jpg"},
        {"name": "Boca Chica", "lodgings": "20 Paquetes", "image": "imagenes/bocachica.jpg"},
        {"name": "La Romana", "lodgings": "31 Paquetes", "image": "imagenes/laromana.jpg"},
        {"name": "Jarabacoa", "lodgings": "15 Paquetes", "image": "imagenes/Jarabacoa.jpeg"},
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



app = rx.App()
app.add_page(index, route="/", title="RDExperience - Turismo RD")
app.add_page(desc_acuario, route="/desc_acuario", title="Descripcion Acuario Nacional")
app.add_page(lista, route="/lista", title="Lista")
app.add_page(reserva_acuario, route="/reserva_acuario", title="Reservacion de Acuario")