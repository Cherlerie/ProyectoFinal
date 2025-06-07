import reflex as rx
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

def hotel_card():
    return rx.card(
        rx.hstack(
            # Imagen principal
            rx.image(
                src="https://plus.unsplash.com/premium_photo-1669748157617-a3a83cc8ea23?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cGxheWElMjBkZSUyMGhhd2FpfGVufDB8fDB8fHww",
                alt="Habitación del hotel",
                width="200px",
                height="200px",
                object_fit="cover",
                border_radius="8px 0 0 8px"
            ),
            
            # Galería de imágenes pequeñas
            rx.vstack(
                rx.image(
                    src="https://upload.wikimedia.org/wikipedia/commons/9/96/Barbados_beach.jpg",
                    alt="Vista 1",
                    width="80px",
                    height="60px",
                    object_fit="cover",
                    border_radius="4px"
                ),
                rx.image(
                    src="https://upload.wikimedia.org/wikipedia/commons/9/96/Barbados_beach.jpg",
                    alt="Vista 2",
                    width="80px",
                    height="60px",
                    object_fit="cover",
                    border_radius="4px"
                ),
                rx.image(
                    src="https://upload.wikimedia.org/wikipedia/commons/9/96/Barbados_beach.jpg",
                    alt="Vista 3",
                    width="80px",
                    height="60px",
                    object_fit="cover",
                    border_radius="4px"
                ),
                spacing="2",
                margin_left="8px"
            ),
            
            rx.vstack(
                rx.hstack(
                    rx.badge(
                        rx.text("8,8", font_weight="bold", color="white"),
                        background="#2563eb",
                        px="3",
                        py="1",
                        border_radius="4px"
                    ),
                    rx.vstack(
                        rx.text("Fabuloso", font_weight="bold", size="2"),
                        rx.text("3.260 comentarios", size="1", color="gray.600"),
                        spacing="0",
                        align="start"
                    ),
                    spacing="3",
                ),
                
                rx.heading(
                    "Aparthotel Stare Miasto",
                    size="5",
                    font_weight="bold",
                    margin_top="2"
                ),
                
                rx.hstack(
                    rx.hstack(
                        rx.icon("utensils", size=16, color="orange.500"),
                        rx.text("Tiene 1 restaurante", size="2"),
                        spacing="1"
                    ),
                    rx.hstack(
                        rx.icon("car", size=16, color="gray.600"),
                        rx.text("Aparcamiento", size="2"),
                        spacing="1"
                    ),
                    spacing="4"
                ),
                
                rx.hstack(
                    rx.icon("map-pin", size=16, color="blue.500"),
                    rx.text(
                        "Golebia 2, Centro histórico, 31-007 Cracovia, Polonia – En el centro de la ciudad",
                        size="2",
                        color="gray.700"
                    ),
                    spacing="1",
                    align="start"
                ),
                
                rx.box(
                    rx.text(
                        "Este alojamiento tiene una ubicación excelente. ¡Los clientes le han dado una puntuación de 9,8!",
                        size="2",
                        color="green.700",
                        font_weight="medium"
                    ),
                    background="#5867ED",
                    border_radius="6px",
                    padding="3",
                    margin_top="3",
                    margin_right = "15px"
                ),
                
                align="start",
                spacing="2",
                flex="1",
                padding_left="4",
                margin_left = "20px"
            ),
            
            align="start",
            spacing="0",
            width="100%"
        ),
        
        background="#3F546E",
        border="1px solid #e2e8f0",
        border_radius="8px",
        box_shadow="0 2px 8px rgba(0,0,0,0.1)",
        padding="0",
        overflow="hidden",
        max_width="900px",
        width="100%"
    )

def reservation_sidebar():
    return rx.vstack(
        rx.box(
            rx.heading("Los datos de tu reserva", size="4", color="gray.700", margin_bottom="4"),
            
            rx.vstack(
                rx.vstack(
                    rx.text("Entrada:", font_weight="bold", size="2"),
                    rx.text("sábado, ", color="gray.700", size="2", display="inline"),
                    rx.text("14 de junio", font_weight="bold", color="blue.600", size="2", display="inline"),
                    rx.text(" de 2025 desde las 15:00", color="gray.700", size="2", display="inline"),
                    spacing="1",
                    align="start"
                ),
                
                rx.vstack(
                    rx.text("Salida:", font_weight="bold", size="2"),
                    rx.text("domingo, ", color="blue.600", size="2", display="inline"),
                    rx.text("15 de junio", font_weight="bold", color="blue.600", size="2", display="inline"),
                    rx.text(" de 2025 hasta las 11:00", color="gray.700", size="2", display="inline"),
                    spacing="1",
                    align="start"
                ),
                
                rx.vstack(
                    rx.text("Duración total de la estancia:", font_weight="bold", size="2"),
                    rx.text("1 noche", color="gray.700", size="2"),
                    spacing="1",
                    align="start"
                ),
                
                spacing="4",
                align="start",
                width="100%"
            ),
            
            background="#091F31",
            border="1px solid #e2e8f0",
            border_radius="8px",
            padding="15px",
            margin_bottom="4",
            width = "320px"
        ),
        
        rx.box(
            rx.heading("Desglose del precio", size="4", color="gray.700", margin_bottom="4"),
            
            rx.vstack(
                rx.hstack(
                    rx.text("Estudio Superior Deluxe", size="2"),
                    rx.text("DOP 12.760,70", font_weight="bold", size="2"),
                    justify="between",
                    width="100%"
                ),
                
                rx.vstack(
                    rx.hstack(
                        rx.text("Precio", font_weight="bold", size="2"),
                        rx.text("DOP 12.760,70", font_weight="bold", size="2"),
                        justify="between",
                        width="100%"
                    ),
                    rx.text("(tu moneda)", color="gray.500", size="1", align="left"),
                    spacing="0",
                    align="start",
                    width="100%"
                ),
                
                rx.vstack(
                    rx.hstack(
                        rx.text("En la moneda del colaborador", size="2"),
                        rx.text("USD216.1", font_weight="bold", size="2"),
                        justify="between",
                        width="100%"
                    ),
                    rx.text("(incl. total clientes)", color="gray.500", size="1", align="left"),
                    spacing="0",
                    align="start",
                    width="100%"
                ),
                
                spacing="3",
                width="100%"
            ),
            
            rx.text("Incluye impuestos y cargos", size="1", color="gray.600", margin_top="3"),
            rx.text(
                "Pagarás en USD. El tipo de cambio puede variar antes de que pagues. Ten en cuenta que la entidad emisora de tu tarjeta puede aplicar cargos por transacción internacional.",
                size="1",
                color="gray.600",
                margin_top="2"
            ),
            
            background="#091F31",
            border="1px solid #e2e8f0",
            border_radius="8px",
            padding="15px",
            margin_bottom="4",
            margin_top = "20px"
        ),
        
        rx.box(
            rx.heading("¿Cuánto cuesta cancelar?", size="4", color="gray.700", margin_bottom="4"),
            
            rx.vstack(
                rx.text(
                    "Cancelación gratis hasta las 23:59 del 11 de junio de 2025",
                    color="green.600",
                    font_weight="medium",
                    size="2"
                ),
                rx.text(
                    "A partir de las 00:00 del 12 de junio DOP 12.761 de 2025",
                    color="gray.700",
                    size="2"
                ),
                spacing="2",
                align="start"
            ),
            
            margin_top = "20px",
            background="#091F31",
            border="1px solid #e2e8f0",
            border_radius="8px",
            padding="15px"
        ),
        
        spacing="0",
        width="320px",
        align="start"
    )
    
