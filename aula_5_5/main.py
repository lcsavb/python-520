
import paramiko

client = paramiko.SSHClient()

opts = {
    'hostname': '13.58.52.58',
    'username': 'ubuntu',
    'pkey': paramiko.RSAKey.from_private_key_file('teste.pem')
}
client.connect(**opts)