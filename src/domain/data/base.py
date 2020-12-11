class DataEntity:
    """
    Base Data Entity Class
    """

    def __init__(self, id: int):
        self.__identification = id

    def get_id(self) -> int:
        """
        Return Object ID
        Used for equality check
        :return:
        """
        return self.__identification

    def to_html(self) -> str:
        """
        Return HTML representation
        :return:
        """
        pass

    def __str__(self):
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


