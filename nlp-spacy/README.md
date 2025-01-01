In order to install ther language model I had to run the following commands

```shell
poetry shell
python -m spacy download en_core_web_sm
```

If you prefer not to activate the poetry shell, you can also run the command directly within the poetry environment:

```shell
poetry run python -m spacy download en_core_web_sm
```