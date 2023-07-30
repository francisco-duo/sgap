from abc import ABC, abstractmethod

from src.app.institution import Institution
from src.app.categories import Institutions


class InstitutionFactory(ABC):

    def __init__(self, ) -> None:
        self.institution = self.select_institution()

    @staticmethod
    @abstractmethod
    def select_institution(self, ) -> Institution: pass

    def create_user(self, students: list): self.institution.create_user(students)  # noqa: E501

    def create_group(self, groups: list): self.institution.create_group(groups)

    def insert_user_in_group(self, students: list): self.insert_user_in_group(students)  # noqa: E501


class InstitutionsFactory(InstitutionFactory):

    @staticmethod
    def select_institution(self, ) -> Institution:
        return Institutions()

# class BasicEducationFactory(InstitutionFactory):

#     @staticmethod
#     def select_institution(institution: str) -> Institution:
#         if institution == "cciweb.com.br":
#             return BasicEducation()


# class TechnicalEducationFactory(InstitutionFactory):

#     @staticmethod
#     def select_institution(institution: str) -> Institution:
#         if institution == "tecscci.com.br":
#             return TechnicalEducation()


# class SuperioEducationFactory(InstitutionFactory):

#     @staticmethod
#     def select_institution(institution: str) -> Institution:
#         if institution == "faculdadecci.com.br":
#             return SuperiorEducation()
