# Ontology Associations

Datamodels for various kinds of ontology associations

Uses [LinkML](https://github.com/linkml/) project.

See http://biodatamodels.github.io/ontology-associations

## Running locally

```bash
. environment.sh
pip install -r requirements.txt
```

## Running locally

Python

```
pytest
```

See [tests](tests)

## Targets


You can make specific targets, e.g

```bash
make stage-jsonschema
```

Use the `all` target to make everything

Note to redeploy documentation all you need to do is:

```bash
make gh-deploy
```

