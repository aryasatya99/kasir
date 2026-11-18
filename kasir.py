menu = {
    "Fried Chiken": 20000,
    "frien fries": 15000,
    "Double Cheese Burger": 40000,
    "Hot Coca-cola": 10000,
    "Ice coffe": 12000,
}

print("==================DAFTAR MENU==================")
for item, price in menu.items():
    print("DAFTAR MENU:", item, "\tPrice:", price)
print("Pembelian di atas Rp100.000,- mendapatkan 15%")
print("===============================================")

order_input = input("Pesanan (format: Nama Menu jumlah, ...): ")
orders = []
for order in order_input.split(","):
    parts = order.strip().rsplit(maxsplit=1)
    if len(parts) != 2 or not parts[1].isdigit():
        print("Format pesanan tidak valid. Gunakan: Nama Menu jumlah.")
        raise SystemExit(1)

    item = next(
        (name for name in menu if name.casefold() == parts[0].casefold()),
        None,
    )
    quantity = int(parts[1])
    if item is None or quantity < 1:
        print("Nama menu tidak dikenal atau jumlah harus lebih dari 0.")
        raise SystemExit(1)
    orders.append((item, quantity))

price = sum(quantity * menu[item] for item, quantity in orders)

if price > 100000:
    discount = price * 15 / 100
else:
    discount = 0

total = price - discount

print("==================DETAIL PEMBELIAN==================")
for item, quantity in orders:
    print(f"{item} x {quantity}: {quantity * menu[item]}")
print("Total Price:", price)
print("Diskon:", discount)
print("Total ALL:", total)