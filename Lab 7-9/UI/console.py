from colorama import Fore, Style


class Console:
    def __init__(self, discipna_service, student_service, nota_service):
        self.__disciplina_service = discipna_service
        self.__student_service = student_service
        self.__nota_service = nota_service

    @staticmethod
    def afiseaza_meniu():
        print("Comenzile disponibile pentru gestiunea entitatilor sunt: ")
        print("add_, find_, delete_, show_, mod_ (Ex: add_disciplina)")

    def citeste_info_disciplina_ui(self):
        id = int(input("Introduceti ID-ul disciplinei: "))
        nume = input("Introduceti numele disciplinei: ")
        profesor = input("Introduceti numele profesorului: ")

        return id, nume, profesor

    def citeste_info_student_ui(self):
        IDStudent = int(input("Introduceti ID-ul studentului: "))
        nume = input("Introduceti numele studentului: ")

        return IDStudent, nume

    def citeste_info_nota_ui(self):
        id_disciplina = int(input("ID disciplina: "))
        id_student = int(input("ID student: "))
        nota = float(input("Introdu nota: "))

        return id_disciplina, id_student, nota

    def afiseaza_entitati(self, lista_entitati):
        for entitate in lista_entitati:
            print(entitate)

    def adauga_disciplina_ui(self):
        id, nume, profesor = self.citeste_info_disciplina_ui()

        try:
            self.__disciplina_service.adauga_disciplina(id, nume, profesor)
            print(Fore.GREEN + "Adaugare realizata cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def adauga_student_ui(self):
        id, nume = self.citeste_info_student_ui()

        try:
            self.__student_service.adauga_student(id, nume)
            print(Fore.GREEN + "Adaugare realizata cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def __adauga_nota_ui(self):
        try:
            id_disciplina, id_student, nota = self.citeste_info_nota_ui()
            self.__nota_service.adauga_nota(id_disciplina, id_student, nota)
            print(Fore.GREEN + "Adaugare realizata cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def modifica_disciplina_ui(self):
        id, nume_nou, profesor_nou = self.citeste_info_disciplina_ui()
        try:
            self.__disciplina_service.actualizeaza_disciplina(id, nume_nou, profesor_nou)
            print(Fore.GREEN + "Modificare realizata cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def modifica_student_ui(self):
        id, nume = self.citeste_info_student_ui()
        try:
            self.__student_service.actualizeaza_student(id, nume)
            print(Fore.GREEN + "Modificare realizata cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def sterge_disciplina_ui(self):
        id, nume, profesor = self.citeste_info_disciplina_ui()
        try:
            self.__disciplina_service.delete_disciplina(id, nume, profesor)
            print(Fore.GREEN + "Stergere realizata cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def sterge_student_ui(self):
        id = int(input("Introduceti id-ul: "))
        try:
            self.__student_service.delete_student(id)
            print(Fore.GREEN + "Stergere realizata cu succes." + Style.RESET_ALL)
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def cauta_disciplina_ui(self):
        try:
            id = int(input("Introdu ID-ul cautat: "))
            disciplina = self.__disciplina_service.find_disciplina(id)
            if disciplina is not None:
                print("Urmatoarea discipina are ID-ul dat :", disciplina)
            else:
                print("Nu s-a gasit melodie cu ID-ul dat")
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def cauta_student_ui(self):
        try:
            id = int(input("Introdu ID-ul cautat:"))
            student = self.__student_service.find_student(id)
            if student is not None:
                print("S-a gasit urmatoarea persoana:", student)
            else:
                print("Nu s-a gasit persoana cu cnp dat.")
        except ValueError as ve:
            print(Fore.RED + str(ve) + Style.RESET_ALL)

    def add_default_studenti(self):
        self.__student_service.add_default()
        print(Fore.GREEN + "Adaugare realizata cu succes." + Style.RESET_ALL)

    def add_default_disciplina(self):
        self.__disciplina_service.add_default()
        print(Fore.GREEN + "Adaugare realizata cu succes." + Style.RESET_ALL)

    def nota_disciplina(self):
        lista = []
        cod_disciplina = int(input("Introduceti codul disciplinei: "))
        for nota in self.__nota_service.get_all():
            if nota.disciplina().get_idDisciplina() == cod_disciplina:
                lista.append(nota)
        return lista

    def nota_disciplina_nume(self):
        lista = self.nota_disciplina()
        lista_sortata = sorted(lista, key=lambda nota: nota.student().get_nume())
        for elem in lista_sortata:
            print(elem)

    def nota_disciplina_nota(self):
        lista = self.nota_disciplina()
        lista_sortata = sorted(lista, key=lambda nota: nota.nota())
        for elem in lista_sortata:
            print(elem)

    def calculeaza_medii(self, note):
        medii = {}
        for nota in note:
            if nota.student().get_nume() not in medii:
                medii[nota.student().get_nume()] = []
            medii[nota.student().get_nume()].append(nota.nota())

        for student in medii:
            medii[student] = sum(medii[student]) / len(medii[student])
        return medii

    def primii_20_la_suta(self, note):
        medii = self.calculeaza_medii(note)
        if not medii:#nu exista medii
            return []

        studenti_ordonati = self.__nota_service.bubble_sort(list(medii.items()), key=lambda x: x[1], reverse=True)
        top_20 = max(1, int(0.2 * len(studenti_ordonati)))
        return studenti_ordonati[:top_20]
    @staticmethod
    def meniu_mare():
        print("1.Modifica Student")
        print("2.Modifica Disciplina")
        print("3.Modifica Nota")
        print("4.Primii 20%")
        print("5.Afisare tot")
        print("0.Exit")

    @staticmethod
    def meniu_student():
        print("1.Adauga")
        print("2.Modifica")
        print("3.Sterge")
        print("4.Gaseste")
        print("5.Adauga default")
        print("6.Fill random")
        print("7.Afisare")
        print("8.Inapoi")

    @staticmethod
    def meniu_disciplina():
        print("1.Adauga")
        print("2.Modifica")
        print("3.Sterge")
        print("4.Gaseste")
        print("5.Adauga default")
        print("6.Fill random")
        print("7.Afisare")
        print("8.Inapoi")

    @staticmethod
    def meniu_nota():
        print("1.Adauga")
        print("2.Afiseaza")
        print("3.Filtru 1")
        print("4.Filtru 2")

    def run(self):
        is_running = True
        while is_running:
            self.meniu_mare()
            cmd = input(">>>").strip().lower()
            match cmd:
                case "1":
                    is_running_nota=True
                    while is_running_nota:
                        self.meniu_student()
                        cmdn=input(">>>").strip().lower()
                        match cmdn:
                            case "1":
                                self.adauga_student_ui()
                            case "2":
                                self.modifica_student_ui()
                            case "3":
                                self.sterge_student_ui()
                            case "4":
                                self.cauta_student_ui()
                            case "5":
                                self.add_default_studenti()
                            case "6":
                                studenti=self.__student_service.fill_studenti()
                                for student in studenti:
                                    self.__student_service.adauga_student(student.get_IDstudent(), student.get_nume())
                            case "7":
                                self.afiseaza_entitati(self.__student_service.get_all())
                            case "8":
                                is_running_nota=False

                case "2":
                    is_running_disciplina = True
                    while is_running_disciplina:
                        self.meniu_disciplina()
                        cmdd = input(">>>").strip().lower()
                        match cmdd:
                            case "1":
                                self.adauga_disciplina_ui()
                            case "2":
                                self.modifica_disciplina_ui()
                            case "3":
                                self.sterge_disciplina_ui()
                            case "4":
                                self.cauta_disciplina_ui()
                            case "5":
                                self.add_default_disciplina()
                            case "6":
                                for disciplina in self.__disciplina_service.fill_discipline():
                                    self.__disciplina_service.adauga_disciplina(disciplina.get_idDisciplina(),
                                                                                disciplina.get_nume(),
                                                                                disciplina.get_profesor())
                            case "7":
                                self.afiseaza_entitati(self.__disciplina_service.get_all())
                            case "8":
                                is_running_disciplina = False

                case "3":
                    is_running_nota = True
                    while is_running_nota:
                        self.meniu_nota()
                        cmdn = input(">>>").strip().lower()
                        match cmdn:
                            case "1":
                                self.__adauga_nota_ui()
                            case "2":
                                self.afiseaza_entitati(self.__nota_service.get_all())
                            case "3":
                                self.nota_disciplina_nume()
                            case "4":
                                self.nota_disciplina_nota()
                            case "5":
                                is_running_nota=False

                case "4":
                    print(self.primii_20_la_suta(self.__nota_service.get_all()))

                case "5":
                    self.afiseaza_entitati(self.__student_service.get_all())
                    print("")
                    self.afiseaza_entitati(self.__disciplina_service.get_all())

                case "0":
                    break