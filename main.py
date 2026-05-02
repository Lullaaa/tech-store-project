class Store:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = price
        print(f"\n✔ {name} added with price ${price}")

    def remove_product(self, name):
        if name not in self.products:
            print("❌ Product not found")
            return False
        del self.products[name]
        print(f"✔ {name} removed")
        return True

    def list_products(self):
        print("\n" + "="*40)
        print(f"        {self.name} PRODUCTS")
        print("="*40)

        if not self.products:
            print("No products available")
            return

        for i, (p, price) in enumerate(self.products.items(), 1):
            print(f"{i}. {p:<15} - ${price}")
        print("="*40)


class Employee:
    def __init__(self, name, store, password):
        self.name = name
        self.store = store
        self.password = password

    def login(self):
        print("\n🔐 Employee Login")
        while True:
            attempt = input("Enter password: ")
            if attempt == self.password:
                print(f"✔ Welcome {self.name}")
                return True
            else:
                print("❌ Wrong password. Try again.")

    def menu(self):
        while True:
            print("\n" + "-"*30)
            print("EMPLOYEE MENU")
            print("-"*30)
            print("1. Add product")
            print("2. Remove product")
            print("3. View products")
            print("4. Exit")

            choice = input("Choose: ")

            if choice == "1":
                name = input("Product name: ")

                while True:
                    price = input("Price: ")
                    if price.isdigit():
                        price = int(price)
                        break
                    print("❌ Enter a valid number")

                self.store.add_product(name, price)

            elif choice == "2":
                while True:
                    name = input("Product to remove: ")
                    if self.store.remove_product(name):
                        break
                    print("Try again")

            elif choice == "3":
                self.store.list_products()

            elif choice == "4":
                break

            else:
                print("❌ Invalid choice")


class Cart:
    def __init__(self, store):
        self.store = store
        self.cart = {}

    def add(self):
        while True:
            name = input("Enter product name to add: ")

            if name in self.store.products:
                self.cart[name] = self.store.products[name]
                print(f"✔ {name} added to cart")
                break
            else:
                print("❌ Product not found. Try again.")

    def remove(self):
        while True:
            name = input("Enter product name to remove: ")

            if name in self.cart:
                del self.cart[name]
                print(f"✔ {name} removed from cart")
                break
            else:
                print("❌ Not in cart. Try again.")

    def view(self):
        print("\n" + "="*30)
        print("YOUR CART")
        print("="*30)

        if not self.cart:
            print("Cart is empty")
            return

        for i, (p, price) in enumerate(self.cart.items(), 1):
            print(f"{i}. {p:<15} - ${price}")

        print("-"*30)
        print(f"TOTAL: ${self.total()}")
        print("="*30)

    def total(self):
        return sum(self.cart.values())

    def checkout(self):
        if not self.cart:
            print("Cart is empty")
            return

        self.view()
        confirm = input("Confirm payment? (y/n): ")

        if confirm.lower() == "y":
            print("✔ Payment successful!")
            self.cart.clear()
        else:
            print("❌ Payment cancelled")


def customer_menu(store):
    cart = Cart(store)

    while True:
        print("\n" + "-"*30)
        print("CUSTOMER MENU")
        print("-"*30)
        print("1. View products")
        print("2. Add to cart")
        print("3. Remove from cart")
        print("4. View cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            store.list_products()

        elif choice == "2":
            cart.add()

        elif choice == "3":
            cart.remove()

        elif choice == "4":
            cart.view()

        elif choice == "5":
            cart.checkout()

        elif choice == "6":
            break

        else:
            print("❌ Invalid choice")


def main():
    store = Store("Tech Store")

    # preloaded employee (you can change this later)
    employee = Employee("Admin", store, "1234")

    print("="*40)
    print("WELCOME TO TECH STORE SYSTEM")
    print("="*40)

    while True:
        print("\n1. Employee Login")
        print("2. Customer")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            if employee.login():
                employee.menu()

        elif choice == "2":
            customer_menu(store)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid option")


if __name__ == "__main__":
    main()