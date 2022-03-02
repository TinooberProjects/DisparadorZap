![](https://tinoober.com/imagens/cabecalho.png)

# O que é o Disparador de Mensagens Zap?

Este projeto de web srcaping desenvolvido em PYTHON para  automatização de disparo de mensagens no Whats App.
Foram utilizados nesta aplicação como base: Selenium, Pandas, Tkinter

# O que ele faz?
Automatiza o envio de mensagens para clientes e grupos do WhatsApp, a partir de uma base de dados previamente cadastrada.

Realiza a limpeza de grupos, envio de mensagens para clientes e envio de imagens, pdf ou pequenos vídeos para grupos do WhatsApp.


# Requisitos do sistema ( Executável Windows)

- Sistema Operacional : Windows 10 64 bits
- Processador (recomendado): Intel Core i3 ou superior
- Memória (mínimo recomendado): 4GB
- Armazenamento ( mínimo): 5 GB
- Navegador Firefox



# Pastas

- ` Base de Dados`: Arquivo .xlsm (Excel com Macros), otimizado para o cadastro dos clientes, imagens e grupos;


- ` Manual de uso`: Descrição geral da aplicação;


# Dependências

## Observação: 

Lembre-se, uma boa prática no Python, é a criação de Ambientes virtuais, crie-o e ou ative-o antes da instalação das dependências

- Criação do Ambiente Virtual:
   
   `pip install -U virtualenv` : instalação;
   
    `python3 0m virtualenv nomeDoAmbienteVirtual`: criação do Ambiente Virtual. Modifique nomeDoAmbienteVirtual pelo nome que desejar;

    `source nomeDoAmbienteVirtual/bin/activate`:ativando o Ambiente Virtual.

- Para instalar as dependências de forma prática:

`pip install -r requirements.txt `

`pip install dependendcias.txt`

- Caso dê algum erro:

`pip install selenium`

`pip install pandas`

- Instale o Firefox;

- Busque o webdriver compatível. Neste código o Geckodriver




# Gerando um arquivo executável

## Existem 2 formas básicas: 

### Opção 1
- 1- instale o pyinstaller

`pip install pyinstaller`

- 2-Para executar 

`pyinstaller -w "arquivo python"` 
(funciona melhor com arquivos simples)

- Buscar a pasta dist, e lá vc terá o seu arquivo distribuível

### Opção 2

- 1- Instale Auto py to exe 

 `pip install auto-py-to-exe`

- 2- Para executar
`auto-py-to-exe` 

