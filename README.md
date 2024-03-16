# Raspagem de dados - Magias de Dungeons & Dragons

Programa faz uma simples raspagem de dados para capturar todas as **462** magias oficiais de Dungeons & Dragons, presentes em seus diversos livros.
O programa gera um arquivo JSON (spells.json) com mais de 7 mil linhas, contendo todas as informações relevantes para cada magia.
Os dados seguem o seguinte formato:

```json
[
    {...},
    {
        "name": "Abi-Dalzim's Horrid Wilting",
        "type": "Necromancy",
        "level": "8",
        "casting_time": "1 Action",
        "range": "150 feet",
        "components": "V, S, M (a bit of sponge)",
        "duration": "Instantaneous",
        "description": "You draw the...",
        "at_higher_level": "",
        "source": "Page: 15 from EE Players Companion",
        "classes": [
            "Sorcerer",
            "Wizard"
            ]
    },
    {...}
]
```

### Observações

Algumas magias têm seus efeitos alterados ou "melhorados" caso utilizem espaços de magias além do seu nível, nesses casos, a chave **"at_higher_level"** será preenchida com as informações, de maneira similar à chave **"description"**, caso contrário, permanece vazia como no exemplo acima.

Utilizei a biblioteca `Selenium`, juntamente com um driver do Chrome (`chromedriver.exe`), pois tive problemas utilizando as bibliotecas `Requests` e `BeautifulSoup`. Acredito que o site tem alta dependência em `Javascript`, o que estava danificando os dados retornados.

Não disponibilizei o arquivo `chromedriver.exe` porque deve ser uma versão compatível com a versão atual do Chrome na máquina do usuário. Caso encontrem problemas de compatibilidade, podem baixar a versão adequada do ChromeDriver.

Para instalar as dependências, basta rodar o comando abaixo na raíz do projeto:
```bash
    pip install -r requirements.txt
```