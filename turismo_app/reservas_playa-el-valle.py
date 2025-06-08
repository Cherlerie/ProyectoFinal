import reflex as rx
from typing import List, Dict

class PropertyState(rx.State):
    """Estado para manejar la información de Playas El Valle."""
    
    # Variables de estado reactivas
    title: str = "Playas El Valle Experience"
    rating: float = 4.8
    reviews: int = 342
    location: str = "Playa El Valle, Península de Samaná, República Dominicana"
    location_quality: str = "Ubicación espectacular"
    map_score: float = 9.2
    guest_review: str = "Playa increíble, naturaleza virgen y formaciones rocosas únicas. Una experiencia inolvidable"
    guest_name: str = "María Elena"
    guest_country: str = "España"
    personal_rating: float = 9.5
    
    description: str = "Playas El Valle Experience te ofrece la oportunidad de descubrir uno de los tesoros más vírgenes de República Dominicana. Ubicada en la península de Samaná, esta playa se caracteriza por sus impresionantes formaciones rocosas, acantilados dramáticos y aguas cristalinas. Un destino perfecto para los amantes de la naturaleza y la aventura que buscan escapar de las multitudes."
    activities_description: str = "La playa ofrece excelentes condiciones para el surf, especialmente para principiantes e intermedios. También puedes disfrutar de caminatas por los senderos naturales, explorar las formaciones rocosas únicas, hacer camping bajo las estrellas y nadar tanto en el mar como en el río cercano. Las puestas de sol desde los acantilados son simplemente espectaculares."
    nature_info: str = "El entorno está rodeado de exuberante vegetación tropical y montañas que crean un paisaje de película. La playa se mantiene en estado casi virgen, lo que la convierte en un santuario natural donde puedes desconectarte completamente y conectar con la naturaleza."
    access_info: str = "El acceso requiere una caminata de aproximadamente 20 minutos por un sendero natural desde el pueblo de El Valle. Se recomienda llevar agua, protector solar y calzado adecuado. El Aeropuerto Internacional El Catey de Samaná está a 45 minutos en vehículo."
    
    main_image: str = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&h=600&fit=crop"
    images: List[str] = [
        "https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1520637836862-4d197d17c92a?w=400&h=300&fit=crop",
        "https://images.unsplash.com/photo-1501594907352-04cda38ebc29?w=200&h=150&fit=crop",
        "https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=200&h=150&fit=crop",
        "https://images.unsplash.com/photo-1544551763-77ef2d0cfc6c?w=200&h=150&fit=crop",
        "https://images.unsplash.com/photo-1505142468610-359e7d316be0?w=200&h=150&fit=crop",
    ]

