from dataclasses import dataclass
from datetime import date
from jinja2 import Template
from typing import List

LOGO = "_readme/logo.txt"
MENSAJE = "_readme/saludar.py"
DESCRIPCION = "_readme/descripcion.txt"
REPOS = "_readme/repos.csv"
REGLAS = "_readme/reglas.md"

readme = Template('''\
![maintenance](https://img.shields.io/maintenance/yes/{{year}})
[![Ayuda en Python CI](https://github.com/AyudaEnPython/AyudaEnPython/actions/workflows/main.yml/badge.svg)](https://github.com/AyudaEnPython/AyudaEnPython/actions/workflows/main.yml)

{{logo}}              

## Descripción

{{descripcion}}

```python
{{mensaje}}
```
---

## Nuestros Repositorios

{% for repo in repos %}
* [{{repo.name}}]({{repo.url}}):
  {{repo.description}}
{% endfor %}
> _*NOTA*_: Conforme se vayan agregando más repositorios, esta lista se irá
> actualizando.

---

## Reglas de la Comunidad

{{reglas}}
'''
)


def read_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def read_repo_data(filename: str, class_: object) -> List[str]:
    with open(filename, "r") as f:
        data = [line.split(";") for line in f.read().splitlines()]
    return [class_(name, description) for name, description in data[1:]]


@dataclass
class Repo:
    name: str
    description: str

    def __post_init__(self) -> None:
        self.url = "https://github.com/AyudaEnPython/{}".format(self.name)


def main():
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme.render(
            year=date.today().year,
            logo=read_file(LOGO),
            mensaje=read_file(MENSAJE),
            descripcion=read_file(DESCRIPCION),
            reglas=read_file(REGLAS),
            repos=read_repo_data(REPOS, Repo),
        ))


if __name__ == "__main__":
    main()
