from usuario import Usuario

antonio = Usuario("Antonio", "antonio17","antonio_facundo@outlook.com")


print(antonio.username)
print(antonio.email)
print(antonio.password)

antonio.n_password = "nueva contra"

print(antonio.password)