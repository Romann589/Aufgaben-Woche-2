import customer
from logger import log_error, log_debug
from pathlib import Path


def add_new_customer(name: str, age: int) -> customer.Customer:
    return customer.Customer(name, age)


def print_customer_info(customer: customer.Customer) -> None:
    print(f"Name: {customer.name}, Age: {customer.age}")


def save_customer_to_txt(customer: customer.Customer) -> None:
    file_path = Path(__file__).parent / "customers.txt"

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"Name: {customer.name}, Age: {customer.age}\n")


def validate_name(name: str) -> str:
    if not name.isalpha():
        log_error(f"Ungültiger Name eingegeben: {name}")
        raise ValueError("Der Name darf nur Buchstaben enthalten.")
    return name


def validate_age(age_input: str) -> int:
    if not age_input.isdigit():
        log_error(f"Ungültiges Alter eingegeben: {age_input}")
        raise ValueError("Das Alter muss eine ganze Zahl sein.")
    return int(age_input)


def new_customer_input() -> customer.Customer:
    while True:
        try:
            name = validate_name(input("Enter your name: "))
            break
        except ValueError as error:
            print(f"Error: {error}")

    while True:
        try:
            age = validate_age(input("Enter your age: "))
            break
        except ValueError as error:
            print(f"Error: {error}")

    return add_new_customer(name, age)


def main() -> None:
    log_debug("Programm gestartet.")

    log_debug("Neuer Customer wird eingegeben.")
    customer = new_customer_input()

    log_debug("Customer wird in customers.txt gespeichert.")
    save_customer_to_txt(customer)

    log_debug("Customer wird im Terminal ausgegeben.")
    print_customer_info(customer)

    log_debug("Programm beendet.")


if __name__ == "__main__":
    main()