class Student:
    
    def __init__(self, nama="Student", umur=0, asal="Tidak tahu"):
        self.nama = nama
        self.umur = umur
        self.asal = asal
    
    def printStudent(self):
        print("Nama: ", self.nama)
        print("Umur: ", self.umur)
        print("Asal: ", self.asal)
    
    # Getter Method Declaration
    def getNama(self):
        return self.nama
    
    def getUmur(self):
        return self.Umur
    
    def getAsal(self):
        return self.asal
    
    # Setter Method Declaration
    def setNama(self, nama):
        self.nama = nama
    
    def setUmur(self, umur):
        self.umur = umur
    
    def setAsal(self, asal):
        self.asal = asal


studentNama = input("Masukkan Nama: ")
studentUmur = input("Masukkan Umur: ")
studentAsal = input("Masukkan Asal: ")

student1 = Student(studentNama, studentUmur, studentAsal)

student1.printStudent()

studentNama = student1.getNama()
print("Nama Siswa", studentNama)