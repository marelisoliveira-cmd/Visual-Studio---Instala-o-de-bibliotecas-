from faker import Faker

fake = Faker("pt_BR")

print("Nome fictício:", fake.name())
print("Endereço fictício:", fake.address())
print("E-mail fictício:", fake.email())