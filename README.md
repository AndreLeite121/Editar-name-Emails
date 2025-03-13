Renomeador de Arquivos .eml

Este script percorre todas as pastas dentro de um diretório principal e renomeia arquivos .eml com base no assunto (subject) encontrado no corpo do e-mail.

Requisitos

Python 3.6+

Instalação

Clone este repositório:

git clone https://github.com/seuusuario/seurepositorio.git

Acesse o diretório do projeto:

cd seurepositorio

Uso

Edite o caminho da variável pastaPrincipal no código para apontar para o diretório onde estão os arquivos .eml.

Execute o script:

python trocarNomeEmails.py

Funcionalidades

Percorre todas as pastas dentro do diretório especificado.

Abre os arquivos .eml, extrai o campo Subject e renomeia os arquivos.

Substitui caracteres inválidos no nome do arquivo.

Evita sobrescrever arquivos já existentes adicionando um número incremental ao nome.

Lida com diferentes codificações de e-mails para evitar erros de leitura.

Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias no código.

Licença

Este projeto está sob a licença MIT.