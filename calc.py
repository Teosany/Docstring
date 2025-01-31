from decimal import Decimal, InvalidOperation

def get_number(prompt: str) -> Decimal:
    while True:
        try:
            return Decimal(input(prompt))
        except (ValueError, InvalidOperation):
            print("Veuillez entrer un nombre valide.")


def calculate_sum() -> None:
    first_number = get_number("Entrez un premier nombre : ")
    second_number = get_number("Entrez un deuxième nombre : ")

    result = first_number + second_number
    print(f"Le résultat de l'addition de {first_number:g} avec {second_number:g} est égal à {result:g}")


if __name__ == "__main__":
    calculate_sum()