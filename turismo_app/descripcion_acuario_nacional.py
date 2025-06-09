
import reflex as rx
from typing import List, Dict

class PropertyState(rx.State):
    """Estado para manejar la información de la propiedad."""
    
    # Variables de estado reactivas
    title: str = "Acuario Nacional"
    rating: float = 4.3
    reviews: int = 586
    location: str = "Av. España 75, Santo Domingo Este 10205, República Dominicana"
    location_quality: str = "Muy buena ubicación"
    map_score: float = 8.1
    guest_review: str = "Muy bien decorado y un ambiente agradable."
    guest_name: str = "Maria"
    guest_country: str = "Venezolana"
    personal_rating: float = 8.2
    
    description: str = "El Acuario Nacional, ubicado en Santo Domingo, es un espacio ideal para los amantes de la vida marina. Cuenta con numerosos tanques y túneles que permiten observar de cerca especies del mar Caribe, como tiburones, tortugas, rayas y peces tropicales. Además, ofrece zonas al aire libre con vistas al mar y áreas para el descanso familiar. El lugar dispone de estacionamiento, tienda de recuerdos y guías que explican el recorrido. Está abierto todos los días y es perfecto para visitas educativas o en familia."
    room_description: str = "El lugar dispone de estacionamiento, tienda de recuerdos y guías que explican el recorrido. Está abierto todos los días y es perfecto para visitas educativas o en familia."
    breakfast_info: str = " "
    location_info: str = ""
    
    main_image: str = "data:image/jpeg;base64,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"
    images: List[str] = [
        "https://pedritopuntacana.com/wp-content/uploads/2017/01/acuario-7.jpg",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSuP9f8pNQSX2XvWjTj3_NlQzCnwnNbteqTCQ&s",
        "https://media-cdn.tripadvisor.com/media/photo-s/09/25/3b/2e/national-aquarium.jpg",
        "https://nuestroshijos.do/wp-content/uploads/2016/10/parquetematico1_500.jpg",
        "https://i0.wp.com/pedritopuntacana.com/wp-content/uploads/2017/01/acuario-5.jpg?w=537&h=360&ssl=1",
        "https://www.ferriesdelcaribe.com/img/explorador/detail/FDC-Wishlist-Fotos-Hr-2-RD-3-Acuario-Nacional.jpg",
    ]

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
        align="center"
)
    
def star_rating() -> rx.Component:
    """Componente para mostrar estrellas de rating."""
    return rx.hstack(
        rx.foreach(
            range(5),
            lambda i: rx.cond(
                i < 4,  # 4 estrellas llenas para 4.1
                rx.icon("star", fill="orange", color="orange", size=16),
                rx.icon("star", color="gray", size=16)
            )
        ),
        spacing="1"
    )

def property_header() -> rx.Component:
    """Header con título, rating y acciones."""
    return rx.vstack(
        rx.hstack(
            star_rating(),
            rx.text(
                PropertyState.rating,
                font_weight="bold",
                color="orange"
            ),
            spacing="2"
        ),
        rx.hstack(
            rx.heading(
                PropertyState.title,
                size="6",
                font_weight="bold"
            ),
            rx.spacer(),
            rx.hstack(
                rx.button(
                    rx.icon("heart", size=20),
                    variant="ghost",
                    color_scheme="gray"
                ),
                rx.button(
                    rx.icon("share", size=20),
                    variant="ghost", 
                    color_scheme="gray",
                    margin_right ="20px"
                ),
                rx.button(
                    "Reserva ahora",
                    color_scheme="blue",
                    size="3"
                ),
                spacing="2"
            ),
            width="100%"
        ),
        rx.hstack(
            rx.icon("map-pin", size=16, color="gray"),
            rx.text(
                PropertyState.location,
                color="gray",
                size="2"
            ),
            rx.text(
                " - ",
                color="gray"
            ),
            rx.text(
                PropertyState.location_quality,
                color="blue",
                size="2",
                text_decoration="underline"
            ),
            rx.text(
                " · ",
                color="gray"
            ),
            rx.text(
                "Ver mapa",
                color="blue",
                size="2",
                text_decoration="underline"
            ),
            spacing="1",
            align="center"
        ),
        spacing="3",
        width="100%"
    )

