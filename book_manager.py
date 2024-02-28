class Book:
  def __init__(self, isbn, title, author):
    self.isbn = isbn
    self.title = title
    self.author = author

  def __eq__(self, other):
    if not isinstance(other, Book):
        return NotImplemented
    return self.isbn == other.isbn

  def __repr__(self):
    return f"Book({self.isbn}, '{self.title}', '{self.author}')"