def navbar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.heading("SamanáExperience", size="6", color="white"),
            flex="1",
        ),
        
        rx.center(
            rx.hstack(
                rx.link("Inicio", href="/", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
                rx.link("Destinos", href="#", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
                rx.link("Actividades", href="#", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
                rx.link("Contacto", href="#", color="white", padding_x="1em", _hover={"opacity": "0.8"}),
                spacing="0",
            ),
            width="100%",
            position="absolute",
            left="50%",
            transform="translateX(-50%)",
        ),
        
        rx.box(
            rx.button(
                "Explorar",
                color_scheme="teal",
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
                i < 5,  # 5 estrellas llenas para 4.8
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
                font_weight="bold",
                color="white"
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
                    "Visitar ahora",
                    color_scheme="teal",
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
                color="teal",
                size="2",
                text_decoration="underline"
            ),
            rx.text(
                " · ",
                color="gray"
            ),
            rx.text(
                "Ver ubicación",
                color="teal",
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
    """Galería de imágenes de la playa."""
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
                "Excepcional",
                font_weight="bold",
                font_size="18px",
                color="white"
            ),
            rx.spacer(),
            rx.box(
                rx.text(
                    PropertyState.map_score,
                    color="white",
                    font_weight="bold",
                    font_size="16px",
                    background ="#14B8A6",
                    padding = "4px",
                    border_radius = "10px"
                ),
                bg="teal.500",
                px="3",
                py="1",
                border_radius="4px"
            ),
            width="100%"
        ),
        rx.text(
            rx.text.span(PropertyState.reviews),
            rx.text.span(" reseñas de visitantes"),
            color="gray.400",
            size="3"
        ),
        rx.text(
            "Lo que más aman los visitantes:",
            font_weight="bold",
            size="3",
            margin_top="4",
            color="white"
        ),
        rx.box(
            rx.text(
                rx.text.span('"'),
                rx.text.span(PropertyState.guest_review),
                rx.text.span('"'),
                font_style="italic",
                color="gray.300",
                size="3"
            ),
            bg="rgba(20, 184, 166, 0.1)",
            p="3",
            border_radius="8px",
            border_left="4px solid",
            border_color="teal.500"
        ),
        rx.hstack(
            rx.box(
                rx.image(
                    src="https://images.unsplash.com/photo-1494790108755-2616b612b494?w=32&h=32&fit=crop&crop=face",
                    border_radius ="100px",
                    width="32px",
                    height="32px"
                ),
                bg="teal.500",
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
                    size="2",
                    color="white"
                ),
                rx.hstack(
                    rx.text(
                        "🇪🇸",
                        font_size="14px"
                    ),
                    rx.text(
                        PropertyState.guest_country,
                        size="2",
                        color="gray.400"
                    ),
                    spacing="1"
                ),
                spacing="0"
            ),
            spacing="2",
            align="center"
        ),
        # Sección Naturaleza
        rx.hstack(
            rx.text(
                "Naturaleza",
                font_weight="bold",
                color="white"
            ),
            rx.spacer(),
            rx.box(
                rx.text(
                    PropertyState.personal_rating,
                    color="white",
                    font_weight="bold",
                    background ="#14B8A6",
                    padding = "4px",
                    border_radius = "10px"
                ),
                bg="teal.500",
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

def beach_description() -> rx.Component:
    """Sección de descripción de la playa."""
    return rx.vstack(
        rx.text(
            PropertyState.description,
            size="3",
            line_height="1.6",
            color="gray.300"
        ),
        rx.text(
            PropertyState.activities_description,
            size="3",
            line_height="1.6",
            color="gray.300",
            margin_top="3"
        ),
        rx.text(
            PropertyState.nature_info,
            size="3",
            line_height="1.6",
            color="gray.300",
            margin_top="3"
        ),
        rx.text(
            PropertyState.access_info,
            size="3",
            line_height="1.6",
            color="gray.300",
            margin_top="3"
        ),
        rx.text(
            "Información basada en datos de visitantes y guías locales especializados",
            size="1",
            color="gray.500",
            font_style="italic",
            margin_top="3"
        ),
        spacing="0",
        width="100%",
        align="start"
    )

def activities_section() -> rx.Component:
    """Sección de actividades disponibles."""
    return rx.vstack(
        rx.heading(
            "Actividades Disponibles",
            size="4",
            font_weight="bold",
            color="white"
        ),
        rx.hstack(
            # Primera fila de actividades
            rx.hstack(
                rx.icon("waves", size=16, color="teal"),
                rx.text("Surf", size="2", color="gray.300"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("mountain", size=16, color="teal"),
                rx.text("Senderismo", size="2", color="gray.300"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("tent", size=16, color="teal"),
                rx.text("Camping", size="2", color="gray.300"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("camera", size=16, color="teal"),
                rx.text("Fotografía", size="2", color="gray.300"),
                spacing="2",
                align="center"
            ),
            spacing="6",
            wrap="wrap"
        ),
        rx.hstack(
            # Segunda fila de actividades
            rx.hstack(
                rx.icon("sun", size=16, color="teal"),
                rx.text("Avistamiento de atardeceres", size="2", color="gray.300"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("fish", size=16, color="teal"),
                rx.text("Natación", size="2", color="gray.300"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("tree-palm", size=16, color="teal"),
                rx.text("Exploración natural", size="2", color="gray.300"),
                spacing="2",
                align="center"
            ),
            rx.hstack(
                rx.icon("compass", size=16, color="teal"),
                rx.text("Aventura", size="2", color="gray.300"),
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

def highlights_sidebar() -> rx.Component:
    """Sidebar con aspectos destacados de la playa."""
    return rx.vstack(
        rx.heading(
            "Aspectos Destacados",
            size="4",
            font_weight="bold",
            color="white",
            margin_bottom="4"
        ),
        
        # Formaciones rocosas
        rx.hstack(
            rx.icon("mountain", size=20, color="teal"),
            rx.vstack(
                rx.text(
                    "Formaciones Rocosas Únicas",
                    font_weight="bold",
                    size="3",
                    color="white"
                ),
                rx.text(
                    "Acantilados dramáticos y rocas esculpidas naturalmente",
                    size="2",
                    color="gray.400"
                ),
                spacing="0",
                align="start"
            ),
            spacing="3",
            align="start",
            width="100%"
        ),
        
        # Naturaleza virgen
        rx.hstack(
            rx.icon("tree-pine", size=20, color="teal"),
            rx.vstack(
                rx.text(
                    "Naturaleza Virgen",
                    font_weight="bold",
                    size="3",
                    color="white"
                ),
                rx.text(
                    "Playa casi intacta rodeada de vegetación exuberante",
                    size="2",
                    color="gray.400"
                ),
                spacing="0",
                align="start"
            ),
            spacing="3",
            align="start",
            width="100%"
        ),
        
        # Ideal para aventureros
        rx.hstack(
            rx.icon("backpack", size=20, color="teal"),
            rx.vstack(
                rx.text(
                    "Perfecto para Aventureros",
                    font_weight="bold",
                    size="3",
                    color="white"
                ),
                rx.text(
                    "Surf, camping, senderismo y exploración. Múltiples actividades al aire libre",
                    size="2",
                    color="gray.400",
                    line_height="1.4"
                ),
                spacing="0",
                align="start"
            ),
            spacing="3",
            align="start",
            width="100%"
        ),
        
        # Vistas espectaculares
        rx.hstack(
            rx.icon("sunset", size=20, color="teal"),
            rx.vstack(
                rx.text(
                    "Vistas Espectaculares",
                    font_weight="bold",
                    size="3",
                    color="white"
                ),
                rx.text(
                    "Atardeceres inolvidables desde los acantilados. Vistas panorámicas del océano",
                    size="2",
                    color="gray.400"
                ),
                spacing="0",
                align="start"
            ),
            spacing="3",
            align="start",
            width="100%"
        ),
        
        # Acceso único
        rx.hstack(
            rx.icon("footprints", size=20, color="teal"),
            rx.vstack(
                rx.text(
                    "Experiencia Auténtica",
                    font_weight="bold",
                    size="3",
                    color="white"
                ),
                rx.text(
                    "Caminata de acceso. Alejado de multitudes. Conexión pura con la naturaleza",
                    size="2",
                    color="gray.400"
                ),
                spacing="0",
                align="start"
            ),
            spacing="3",
            align="start",
            width="100%"
        ),
        
        # Botones de acción
        rx.vstack(
            rx.button(
                "Planificar Visita",
                color_scheme="teal",
                size="3",
                width="100%"
            ),
            rx.button(
                rx.hstack(
                    rx.icon("bookmark", size=16),
                    rx.text("Guardar Destino"),
                    spacing="2"
                ),
                variant="outline",
                color_scheme="teal",
                size="3",
                width="100%"
            ),
            spacing="2",
            margin_top="6"
        ),
        
        spacing="4",
        width="100%",
        align="start",
        bg="rgba(44, 57, 73, 0.8)",
        p="4",
        border_radius="8px",
        border="1px solid",
        border_color="teal.500",
        padding = "20px"
    )

def map_section() -> rx.Component:
    """Sección del mapa de ubicación."""
    return rx.vstack(
        rx.box(
            rx.html(
                """
                <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3743.8234567890123!2d-69.3456789!3d19.2345678!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8ea1234567890abc%3A0x1234567890abcdef!2sPlaya%20El%20Valle%2C%20Saman%C3%A1%2C%20Rep%C3%BAblica%20Dominicana!5e0!3m2!1ses!2sdo!4v1638360000000!5m2!1ses!2sdo"
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
            "Ver Ubicación Completa",
            color_scheme="teal",
            size="2",
            width="100%",
            margin_top="2"
        ),
        spacing="2",
        width="100%"
    )

def main_content() -> rx.Component:
    """Contenido principal con toda la información de la playa."""
    return rx.hstack(
        rx.vstack(
            image_gallery(),
            beach_description(),
            activities_section(),
            spacing="6",
            width="65%"
        ),
        rx.vstack(
            reviews_section(),
            map_section(),
            highlights_sidebar(),
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
        footer_item("Playa El Valle", "/#"),
        footer_item("Las Terrenas", "/#"),
        footer_item("Cayo Levantado", "/#"),
        footer_item("Salto El Limón", "/#"),
        footer_item("Playa Rincón", "/#"),
        spacing="4",
        text_align=["center", "center", "start"],
        flex_direction="column",
    )

def footer_items_activities() -> rx.Component:
    return rx.flex(
        rx.heading(
            "ACTIVIDADES", size="4", weight="bold", as_="h3", color="white"
        ),
        footer_item("Surf", "/#"),
        footer_item("Senderismo", "/#"),
        footer_item("Camping", "/#"),
        footer_item("Avistamiento de Ballenas", "/#"),
        footer_item("Tours Naturales", "/#"),
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
        footer_item("Guías Locales", "/#"),
        footer_item("Testimonios", "/#"),
        footer_item("Blog Naturaleza", "/#"),
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
                                "SamanáExperience",
                                size="7",
                                weight="bold",
                                color="white",
                            ),
                            align_items="center",
                        ),
                        rx.text(
                            "Descubre la belleza natural auténtica de la Península de Samaná",
                            size="3",
                            color="rgba(255, 255, 255, 0.7)",
                            text_align=["center", "center", "start"],
                            max_width="250px",
                            line_height="1.5",
                        ),
                        rx.text(
                            "© 2024 SamanáExperience. Todos los derechos reservados.",
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
                    footer_items_activities(),
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
    """Página principal con información de Playas El Valle."""
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