def image_gallery() -> rx.Component:
    """Galería de imágenes de la propiedad."""
    return rx.hstack(
        # Imagen principal grande
        rx.box(
            rx.image(
                src=PropertyState.main_image,
                width="100%",
                height="300px",
                object_fit="cover",
                border_radius="8px"
            ),
            width="80%"
        ),
        # Grid de imágenes pequeñas
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.image(
                        src=PropertyState.images[0],
                        width="100%",
                        height="145px",
                        object_fit="cover",
                        border_radius="8px"
                    ),
                    width="70%"
                ),
                rx.box(
                    rx.image(
                        src=PropertyState.images[1],
                        width="100%",
                        height="145px",
                        object_fit="cover",
                        border_radius="8px"
                    ),
                    width="70%"
                ),
                spacing="2",
                width="100%"
            ),
            rx.hstack(
                rx.box(
                    rx.image(
                        src=PropertyState.images[2],
                        width="100%",
                        height="145px",
                        object_fit="cover",
                        border_radius="8px"
                    ),
                    width="45%"
                ),
                rx.box(
                    rx.image(
                        src=PropertyState.images[3],
                        width="100%",
                        height="145px",
                        object_fit="cover",
                        border_radius="8px"
                    ),
                    width="45%"
                ),
                rx.box(
                    rx.image(
                        src=PropertyState.images[4],
                        width="100%",
                        height="145px",
                        object_fit="cover",
                        border_radius="8px"
                    ),
                    width="45%"
                ),
                rx.box(
                    rx.box(
                        rx.image(
                            src=PropertyState.images[5],
                            width="100%",
                            height="145px",
                            object_fit="cover",
                            border_radius="8px"
                        ),
                        position="relative"
                    ),
                    width="45%"
                ),
                spacing="2",
                width="100%"
            ),
            spacing="2",
            width="38%"
        ),
        spacing="4",
        width="100%"
    )

def reviews_section() -> rx.Component:
    """Sección de reseñas y comentarios."""
    return rx.vstack(
        # Rating y comentarios
        rx.hstack(
            rx.text(
                "Muy Bonito",
                font_weight="bold",
                font_size="18px"
            ),
            rx.spacer(),
            rx.box(
                rx.text(
                    PropertyState.map_score,
                    color="white",
                    font_weight="bold",
                    font_size="16px",
                    background ="#3F7BFD",
                    padding = "4px",
                    border_radius = "10px"
                ),
                bg="blue.500",
                px="3",
                py="1",
                border_radius="4px"
            ),
            width="100%"
        ),
        rx.text(
            rx.text.span(PropertyState.reviews),
            rx.text.span(" comentarios"),
            color="gray.600",
            size="3"
        ),
        rx.text(
            "Opiniones de los visitantes",
            font_weight="bold",
            size="3",
            margin_top="4"
        ),
        rx.box(
            rx.text(
                rx.text.span('"'),
                rx.text.span(PropertyState.guest_review),
                rx.text.span('"'),
                font_style="italic",
                color="gray.600",
                size="3"
            ),
            bg="gray.50",
            p="3",
            border_radius="8px",
            border_left="4px solid",
            border_color="blue.500"
        ),
        rx.hstack(
            rx.box(
                rx.image(
                    src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmCfrDHAps3hamCP6CGJAYnDEI9QGwUb-vuQ&s",
                    border_radius ="100px"
                ),
                bg="blue.500",
                width="32px",
                height="32px",
                border_radius="50%",
                display="flex",
                align_items="center",
                justify_content="center"
            ),
            rx.vstack(
                rx.text(
                    PropertyState.guest_name,
                    font_weight="bold",
                    size="2"
                ),
                rx.hstack(
                    rx.text(
                        "🇨🇴",
                        font_size="14px"
                    ),
                    rx.text(
                        PropertyState.guest_country,
                        size="2",
                        color="gray.600"
                    ),
                    spacing="1"
                ),
                spacing="0"
            ),
            spacing="2",
            align="center"
        ),
        # Sección Personal
        rx.hstack(
            rx.text(
                "Personal",
                font_weight="bold"
            ),
            rx.spacer(),
            rx.box(
                rx.text(
                    PropertyState.personal_rating,
                    color="white",
                    font_weight="bold",
                    background ="#3F7BFD",
                    padding = "4px",
                    border_radius = "10px"
                ),
                bg="blue.500",
                px="2",
                py="1",
                border_radius="4px"
            ),
            width="100%",
            margin_top="4"
        ),
        spacing="3",
        width="100%",
        align="start",
        background = "#2C3949",
        padding = "15px",
        border_radius="8px",
        border="1px solid",
    )

