from abc import ABC, abstractmethod


class Institution(ABC):

    @abstractmethod
    def create_user(self, ): pass

    @abstractmethod
    def create_group(self, ): pass

    @abstractmethod
    def insert_user_in_group(self, ): pass

    @abstractmethod
    def remove_of_group(self, ): pass
