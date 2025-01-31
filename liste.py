from typing import List

def display_menu() -> str:
    menu = """Choisissez parmi les 5 options suivantes: 
1: Ajouter un élement à la liste
2: Retirer un élement de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter"""
    print(menu)
    return input("👉 Votre choix : ")


def show_items(items: List[str]) -> None:
    if not items:
        print("La liste est vide.")
    else:
        print(f"Voici le contenu de votre liste : ")
        for i, item in enumerate(items, 1):
            print(f"{i}. {item}")


def main() -> None:
    items: List[str] = []

    while True:
        choice = display_menu()

        match choice:
            case "1":
                item = input("Entrez le nom d'un élement à ajouter à la liste : ")
                items.append(item)
                print(f"L'élément {item} a bien été ajouté à la liste.")
            case "2":
                if not items:
                    print("La liste est vide.")
                else:
                    item = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
                    try:
                        items.remove(item)
                        print(f"L'élément {item} a bien été supprimé de la liste.")
                    except ValueError:
                        print(f"L'élément {item} n'est pas dans la liste.")
            case "3":
                show_items(items)
            case "4":
                if not items:
                    print("La liste est vide.")
                else:
                    items.clear()
                    print("La liste a été vidée de son contenu.")
            case "5":
                return
            case _:
                print("Option invalide.")

        print("---")


if __name__ == "__main__":
    main()
