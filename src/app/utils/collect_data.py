from src.resources.resources_sophia import students


class CollectData:
    def __init__(self, ) -> None:
        self.student_list = []
        self.__collect_data = self.__collect_data_of_sophia_of_new_students()

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

                            self.student_list.append(student_dict)

        return self.student_list

    def new_students(self, ): return self.__collect_data
