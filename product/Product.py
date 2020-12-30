class Product:
    '''Class that contains a Product Name, its locations and their keywords, and users to contact'''
    def __init__(self, name, urls, contacts):
        self.name = name
        self.urls = urls
        self.contacts = contacts