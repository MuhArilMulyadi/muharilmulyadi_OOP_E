# Multi Inheritance

class Mhs_alumni:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilkan_info(self):
        return f"Nama: {self.nama}, NIM: {self.nim}"


class Mhs_aktif:
    def __init__(self, prodi, angkatan):
        self.prodi = prodi
        self.angkatan = angkatan

    def tampilkan_info(self):
        return f"Prodi: {self.prodi}, Angkatan: {self.angkatan}"


class KTM(Mhs_aktif):
    pass


class Ijazah(Mhs_alumni):
    pass


class Beasiswa(Mhs_aktif):
    pass


class Mhs_bebas_pustaka(Mhs_alumni, Mhs_aktif):
    def __init__(self, nama, nim, prodi, angkatan):
        Mhs_alumni.__init__(self, nama, nim)
        Mhs_aktif.__init__(self, prodi, angkatan)

    def tampilkan_info(self):
        info_alumni = Mhs_alumni.tampilkan_info(self)
        info_aktif = Mhs_aktif.tampilkan_info(self)
        return f"{info_alumni}, {info_aktif}"


# Object
ktm = KTM("Teknologi Informasi", 2024)
ijazah = Ijazah("Muh Aril Mulyadi", "24241164")
beasiswa = Beasiswa("Teknologi Informasi", 2024)
mhs_bebas_pustaka = Mhs_bebas_pustaka("Muh Aril Mulyadi", "24241164", "Teknologi Informasi", 2024)

# Output
print(ktm.tampilkan_info())
print(ijazah.tampilkan_info())
print(beasiswa.tampilkan_info())
print(mhs_bebas_pustaka.tampilkan_info())
