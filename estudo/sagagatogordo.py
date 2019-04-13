lista_de_gatos = [
{ 
'nome': 'Malawi',
'peso': 3750
},
{
'nome': 'Gato',
'peso': 6000
}
]

gatos_gordos = []
gatos_magros = []

for gato in lista_de_gatos:
	if int(gato['peso']) > 5000:
		gatos_gordos.append(gato)
else:
	gatos_magros.append(gato) 

print(gatos_magros)

print(gatos_gordos)
