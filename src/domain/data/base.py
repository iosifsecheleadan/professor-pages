class DataException(Exception):
    pass


class DataEntity:
    """
    Base Data Entity Class
    """

    def __init__(self, identifier: int):
        self.__identification = identifier

    @staticmethod  # abstract
    def from_csv(csv_string: str):
        """
        Return new Data Entity from csv formatted string
        :param csv_string:
        :return:
        """
        pass

    def to_csv(self) -> str:
        """
        Return csv representation
        :return:
        """
        pass

    def get_id(self) -> int:
        """
        Return Object ID
        Used for equality check
        :return:
        """
        return self.__identification

    # abstract
    def to_html(self) -> str:
        """
        Return HTML representation
        :return:
        """
        pass

    # abstract
    def __str__(self) -> str:
        """
        Return pretty print string representation
        :return:
        """
        pass

    def __eq__(self, other: object) -> bool:
        """
        Check equality by id
        :param other:
        :return:
        """
        if isinstance(other, DataEntity):
            return other.get_id() == self.get_id()
        return False
