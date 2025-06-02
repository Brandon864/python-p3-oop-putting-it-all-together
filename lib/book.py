# lib/book.py

class Book:
    def __init__(self, title, page_count):
        """Initialize a Book with title and page_count."""
        self._title = title
        self._page_count = page_count  # Use setter for validation

    # Getter for title
    def get_title(self):
        return self._title

    # Setter for title
    def set_title(self, title):
        if not isinstance(title, str) or not title:
            raise ValueError("Title must be a non-empty string")
        self._title = title

    # Property for title
    title = property(get_title, set_title)

    # Getter for page_count
    def get_page_count(self):
        return self._page_count

    # Setter for page_count
    def set_page_count(self, page_count):
        if not isinstance(page_count, int):
            print("page_count must be an integer")
            return
        if page_count <= 0:
            raise ValueError("Page count must be a positive integer")
        self._page_count = page_count

    # Property for page_count
    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        """Simulate turning a page."""
        print("Flipping the page...wow, you read fast!")