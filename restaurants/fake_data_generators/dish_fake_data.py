from restaurants.models import Dish

dishes = [
    {
        "name": "Lomo Saltado",
        "description": "Plato elaborado con lomo fino, cebolla, tomate y papas fritas. Sazonado con especias peruanas.",
        "price": 5000,
        "type": "MAIN_COURSE",
    },
    {
        "name": "Ceviche",
        "description": "Pescado fresco marinado en limón con cebolla morada, ají y cilantro. Servido con camote y maíz.",
        "price": 4500,
        "type": "APPETIZER",
    },
    {
        "name": "Pisco Sour",
        "description": "Cóctel peruano a base de pisco, limón, jarabe de goma y clara de huevo. Servido con una pizca de canela.",
        "price": 2500,
        "type": "BEVERAGE",
    },
    {
        "name": "Arroz con Mariscos",
        "description": "Arroz cocido con mariscos frescos, pimientos, cebolla y achiote. Acompañado de salsa de mariscos.",
        "price": 5200,
        "type": "MAIN_COURSE",
    },
    {
        "name": "Mazamorra Morada",
        "description": "Postre tradicional peruano a base de maíz morado cocido con frutas y especias. Servido con arroz con leche.",
        "price": 2200,
        "type": "DESSERT",
    },
    {
        "name": "Anticuchos",
        "description": "Brochetas de corazón de res marinadas en ají panca y comino. Acompañadas de papas y choclo.",
        "price": 3800,
        "type": "APPETIZER",
    },
    {
        "name": "Chicha Morada",
        "description": "Bebida refrescante hecha con maíz morado, piña, canela y clavo de olor. Endulzada con azúcar.",
        "price": 2100,
        "type": "BEVERAGE",
    },
    {
        "name": "Causa Limeña",
        "description": "Pastel de papa amarilla relleno de pollo, atún o camarones. Aderezado con ají amarillo y mayonesa.",
        "price": 4600,
        "type": "APPETIZER",
    },
    {
        "name": "Inca Kola",
        "description": "Bebida gaseosa peruana de sabor dulce y color amarillo. Acompaña perfectamente la comida criolla.",
        "price": 1800,
        "type": "BEVERAGE",
    },
    {
        "name": "Tres Leches",
        "description": "Pastel esponjoso empapado en tres tipos de leche (condensada, evaporada y crema). Decorado con merengue.",
        "price": 2400,
        "type": "DESSERT",
    },
]


def generate_dishes():
    for dish in dishes:
        dish_created, created = Dish.objects.get_or_create(
            name=dish.get("name"),
            description=dish.get("description"),
            price=dish.get("price"),
            type=dish.get("type"),
        )

        print(f'{dish.get("name")} was added') if created else print(
            f"{dish.get('name')} wasn't added"
        )
