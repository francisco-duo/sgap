from src.resources.resources_sophia import students


class CollectData:
    def __init__(self, ) -> None:
        self.student_list = []
        self.new_student_list = []
        self.__collect_data = self.__collect_data_of_sophia_of_new_students()
        self.__collect_all_data = self.__collect_data_of_sophia_of_all_students()  # noqa: E501

    def __collect_data_of_sophia_of_new_students(self, ) -> list:
        for student_object in students:
            if student_object["email"] is None or \
                    student_object["email"] == "":
                classroom_object = student_object["turmas"]

                if classroom_object is None:
                    pass
                else:
                    for classroom in classroom_object:
                        if "PEC" in classroom["descricao"] or \
                            "AQUA" in classroom["descricao"] or \
                                "Preparatório" in classroom["descricao"] or \
                                "Período" in classroom["descricao"] or \
                                "Acampamento" in classroom["descricao"] or \
                                "Oficina" in classroom["descricao"] or \
                                "Curso" in classroom["descricao"]:
                            pass
                        else:
                            student_dict = {
                                "id": student_object["codigo"],
                                "rm": student_object["codigoExterno"],
                                "name": student_object["nome"],
                                "classroom": classroom["descricao"]
                            }

                            self.new_student_list.append(student_dict)

        return self.new_student_list

    def __collect_data_of_sophia_of_all_students(self, ) -> list:
        for student_object in students:

            classroom_object = student_object["turmas"]

            if classroom_object is None:
                pass
            else:
                for classroom in classroom_object:
                    if "PEC" in classroom["descricao"] or \
                        "AQUA" in classroom["descricao"] or \
                            "Preparatório" in classroom["descricao"] or \
                            "Período" in classroom["descricao"] or \
                            "Acampamento" in classroom["descricao"] or \
                            "Oficina" in classroom["descricao"] or \
                            "Curso" in classroom["descricao"]:
                        pass
                    else:
                        student_dict = {
                            "id": student_object["codigo"],
                            "rm": student_object["codigoExterno"],
                            "name": student_object["nome"],
                            "email": student_object["email"],
                            "classroom": classroom["descricao"],
                            "parents": [x["email"] for x in student_object["responsaveis"] if x["responsavelPedagogico"] is True]  # noqa: E501
                        }

                        self.student_list.append(student_dict)

        return self.student_list

    def new_students(self, ): return self.__collect_data

    def all_students(self, ): return self.__collect_all_data
