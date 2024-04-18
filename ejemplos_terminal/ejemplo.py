def mostrar(fecha: str) -> None:
    if fecha == "18-12-2022":
        print("Argentina campeon!")
    else:
        print("No es una fecha importante")

def main() -> None:
    fecha: str = "01-01-2025"
    mostrar(fecha)

main()
