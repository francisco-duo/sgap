from abc import ABC, abstractmethod

from src.app.institution import Institution
from src.app.categories import BasicEducation, TechnicalEducation, SuperiorEducation


class InstitutionFactory(ABC):

    def __init__(self, institution: str) -> None:
        self.institution = self.select_institution(institution)

    @staticmethod
    @abstractmethod
    def select_institution(institution: str) -> Institution: pass

    def create_user(self, ): self.institution.create_user()

    def create_group(self, ): self.institution.create_group()

    def insert_user_in_group(self, ): self.insert_user_in_group()

    def remove_of_group(self, ): self.remove_of_group()


class BasicEducationFactory(InstitutionFactory):

    @staticmethod
    def select_institution(institution: str) -> Institution:
        if institution == "cciweb.com.br":
            return BasicEducation()


class TechnicalEducationFactory(InstitutionFactory):

    @staticmethod
    def select_institution(institution: str) -> Institution:
        if institution == "tecscci.com.br":
            return TechnicalEducation()


class SuperioEducationFactory(InstitutionFactory):

    @staticmethod
    def select_institution(institution: str) -> Institution:
        if institution == "faculdadecci.com.br":
            return SuperiorEducation()
