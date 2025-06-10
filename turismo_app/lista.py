import reflex as rx
from typing import List

class Lugar (rx.Base):
    nombre: str
    ubicacion: str
    distancia_centro: str
    descripcion: str
    calificacion: float
    num_comentarios: int
    precio: str
    servicios: List[str]
    path: str

Lugares = [
   Lugar(
    nombre="Acuario Nacional",
    ubicacion="Santo Domingo Este, Avenida España",
    distancia_centro="1,3 km del centro",
    descripcion="Visitar el Acuario Nacional es una excelente opción para toda la familia: combina entretenimiento, descubrimiento y aprendizaje sobre la biodiversidad marina en un entorno accesible y bien ubicado.",
    calificacion=9.7,
    num_comentarios=41,
    precio="Desde $60",
    servicios=["Wifi gratis", "Tienda de recuerdos", "Cafetería"],
    path = "/imagenes/acuario.jpeg"
),

Lugar(
    nombre="Parque Colón",
    ubicacion="Ciudad Colonial, Santo Domingo",
    distancia_centro="1,4 km del centro",
    descripcion="Un icónico espacio histórico en el corazón de la Ciudad Colonial, rodeado de arquitectura colonial y vida cultural.",
    calificacion=8.9,
    num_comentarios=23,
    precio="Gratis",
    servicios=["Guías turísticos", "Zonas para fotos", "Restaurantes cercanos"],
    path = "/imagenes/colon.jpeg"
),

Lugar(
    nombre="Teleférico de Puerto Plata",
    ubicacion="Puerto Plata",
    distancia_centro="3 km del centro",
    descripcion="Único teleférico del Caribe que te lleva hasta la cima de la Loma Isabel de Torres con vistas impresionantes.",
    calificacion=9.5,
    num_comentarios=58,
    precio="Desde $150",
    servicios=["Wifi gratis", "Mirador", "Tiendas de souvenirs"],
    path = "/imagenes/teleferico.jpg"
),

Lugar(
    nombre="Los Tres Ojos",
    ubicacion="Santo Domingo Este",
    distancia_centro="4 km del centro",
    descripcion="Parque nacional subterráneo con tres lagunas de agua cristalina dentro de cavernas naturales.",
    calificacion=9.1,
    num_comentarios=67,
    precio="Desde $100",
    servicios=["Visitas guiadas", "Áreas de descanso", "Estacionamiento"],
    path = "/imagenes/parque3ojos.jpg"
),

Lugar(
    nombre="Salto El Limón",
    ubicacion="Samaná",
    distancia_centro="7 km de El Limón",
    descripcion="Una impresionante cascada en medio de la selva tropical, accesible por senderismo o paseo a caballo.",
    calificacion=9.6,
    num_comentarios=80,
    precio="Desde $200 (con guía)",
    servicios=["Guías locales", "Puestos de comida", "Zonas de baño"],
    path = "/imagenes/saltoellimon.jpg"
),

Lugar(
    nombre="Bahía de las Águilas",
    ubicacion="Pedernales",
    distancia_centro="aprox. 30 km de Pedernales",
    descripcion="Playa virgen considerada una de las más bellas del Caribe, dentro del Parque Nacional Jaragua.",
    calificacion=9.8,
    num_comentarios=92,
    precio="Acceso libre (excursiones desde $500)",
    servicios=["Excursiones en bote", "Zona protegida", "Observación de fauna"],
    path = "/imagenes/bahiaaguilas.jpg"
)

]

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
        bg="#2C3949",
        border_radius="8px",
        box_shadow="4",
        position="absolute",
        margin_top="-3em",
        top="68%",  
        left="50%",
        transform="translateX(-50%)",
        z_index="5",
    )

def tarjeta_Lugares(Lugares: Lugar) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.box(
                rx.image(
                    src={Lugares.path},  
                    width="200px",
                    height="150px",
                    object_fit="cover",
                    border_radius="8px",
                ),
                flex="none",
            ),
            rx.vstack(
                rx.heading(Lugares.nombre, size="5"),
                rx.text(Lugares.ubicacion, color="gray"),
                rx.text(Lugares.distancia_centro, color="gray", size="2"),
                rx.text(Lugares.descripcion, size="2", margin_top="0.5em"),
                
                rx.hstack(
                    *[rx.badge(servicio, variant="soft") for servicio in Lugares.servicios],
                    spacing="2",
                    margin_top="0.5em",
                ),
                
                align_items="flex-start",
                spacing="1",
                flex="1",
                padding_left="1em",
            ),
            rx.vstack(
                rx.hstack(
                    rx.badge(
                        f"Excepcional {Lugares.calificacion}",
                        color_scheme="green",
                    ),
                    rx.text(f"{Lugares.num_comentarios} comentarios", size="1"),
                    spacing="2",
                ),
                rx.spacer(),
                rx.vstack(
                    rx.text(Lugares.precio, size="4", font_weight="bold"),
                    rx.button(
                        "Ver disponibilidad",
                        color_scheme="blue",
                        size="2",
                    ),
                    align_items="flex-end",
                ),
                height="100%",
                align_items="flex-end",
                spacing="3",
            ),
            spacing="4",
            align_items="flex-start",
        ),
        padding="1.5em",
        bg="#3F546E",
        border_radius="8px",
        box_shadow="sm",
        width="100%",
        margin_bottom="1em",
        _hover={
            "box_shadow": "md",
            "transform": "translateY(-2px)",
            "transition": "all 0.3s ease",
        },
    )

def filtros_laterales() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.heading("Filtrar por:", size="4"),
            rx.divider(),
            
            rx.vstack(
                rx.heading("Filtros populares", size="5", margin_bottom="0.5em"),
                rx.checkbox("Aire acondicionado (45)"),
                rx.checkbox("4 estrellas (147)"),
                rx.checkbox("Zona Colonial (110)"),
                rx.checkbox("Piscina privada (84)"),
                rx.checkbox("Hoteles (123)"),
                rx.checkbox("Villas (6)"),
                rx.checkbox("Piscina (189)"),
                rx.checkbox("Fantásticos 9+ (111)"),
                spacing="2",
                align_items="flex-start",
            ),
            
            width="250px",
            padding="1em",
            bg="#2C3949",
            border_radius="8px",
            box_shadow="sm",
            position="sticky",
            top="6em",
        )
    )

def resultados_busqueda() -> rx.Component:
    return rx.box(
        rx.heading("Santo Domingo: 6 paquetes encontrados", size="5", margin_bottom="1em"),
        rx.vstack(
            *[tarjeta_Lugares(Lugares) for Lugares in Lugares],
            spacing="3",
        ),
        flex="1",
        padding_left="2em",
    )

def lista() -> rx.Component:
    return rx.box(
        navbar(),
        
        rx.box(
            rx.box(
                compact_filter(),
                height="300px",
                width="100%",
                background_image="url('o.png')",  
                background_size="cover",
                background_position="center",
                position="relative",
            ),
            margin_bottom="5em",
        ),
        
        rx.flex(
            filtros_laterales(),
            resultados_busqueda(),
            padding_x="5%",
            padding_top="2em",
            spacing="4",
        ),
        
        width="100%",
        background = "#091F31"
    )

