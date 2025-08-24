from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

senha_plana = "sgproject1"  # <-- altere se quiser
hash_senha = pwd_context.hash(senha_plana)

print("Senha:", senha_plana)
print("Hash gerado:")
print(hash_senha)



# venv) PS C:\Users\Utilizador\Documents\SynchroGest\synchrogest\backend\app> python gerar_hash.py
# Senha: admin123
# Hash gerado:
# $2b$12$Qa9SvyEti9sNFvSyVy8bJOxu6iR.TUu64HxcTwB6EW2t1eC/tWdQC