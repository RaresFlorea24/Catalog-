"""
from Tests import *
from Tests.Teste_domain.teste_disiplina import test_disciplina, test_equal_disciplina, test_validare_disciplina
from Tests.Teste_domain.teste_nota import test_nota, test_validare_nota
from Tests.Teste_domain.teste_student import test_student, test_equal_student, test_validator_student
from Tests.Teste_repo.teste_repo_discipline import run_teste_disciplina
from Tests.Teste_repo.teste_repo_nota import
from Tests.Teste_repo.teste_repo_studenti import
from Tests.Teste_service.teste_service_discipline import
from Tests.Teste_service.teste_service_note import
from Tests.Teste_service.teste_service_studenti import
from colorama import Style,Fore

def run_tests_service():
    #test_add_service()
    #test_actualizeaza_service()
    #test_find_service()
    #test_delete_service()
    #test_add_service()
    #test_actualizeaza_service()
    #test_find_service()
    #test_delete_service()
    #test_adauga_nota()
    #test_find_nota()
    #test_get_all()
    print("[INFO] " + Fore.GREEN + "Teste service rulate cu succes" + Style.RESET_ALL)


def run_tests_repos():
    run_tests_repo_disciplina()
    print("[INFO] " + Fore.GREEN + "Teste repo rulate cu succes" + Style.RESET_ALL)


def run_tests_domain():
    test_student()
    test_disciplina()
    test_equal_disciplina()
    test_validare_disciplina()
    test_equal_student()
    test_validator_student()
    test_nota()
    test_validare_nota()
    print("[INFO] " + Fore.GREEN + "Teste domain rulate cu succes" + Style.RESET_ALL)

def run_tests_all():
    run_tests_domain()
    run_tests_service()
    run_tests_repos()
"""