class catalogue():
    def __init__(self):
        hat1 = fashion_item(34, 1, "White", "Hat", "Hat1.jpeg")
        hat2 = fashion_item(35, 1, "Black", "Hat", "Hat2.jpeg")
        hat3 = fashion_item(36, 1, "Black", "Hat", "Hat3.jpeg")

        jeans1 = fashion_item(23, 'M', "Grey", "Jeans", "Jeans1.jpeg")
        jeans2 = fashion_item(24, 'M', "Navy", "Jeans", "Jeans2.jpeg")
        jeans3 = fashion_item(25, 'M', "Silver", "Jeans", "Jeans3.jpeg")
        jeans4 = fashion_item(26, 'M', "Light Blue", "Jeans", "Jeans4.jpeg")

        shoes1 = fashion_item(67, 9, "White", "Shoes", "Shoes1.jpeg")
        shoes2 = fashion_item(67, 9, "Black", "Shoes", "Shoes2.jpeg")
        shoes3 = fashion_item(67, 9, "Checkered", "Shoes", "Shoes3.jpeg")

        tshirt1 = fashion_item(72, 'S', "Brown", "Tshirt", "Tshirt1.jpeg")
        tshirt2 = fashion_item(73, 'S', "Grey", "Tshirt", "Tshirt2.jpeg")
        tshirt3 = fashion_item(74, 'S', "Brown", "Tshirt", "Tshirt3.jpeg")

        self.hat_items = [hat1, hat2, hat3]
        self.jean_items = [jeans1, jeans2, jeans3, jeans4]
        self.shoe_items = [shoes1, shoes2, shoes3]
        self.tshirt_items = [tshirt1, tshirt2, tshirt3]

    def get_hat_IDs(self):
        results = []
        for hat in self.hat_items:
            results.append(hat.ID)
        return (results)


class fashion_item():
    def __init__(self, ID, size, colour, category, filename):
        self.size = size
        self.colour = colour
        self.category = category
        self.ID = ID
        self.filename = filename
