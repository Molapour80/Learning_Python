product ={}
def add():
    code = input("Enter your code:").isnumeric()
    name = input("product:")
    price = float(input("price:"))
    if code  in product:
        print(f"this code is product{code}")
    else:
        product[code] ={"name":name , "price":price}
        return code , name , price

def display():
    if not product:
        print("No products available.")
        return
    for code, details in product.items():
        print(f"Code: {code}, Name: {details['name']}, Price: {details['price']}")

def delete(code): 
    if code  not in product: 
        print("Not found!!!")
    else:
        product.pop(code)
        return product      

def edit(code):
    if code  not in product:
        return "not found"
    name =input("name product:") or product[code]["name"]
    price = float(input("price")) or product[code]["price"]
    product[code] = {"name ":name , "price":price}
    if name:
        product[code]["name"] = name
    if price:
        product[code]["price"] = float(price)

    print(f"Product with code {code} updated.")


def search_code(code):
    if code in product:
        return product[code]["name"], product[code]["price"]
    else:
        print("Product not found.")
        return None, None
def search_name(name):
    for code, details in product.items():
        if details["name"].lower() == name.lower():
            return code, details["price"]
    print("Product not found.")
    return None, None

def ditails_total():
    for product in product.values():
        total = sum(product['price'])
        print(f"total:{len(product)} , total_price:{total}")




Help  ='''

    1.add:insert to product
    2.display:show the product
    3.delete:clear the list
    4.edit:remove the product
    5.search:found the product in list
    6.ditails:show
    7.help
    8.Exit
'''






def main():
    setup = '''
1.add
2.display
3.delete
4.edit
5.search
6.ditails
7.help
8.Exit
'''
    print(setup)
    while True:

        function = input("choose the function: ").strip().lower()
        if function in "help":
            print(Help)
        elif function in "1":
            add()
        elif function in "2":
            display()
        elif function in "3":
            code= input("code:").isnumeric()
            delete(code)
        elif function in "4":
            code = input("code:")
            edit(code)
        elif function in "5":
            choose = input("code or name ")
            if choose in code:
                code = input("code")
                name ,price = search_code(code)
                if name and price:
                    print(f"Found: {name}, Price: {price}")

            elif choose in name:
                name =input("name:")
                code, price = search_name(name)
                if code and price:
                    print(f"Found: Code: {code}, Price: {price}")

                search_name(name)
        elif function in "6":
            ditails_total()
        elif function in "8":
            break
        else:
            print("Try ahain:))")
    
main()


 