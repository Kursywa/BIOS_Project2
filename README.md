# BIOS_Project2
Przed uruchomieniem programu należy umieścić plik z rozszerzeniem .pdb  w tym samym folderze co program. Po uruchomieniu zostaniemy zapytani o nazwę pliku pdb. Nazwę należy podać bez typu rozszerzenia, np 2hhb.
Program pobiera listę reszt(residues) a następnie kalkuluje dystans pomiędzy każdaą resztą. Jeśli dystans jest mniejszy niż 8 A oznacza to, że reszty mogą ze sobą oddziaływać (do macierzy wstawiane jest 1). 
Etap ten zaimuje najwięcej czasu, ponieważ algorytm wtedy "myśli". Wyświetlane są odległości między resztami, które należy zignorować.
Na samym końcu wyświetlany jest wykres w formacie .png obrazujący możliwe oddziaływania między resztami
