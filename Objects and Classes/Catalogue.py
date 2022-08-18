class Catalogue:
    products = []

    def __init__(self, name):
        self.name = name

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        current_word_list = []
        for i in self.products:
            if first_letter in i:
                current_word_list.append(i)
        return current_word_list

    def __repr__(self):
        result = f"Items in the {self.name} catalogue:\n"
        result += '\n'.join(sorted(self.products))
        return result


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
