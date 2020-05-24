"""
Lista ogłoszeń
​
Napisz programy, w których tworzysz listę ogłoszeń samochodowych, a następnie wyszukujesz ogłoszenia na podstawie ich parametrów.
​
Na przykład ogłoszenia o cenach z określonego przedziału.
​
Użyj funkcji `lambda`, określających, które ogłoszenia powinny zostać wyszukane.
Użyj poznanych kolekcji do trzymania ogłoszeń. Możesz zastosować metodę `filter` do wyszukiwania odpowiednich ogłoszeń.
"""



class Notice:

    def __init__(self, category: int, title: str, description: str, price: float, seller_name: str, seller_phone: str, address: str):
        """
        making class which will create and display notice
        """
        self.category = category
        self.title = title
        self.description = description
        self.price = price
        self.seller_name = seller_name
        self.seller_phone = seller_phone
        self.address = address

    def __str__(self) -> str:
        return self.display_notice()


    def display_notice(self) -> str:
        """
        This method prints one notice
        :return: string with notice
        """
        return f' Category: {self.category}\n' \
               f' Title: {self.title}\n' \
               f' Description: {self.description}\n' \
               f' Seller: {self.seller_name}\n' \
               f' Address: {self.address}\n' \
               f' Seller phone: {self.seller_phone}\n' \
               f' Price: {self.price}'


class NoticeBoard:
    def __init__(self):
        self.items = []


    def add_notice_to_board(self, notice: dict) -> list:
        """
        This method add notice to the notice board
        :return: dictionary with notice
        """
        if not isinstance(notice, Notice):
            raise TypeError("Notice has to be an instance of class Notice")
        else:
            self.items.append(notice)

    def display_board(self) -> str:
        print("Local notice board: ")
        for self.notice in self.items:
            print(f'{self.notice}\n')

    def __str__(self):
        return self.display_board()

'''
class FilteredBoard:
    """
    class for filtered notices
    """
    def __init__(self, criteria_filter: str, condition_filter):
        self.criteria_filter = criteria_filter
        self.condition_filter = condition_filter
        self.filtered_board = []

    def __str__(self):
        return self.filtered_board()

    def display_filtered_board(self) -> str:
        print("Search result: ")
        for self.filtered_notice in self.filtered_board:
            print(f'{self.filtered_notice}\n')


    def filter_board(self, board: list) -> list:
        if not isinstance(board, NoticeBoard):
            raise TypeError("Board has to be an instance of class NoticeBoard")

        for self.element in self.board:
            self.filtered_board = list(filter(lambda element: element[self.criteria_filter] in self.condition_filter, self.board))
'''



board1 = NoticeBoard()

n1 = Notice(1, 'Rower', 'Bardzo dobry rower', 2000.0, 'Jan Nowak', '111 222 333', 'Pcim Sredni')

n2 = Notice(2, 'Kawa', 'niedobra kawa', 20.0, 'Janina Jakas', '123 456 798', 'Wroclaw')

n3 = Notice(1, 'Sanki', 'Szybkie sanki', 120.0, 'Zdzislaw Bardzowolny', '987 654 321', 'Sniegobraki')

board1.add_notice_to_board(n1)
board1.add_notice_to_board(n2)
board1.add_notice_to_board(n3)


board1.display_board()
print()
print(board1.items)

'''
fboard1 = FilteredBoard()

fboard1.filter_board()
'''