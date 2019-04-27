import pymongo

client = pymongo.MongoClient()

db = client.projeto

# db.users.insert({'nome': 'Cobrinha aamrela'})

# for user in db.users.find():
# 	print(user)

def cadastrar_usuario(nome,email,idade):
	usuario = db.users.find_one({ 'email': email })
	if not usuario:
	    db.users.insert({
	    	'nome': nome,
	    	'email': email,
	    	'idade': int(idade)
	    	})


def extrair_usuarios():
    return list(db.users.find())
    

cadastrar_usuario(
    'Lucas Amorim Vieira de Barros',
    'lcsavb@gmaildfsdfsdfsda.com',
    32
)


for usuario in extrair_usuarios():
	print(usuario)