class FileRepositoryInterface:
    """
    Reads data from .csv formatted file on init
    Over-Writes data to file
    Use os.path.normpath ( from os.path import normpath )
        to use paths that are valid in Windows, Linux and Mac OS
    """

    def read_all(self):
        """
        Read data from file
        To be called on init
        :return:
        """
        pass

    def save_all(self):
        """
        Over-Write saved data to file
        :return:
        """
        pass

    def create(self, value):
        """
        Save Value In Memory
        :param value:
        :return:
        """
        pass

    def update(self, value):
        """
        Update previous value with new value
        :param value:
        :return:
        """
        pass

    def delete(self, value):
        """
        Remove
        :param value:
        :return:
        """
        pass
