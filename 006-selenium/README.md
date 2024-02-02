# Teste de Automação Web Scraping com Selenium

Um teste usando apenas duas libs para automatizar a busca pelo app "Safari" e abrir um link repetidas vezes

## Configuração do Ambiente

### 1. Ambiente Virtual (venv)

Certifique-se de ter o Python instalado. Em seguida, crie e ative um ambiente virtual:

```bash
# No diretório do seu projeto
python -m venv .venv   #Cria o ambiente virtual
```

- Windows:

```bash
  .venv\Scripts\activate
```

- macOS/Linux:

```bash
  source .venv/bin/activate
```

### 2. Instalação de Dependências

Após ativar o ambiente virtual, instale as dependências do projeto usando o arquivo requirements.txt:

```bash
pip install -r requirements.txt
```

- Baixe a versão do Chrome Driver para a mesma versão que está utilizando (já baixei a versão 121.x para MACOS)
  [Link aqui](https://googlechromelabs.github.io/chrome-for-testing/)

- Extrai o conteúdo para a pasta <code>chrome-driver</code>

Depois rode o seguinte comando

```bash
cp -r driver/* .venv/bin/
```

## Executando o Projeto

Para executar, apenas rode o arquivo <code>main.py</code> da seguinte maneira:

```bash
python3 main.py
```

Aguarde a mágica acontecer!