def contact_form():
    return rx.container(
        rx.vstack(
            rx.hstack(
                rx.text("¡Ya casi estás! Solo tienes que rellenar los campos marcados con ", 
                color="green", size="3"),
                rx.text("*", color="red", size="3"),
                justify="center"
            ),
            
            rx.vstack(
                rx.text("¿Viajas por trabajo?", font_weight="bold", size="3"),
                rx.radio_group(
                    ["Sí", "No"],
                    default_value="No",
                    direction="row",
                    spacing="3"
                ),
                align_items="start",
                spacing="2"
            ),
            
            rx.hstack(
                rx.vstack(
                    rx.text("Tratamiento", font_weight="bold", size="3"),
                    rx.select(
                        ["Sr.", "Sra.", "Dr.", "Dra."],
                        placeholder="Seleccionar...",
                        width="100%"
                    ),
                    width="30%",
                    align_items="start"
                ),
                
                rx.vstack(
                    rx.hstack(
                        rx.text("Nombre", font_weight="bold", size="3"),
                        rx.text("*", color="red", size="3")
                    ),
                    rx.input(
                        placeholder="Nombre",
                        width="100%"
                    ),
                    width="35%",
                    align_items="start"
                ),
                
                rx.vstack(
                    rx.hstack(
                        rx.text("Apellido", font_weight="bold", size="3"),
                        rx.text("*", color="red", size="3")
                    ),
                    rx.input(
                        placeholder="Apellido",
                        width="100%"
                    ),
                    width="35%",
                    align_items="start"
                ),
                
                spacing="4",
                width="100%"
            ),
            
            rx.vstack(
                rx.hstack(
                    rx.text("E-mail", font_weight="bold", size="3"),
                    rx.text("*", color="red", size="3")
                ),
                rx.input(
                    placeholder="Asegúrate de que no haya errores",
                    type="email",
                    width="100%"
                ),
                align_items="start",
                spacing="2"
            ),
            
            rx.vstack(
                rx.hstack(
                    rx.text("Confirmar dirección de e-mail", font_weight="bold", size="3"),
                    rx.text("*", color="red", size="3")
                ),
                rx.input(
                    placeholder="Confirmar e-mail",
                    type="email",
                    width="100%"
                ),
                align_items="start",
                spacing="2"
            ),
            
            rx.vstack(
                rx.hstack(
                    rx.text("Teléfono (móvil, si es posible)", font_weight="bold", size="3"),
                    rx.text("*", color="red", size="3")
                ),
                rx.hstack(
                    rx.select(
                        ["+1", "+34", "+52", "+57", "+58", "+593", "+1-809"],
                        default_value="+1",
                        width="100px"
                    ),
                    rx.input(
                        placeholder="Número de teléfono",
                        type="tel",
                        flex="1"
                    ),
                    spacing="2",
                    width="100%"
                ),
                align_items="start",
                spacing="2"
            ),
            rx.button(
                "Confirmar",
                color_scheme="blue",
                size="4",
                border_radius="full",
                _hover={"transform": "scale(1.05)"},
                padding_x="2em",
            ),
            
            spacing="4",
            align_items="stretch"
        ),
        width = "900px",
        margin="4",
        padding="50px",
        background="#2C3949", 
        border_radius="8px",
        box_shadow="0 2px 10px rgba(0,0,0,0.1)"
    )

def index():
    return rx.box(
        navbar(),
        rx.box(
            rx.hstack(
                reservation_sidebar(),
                rx.vstack(
                    hotel_card(),
                    contact_form(),
                    flex="1",
                    align="start"
                ),
                
                
                
                spacing="8",
                align="start",
                width="100%",
                max_width="1200px"
            ),
            
            padding="8",
            min_height="100vh",
            display="flex",
            justify_content="center",
            margin_top="70px"
        ),
        background="#091F31",
        min_height="100vh",
    )

app = rx.App()
app.add_page(index)