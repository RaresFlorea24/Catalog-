from Domain.validation import ValidatorStudent, ValidatorDisciplina, ValidatorNota
from Repository.repo_note import NoteRepoFile
from Repository.repo_studenti import StudentRepoFile
from Repository.repo_discipline import DisciplineRepoFile
from Service.nota_controller import ServiceNota
from Service.student_controller import ServiceStudent
from Service.disciplina_controller import ServiceDisciplina
#from Tests.run_test import run_tests_all
from UI.console import Console
def main():
    validator_discipline=ValidatorDisciplina()
    validator_studenti=ValidatorStudent()
    validator_note=ValidatorNota()

    repo_discipline=DisciplineRepoFile("Data/discipline.text")
    repo_studenti=StudentRepoFile("Data/studenti.text")
    repo_note=NoteRepoFile("Data/note.text")

    discipline_service=ServiceDisciplina(repo_discipline,validator_discipline)
    studenti_service=ServiceStudent(repo_studenti,validator_studenti)
    note_service=ServiceNota(repo_discipline,repo_studenti,repo_note,validator_note)

    console=Console(discipline_service,studenti_service,note_service)
    #run_tests_all()
    console.run()

if __name__=='__main__':
    main()
