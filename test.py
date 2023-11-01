from colorama import init, Fore, Back, Style

def imprimir_ticket(fecha, numeros, jacks, total, id_ticket, codigo_extra):
    init(autoreset=True)  # Inicializar colorama y resetear automáticamente los estilos después de cada print

    # Representación simplificada del código de barras en ASCII
    barcode = """
|||   ||  ||| | ||  || |||  ||| |
|||   ||  ||| | ||  || |||  ||| |
|||   ||  ||| | ||  || |||  ||| |
"""

    # Crear contenido del ticket
    lines = [
        "Loto Plus",
        "Participa Desquite o Sale",
        "Participa Sale o Sale",
        "SORTEO 3158 del 12/01/2019",
        "(Apuesta Automática)",
        "Calidad ISO RI 9000-438",
        "MONYO, IRMA SUSANA",
        "MZ 71 PC 14",
        "MARGARITA BELEN",
        fecha,
        '   '.join(numeros),
        f"JACKS  {jacks[0]} - {jacks[1]}",
        f"TOTAL:             $ {total:.2f}",
        f"ID TICKET: {id_ticket}",
        codigo_extra,
    ]

    max_width = max(len(line) for line in lines)
    border = "+" + "-" * max_width + "+"
    separator = "|" + " " * max_width + "|"

    # Imprimir ticket con un estilo creativo
    print(Back.WHITE + Fore.BLACK + border)
    for line in lines:
        centered_line = line.center(max_width)
        print(Back.WHITE + Fore.BLACK + "|" + Fore.GREEN + Style.BRIGHT + centered_line + Back.WHITE + Fore.BLACK + "|")
        print(Back.WHITE + Fore.BLACK + separator)
    for bar_line in barcode.strip().split('\n'):
        print(Back.WHITE + Fore.BLACK + "|" + Fore.BLUE + Style.BRIGHT + bar_line.center(max_width) + Back.WHITE + Fore.BLACK + "|")
    print(Back.WHITE + Fore.BLACK + border)

# Ejemplo de uso
fecha = "11/01/2019 15:52:09"
numeros = ["02", "11", "19", "22", "24", "40"]
jacks = ["7", "8"]
total = 40.00
id_ticket = "171 006 514 045 002 358/0272"
codigo_extra = "AB0000001-0167003-10140191-1568-0115"
imprimir_ticket(fecha, numeros, jacks, total, id_ticket, codigo_extra)
