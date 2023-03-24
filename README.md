# Gendiff — утилита для сравнения конфигурационных файлов
___
[![Actions Status](https://github.com/Konst-Pav/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/Konst-Pav/python-project-50/actions)  [![Test Coverage](https://api.codeclimate.com/v1/badges/480e2cbbc0dafb58087e/test_coverage)](https://codeclimate.com/github/Konst-Pav/python-project-50/test_coverage)  [![Maintainability](https://api.codeclimate.com/v1/badges/480e2cbbc0dafb58087e/maintainability)](https://codeclimate.com/github/Konst-Pav/python-project-50/maintainability)
___
### Синтаксис команды:
#### gendiff [-f] ['first_file'] ['second file']
Варианты форматирования:
- stylish (по умолчанию)
- plain
- json
___
### Для утилиты нужно:
- Python 3.10
- Poetry 1.2
___
### Вывод утилиты в формате "Stylish":
[![asciicast](https://asciinema.org/a/Ow2aSGxCeVCC94dP3ZusNbZ3R.svg)](https://asciinema.org/a/Ow2aSGxCeVCC94dP3ZusNbZ3R)
___
### Вывод утилиты в формате "Plain":
[![asciicast](https://asciinema.org/a/1pHXC1K9ykEbwnDpYqfsJv89E.svg)](https://asciinema.org/a/1pHXC1K9ykEbwnDpYqfsJv89E)
___
### Вывод утилиты в формате "Json":
[![asciicast](https://asciinema.org/a/w70nsbRzm4FAfjTYCO9owAAWV.svg)](https://asciinema.org/a/w70nsbRzm4FAfjTYCO9owAAWV)
___
### Команды Makefile:
**make build** — poetry build — команда для получения директории dist/ и пакетов для установки  
**make install** — poetry install  
**make package-install** — python3 -m pip install --user dist/*.whl — установка программы  
**make lint** — poetry run flake8 brain_games — проверка линтера flake8
