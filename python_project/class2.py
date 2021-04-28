class School:
    haknyun = 1

    def __init__(self, name, year, address):
        self.name = name
        self.year = year
        self.address = address
    def start(self):
        self.haknyun = self.haknyun + 1

school1 = School("chuncheon", "1964", "test")
school1.start()
school1.start()
print(school1.haknyun,school1.name, school1.year, school1.address)
