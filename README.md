# Empreendedorismo

## Instalação

1. Clone o repositório:

```console
git clone https://github.com/seu-usuario/seu-repositorio.git
```

2. Acesse o diretório do projeto:

```console
cd seu-repositorio

```

3. Crie e ative o ambiente virtual:

```python
py -m venv venv
venv\Scripts\activate

```

4. Instale as dependências:

```python
pip install -r requirements.txt
```

## Configuração

1. Defina as variáveis de ambiente:

No Windows (PowerShell):

```console
$env:FLASK_APP="app"
$env:FLASK_DEBUG="True"

```

No Linux/macOS:

```console
export FLASK_APP=app
export FLASK_DEBUG=True

```

Para iniciar o servidor, execute o seguinte comando:

```python
flask run
```