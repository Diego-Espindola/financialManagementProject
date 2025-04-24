from datetime import date
import Movement as m

# Inserir
m1 = m.Movement(1, 205.5, "Salário", 1, date.today(), m.MovementType.INCOME)
m1.insert()

# Buscar
print(m.Movement.find(1))

# Atualizar
m1.value = 210.0
m1.description = "Salário ajustado"
m1.update()

print(m.Movement.find(1))

# Deletar
m.Movement.delete(1)
