print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

""")
# Start loop
menu_items = {}

while True:

    order = input('> ')
    if order == 'quit':
        break

    if order not in menu_items:
        menu_items[order] = 1
        report = f"** {menu_items[order]} order of {order} have been added to your meal **"
        print(report)
    else:
        menu_items[order] += 1
        report = f"** {menu_items[order]} orders of {order} have been added to your meal **"
        print(report)
