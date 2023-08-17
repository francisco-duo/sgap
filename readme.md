# SGAP

## Sobre a aplicação.

- O SGAP surgiu com o intuito de resolver os desafios enfrentados por instituições que utilisam em seu meio administrativo o software de gestão Sophia e os apps do google workspace.

## O que faz?

- Cria grupos no admin google;
- Cria usuários no admin google;
- Insere os usuários criados no aplicativo de gestão Sophia.

# Como funciona?

- Para o funcionamento do script é necessário criar uma conta de serviço no google cloud console;
- Conectar a aplicação com a api do sophia;
- Adicionar os dados necessários nos arquivos de .settings.toml e .secrets.toml. Se houver dúvidas sobre o que colocar no .secrets.toml consulte o .secrets.example.toml;
- Lembre-se também de executar o comando no ambiente virutal pelo terminal ```pip install -r requirements.txt```

# Quais scripts executar?

- Execute apenas os arquivos que estão no diretório src/run
  - ```
    python create_emails.py
    python create_groups.py
    python insert_members.py
    ```
  