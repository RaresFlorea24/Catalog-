from Domain.disciplina import Disciplina
from Domain.student import Student
from Domain.nota import Nota


class ValidatorDisciplina:
    def validate(self, disciplina: Disciplina):
        """
        Valideaza o melodie data
        :param disciplina: disciplina de validat
        :return:-
        :raises:ValueError cu mesajele de eroare daca disciplina nu este valida
        """
        errors = []
        if len(disciplina.get_nume()) < 2:
            errors.append("Numele disciplinei trebuie sa fie format din cel putin 2 litere")
        if len(disciplina.get_profesor()) < 2:
            errors.append("Numele profesorului trebuie sa fie format din cel putin 2 litere")

        if len(errors) > 0:
            error_message = '\n'.join(errors)
            raise ValueError(error_message)


class ValidatorStudent:
    def validate(self, student: Student):
        errors = []
        if len(str(student.get_IDstudent())) != 5:
            errors.append("ID-ul unui student trebuie sa contina 5 cifre")

        if len(student.get_nume()) < 2:
            errors.append("Numele unui student trebuie sa contina cel putin 2 litere")

        if len(errors) > 0:
            error_str = '\n'.join(errors)
            raise ValueError(error_str)


class ValidatorNota:
    def validate(self, nota):
        errors = []
        if not 1 <= nota.nota() <= 10:
            errors.append("Nota trebuie sa fie intre 1 si 10")

        if len(errors) > 0:
            error_str = '\n'.join(errors)
            raise ValueError(error_str)
