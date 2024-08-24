class Book:
    def _init_(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price

    # Getter and setter properties for instance variables
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    # Method to calculate royalty
    def royalty(self, copies_sold):
        if copies_sold <= 500:
            return 0.10 * self._price * copies_sold
        elif 500 < copies_sold <= 1500:
            return 0.125 * self._price * copies_sold
        else:
            return 0.15 * self._price * copies_sold

class Ebook(Book):
    def _init_(self, title, author, publisher, price, ebook_format):
        super()._init_(title, author, publisher, price)
        self._ebook_format = ebook_format

    # Getter and setter property for ebook format
    @property
    def ebook_format(self):
        return self._ebook_format

    @ebook_format.setter
    def ebook_format(self, value):
        self._ebook_format = value

    # Override royalty method to deduct GST for ebooks
    def royalty(self, copies_sold):
        royalty_amount = super().royalty(copies_sold)
        gst_deduction = 0.12 * royalty_amount
        return royalty_amount - gst_deduction

# Example usage
if _name_ == "_main_":
    physical_book = Book("Python Programming", "John Doe", "Tech Books", 25.99)
    print(f"Royalty for 800 copies of physical book: ${physical_book.royalty(800):.2f}")

    ebook = Ebook("Python Ebooks", "Jane Smith", "Ebook Publishers", 19.99, "EPUB")
    print(f"Royalty for 1200 copies of ebook: ${ebook.royalty(1200):.2f}")