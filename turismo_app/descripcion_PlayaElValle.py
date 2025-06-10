
import reflex as rx
from typing import List, Dict

class PropertyState(rx.State):
    """Estado para manejar la información de la propiedad."""
    
    # Variables de estado reactivas
    title: str = "Playa El Valle"
    rating: float = 4.2
    reviews: int = 493
    location: str = "Playa El Valle, América del Norte Samana, República Dominicana"
    location_quality: str = "Hermosa Ubicación"
    map_score: float = 8.5
    guest_review: str = "Playa hermosa para relajarse y disfrutar."
    guest_name: str = "Taliana"
    guest_country: str = "Uruguay"
    personal_rating: float = 8.1

    description: str = "Playa El Valle es una playa aislada situada entre montañas al norte de Samaná. De difícil acceso pero con un encanto único, su entorno natural combina selva, ríos y mar en un solo lugar. Es frecuentada por viajeros que buscan experiencias auténticas lejos del turismo masivo. "
    room_description: str = "En las cercanías hay alojamientos ecológicos y se pueden hacer caminatas hacia miradores y cascadas. Es perfecta para desconectar y disfrutar de un ambiente rústico y natural."
    breakfast_info: str = ""
    location_info: str = ""
    
    main_image: str = "https://elvallelodge.com/wp-content/uploads/2023/11/El-secreto-de-la-playa-del-valle.jpg"
    images: List[str] = [
        "https://samanainn.com/uploads/0000/157/2024/08/26/2.png",
        "https://images.visitarepublicadominicana.org/playa-el-valle-samana.jpg",
        "https://elvallelodge.com/wp-content/uploads/2022/08/Por-que-el-valle-samana.jpg",
        "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/1a/e4/df/5f/playa-ermitano.jpg?w=900&h=500&s=1",
        "https://dgcine.gob.do/locaciones/wp-content/uploads/2024/10/Playa-el-Valle.jpg",
        "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/27/19/17/18/caption.jpg?w=1200&h=-1&s=1",
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
            range(4),
            lambda i: rx.cond(
                i < 5, 
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
                "Precioso lugar",
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
            "Lo que más gusta a quienes se alojan aquí:",
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
                    src="https://e00-xlk-ue-marca.uecdn.es/uploads/2025/03/21/16893424870615.png",
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
                rx.icon("Dog", size=16, color="teal"),
                rx.text("Se Permiten Mascotas", size="2"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("fish", size=16, color="teal"),
                rx.text("Distintas Especies de Peces", size="2"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("tent-tree", size=16, color="teal"),
                rx.text("Se permite acampar en algunas areas", size="2"),
                spacing="2",
                align="center"
            ),
            spacing="6",
            wrap="wrap"
        ),
    )

def amenities_sidebar() -> rx.Component:
    """Sidebar con puntos fuertes del alojamiento."""
    return rx.vstack(
        rx.heading(
            "Puntos fuertes del alojamiento",
            size="4",
            font_weight="bold",
            color="gray.800",
            margin_bottom="4"
        ),
        
        # WiFi gratis
        rx.hstack(
            rx.icon("wifi", size=20, color="gray.600"),
            rx.vstack(
                rx.text(
                    "Convertura Disponible",
                    font_weight="bold",
                    size="3"
                ),
                rx.text(
                    "4G y 5G disponibles",
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
                    "Ideal para familias y grupos grandes",
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
            rx.icon("cigarette", size=20, color="gray.600"),
            rx.vstack(
                rx.text(
                    "Zona de fumadores",
                    font_weight="bold",
                    size="3"
                ),
                rx.text(
                    "Lugar para fumar al aire libre",
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