def hotel_description() -> rx.Component:
    """Sección de descripción del hotel."""
    return rx.vstack(
        rx.text(
            PropertyState.description,
            size="3",
            line_height="1.6",
            color="gray.700"
        ),
        rx.text(
            PropertyState.room_description,
            size="3",
            line_height="1.6",
            color="gray.700",
            margin_top="3"
        ),
        rx.text(
            PropertyState.breakfast_info,
            size="3",
            line_height="1.6",
            color="gray.700",
            margin_top="3"
        ),
        rx.text(
            PropertyState.location_info,
            size="3",
            line_height="1.6",
            color="gray.700",
            margin_top="3"
        ),
        rx.text(
            "Las distancias en la descripción del alojamiento se calculan con OpenStreetMaps®",
            size="1",
            color="gray.500",
            font_style="italic",
            margin_top="3"
        ),
        spacing="0",
        width="100%",
        align="start"
    )

def services_section() -> rx.Component:
    """Sección de servicios más populares."""
    return rx.vstack(
        rx.heading(
            "Servicios más populares",
            size="4",
            font_weight="bold",
            color="gray.800"
        ),
        rx.hstack(
            # Primera fila de servicios
            rx.hstack(
                rx.icon("waves", size=16, color="teal"),
                rx.text("Vistas hacia el mar", size="2"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("alarm-clock", size=16, color="teal"),
                rx.text("Abierto fines de semana", size="2"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("battery-full", size=16, color="teal"),
                rx.text("Cargadores disponibles", size="2"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("bed", size=16, color="teal"),
                rx.text("Hoteles Cercanos", size="2"),
                spacing="2",
                align="center"
            ),
            spacing="6",
            wrap="wrap"
        ),
        rx.hstack(
            # Segunda fila de servicios
            rx.hstack(
                rx.icon("wifi", size=16, color="teal"),
                rx.text("WiFi gratis", size="2"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("clock", size=16, color="teal"),
                rx.text("Recepción 12 horas todos los dias", size="2"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("glass-water", size=16, color="teal"),
                rx.text("Bebida Disponible", size="2"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("coffee", size=16, color="teal"),
                rx.text("Comida Disponible", size="2"),
                spacing="2",
                align="center"
            ),
            spacing="6",
            wrap="wrap"
        ),
        spacing="4",
        width="100%",
        align="start"
    )

def amenities_sidebar() -> rx.Component:
    """Sidebar con puntos fuertes del alojamiento."""
    return rx.vstack(
        rx.heading(
            "Recursos utilizables durante la visita",
            size="4",
            font_weight="bold",
            color="gray.800",
            margin_bottom="4"
        ),
        
        # Desayuno disponible
        rx.hstack(
            rx.icon("coffee", size=20, color="gray.600"),
            rx.vstack(
                rx.text(
                    "Comida y bebida",
                    font_weight="bold",
                    size="3"
                ),
                rx.text(
                    "Cosas para quitar el hambre durante la visita",
                    size="2",
                    color="gray.600"
                ),
                spacing="0",
                align="start"
            ),
            spacing="3",
            align="start",
            width="100%"
        ),
        
        # WiFi gratis
        rx.hstack(
            rx.icon("wifi", size=20, color="gray.600"),
            rx.vstack(
                rx.text(
                    "WiFi gratis",
                    font_weight="bold",
                    size="3"
                ),
                rx.text(
                    "Internet y buena covertura",
                    size="2",
                    color="gray.600"
                ),
                spacing="0",
                align="start"
            ),
            spacing="3",
            align="start",
            width="100%"
        ),
        
        # Ideal para familias
        rx.hstack(
            rx.icon("users", size=20, color="gray.600"),
            rx.vstack(
                rx.text(
                    "Ideal para familias",
                    font_weight="bold",
                    size="3"
                ),
                rx.text(
                    "Experiencia muy entretenida para familias",
                    size="2",
                    color="gray.600",
                    line_height="1.4"
                ),
                spacing="0",
                align="start"
            ),
            spacing="3",
            align="start",
            width="100%"
        ),
        
        # Vistas
        rx.hstack(
            rx.icon("eye", size=20, color="gray.600"),
            rx.vstack(
                rx.text(
                    "Vistas",
                    font_weight="bold",
                    size="3"
                ),
                rx.text(
                    "Vistas al mar, ademas de un tunel muy inmersivo en la experiencia",
                    size="2",
                    color="gray.600"
                ),
                spacing="0",
                align="start"
            ),
            spacing="3",
            align="start",
            width="100%"
        ),
        
        # Servicio de traslado

        # Botones de acción
        rx.vstack(
            rx.button(
                "Reserva ahora",
                color_scheme="blue",
                size="3",
                width="100%"
            ),
            rx.button(
                rx.hstack(
                    rx.icon("heart", size=16),
                    rx.text("Guardar el alojamiento"),
                    spacing="2"
                ),
                variant="outline",
                color_scheme="blue",
                size="3",
                width="100%"
            ),
            spacing="2",
            margin_top="6"
        ),
        
        spacing="4",
        width="100%",
        align="start",
        bg="gray.50",
        p="4",
        border_radius="8px",
        border="1px solid",
        border_color="gray.200",
        padding = "20px",
        background = "#2C3949"
    )

def map_section() -> rx.Component:
    """Sección del mapa de Google."""
    return rx.vstack(
        rx.box(
            rx.html(
                """
                <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d61511.03237178954!2d-69.9644938!3d18.4861!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8eaf89f0c4f5c7f5%3A0x1c69e7b88e4b9c5e!2sZona%20Colonial%2C%20Santo%20Domingo%2C%20Rep%C3%BAblica%20Dominicana!5e0!3m2!1ses!2sdo!4v1638360000000!5m2!1ses!2sdo"
                    width="100%" 
                    height="250" 
                    style="border:0; border-radius:8px;" 
                    allowfullscreen="" 
                    loading="lazy" 
                    referrerpolicy="no-referrer-when-downgrade">
                </iframe>
                """,
                width="100%",
                height="250px"
            ),
            width="100%"
        ),
        rx.button(
            "Ver en el mapa",
            color_scheme="blue",
            size="2",
            width="100%",
            margin_top="2"
        ),
        spacing="2",
        width="100%"
    )



def main_content() -> rx.Component:
    """Contenido principal con toda la información del hotel."""
    return rx.hstack(
        rx.vstack(
            image_gallery(),
            hotel_description(),
            services_section(),
            spacing="6",
            width="65%"
        ),
        rx.vstack(
            reviews_section(),
            map_section(),
            amenities_sidebar(),
            spacing="4",
            width="35%"
        ),
        spacing="8",
        width="100%",
        align="start"
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

def index() -> rx.Component:
    """Página principal con el listado de propiedad."""
    return navbar(), rx.container(
        rx.vstack(
            property_header(),
            main_content(),
            spacing="6",
            width="100%",
            margin_bottom = "80px"
        ),
        px="4",
        py="6",
        background = "#091F31",
    ), footer()



app = rx.App()
app.add_page(index)
