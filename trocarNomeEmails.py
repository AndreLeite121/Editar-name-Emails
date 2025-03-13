import os
import email
from email import policy
import re

pastaPrincipal = '/Users/andreleite/Downloads/Aline Emails'

def limpar_nome_arquivo(nome):
    return re.sub(r'[\/:;*?"<>|]', '_', nome)

for pasta_raiz, _, arquivos in os.walk(pastaPrincipal):
    for arquivo in arquivos:
        if arquivo.endswith('.eml'):
            caminho_antigo = os.path.join(pasta_raiz, arquivo)
            msg = None
            for encoding in ["utf-8", "latin-1", "ISO-8859-1"]:
                try:
                    with open(caminho_antigo, 'r', encoding=encoding, errors="ignore") as f:
                        msg = email.message_from_file(f, policy=policy.default)
                    break
                except UnicodeDecodeError:
                    print(f"Erro de decodificação com {encoding} em {arquivo}, tentando outro...")

            if msg is None:
                print(f"Erro ao abrir {arquivo}, ignorando.")
                continue

            subject = msg['Subject'] or 'sem_assunto'
            subject = limpar_nome_arquivo(subject)

            novo_caminho = os.path.join(pasta_raiz, f'{subject}.eml')
            contador = 1
            while os.path.exists(novo_caminho):
                novo_caminho = os.path.join(pasta_raiz, f'{subject}_{contador}.eml')
                contador += 1

            os.rename(caminho_antigo, novo_caminho)
            print(f'Renomeado: {arquivo} -> {os.path.basename(novo_caminho)}')

print("Processo concluído!")
