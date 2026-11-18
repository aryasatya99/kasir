# Simple Cashier Program

A terminal-based cashier program built with Python. Users can order multiple menu items at once, and the total price is calculated automatically, including any discount.

## Features

- Displays the menu list and prices
- Order multiple items in a single input
- Menu names are case-insensitive
- 15% discount for purchases over Rp100,000
- Order input validation

## Requirements

- Python 3.6 or newer

## Getting Started

1. Clone this repository:
   ```
   git clone https://github.com/aryasatya99/kasir.git
   cd kasir
   ```
2. Run the program:
   ```
   python3 kasir.py
   ```

## Usage

Enter your order in the format `Menu Name quantity`, separated by commas.

Input:

```
Order (format: Menu Name quantity, ...): fried chicken 2, hot coca-cola 1
```

Output:

```
==================PURCHASE DETAILS==================
Fried Chicken x 2: 40000
Hot Coca-cola x 1: 10000
Total Price: 50000
Discount: 0
Total: 50000
```

## Menu

| Item | Price |
|------|-------|
| Fried Chicken | Rp20,000 |
| French Fries | Rp15,000 |
| Double Cheese Burger | Rp40,000 |
| Hot Coca-cola | Rp10,000 |
| Ice Coffee | Rp12,000 |

## Roadmap

- [ ] Payment and change calculation
- [ ] Repeat orders without restarting the program
- [ ] Save receipts to a file

## Author

[aryasatya99](https://github.com/aryasatya99)
