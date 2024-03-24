# whys-django-task

BE Django task for Whys startup.


## Assignment CZ

Zadání: 

Podívej se na json soubor test_data.json. Jsou tam data ve následujícím formátu:

[
  {
    "nazev modelu 1": {
      "sloupec 1": "data",
      "sloupec 2": ["pole", "dat"]
    }
  },
  {
    "nazev modelu 2": {
      "sloupec 1": "data",
    }
  },
  {
    "nazev modelu 1": {
      "sloupec 1": "data",
    }
  }
]


Tvým úkolem je vytvořit modely a API v Djangu, které bude příjimat tento JSON formát dat, zparsuje jej a bude mít následující endpointy pro přístup k těmto datům.
Piš to s předpokladem, že ten kód bude někdo číst, ujisti se, že špatný formát dat nezpůsobí v aplikaci chybu.

Endpointy:
[POST] /import - tento endpoint bude příjímat data a parsovat data
[GET] /detail/<nazev modelu>/ - seznam záznamů na základě názvu modelu
[GET] /detail/<nazev modelu>/<id> - všechna data ke konkrétnímu záznamu

* Nezapomeň vytvořit requirements.txt
* Nezapoměň vytvořit README, jak projekt spustit



## Development Guide

### /api/import

This guide provides detailed instructions on how to interact with the `/api/import/` POST endpoint of our API, which allows for batch importing data.

#### Overview

The `/api/import/` endpoint is designed to facilitate the batch importing of data into the system. It accepts structured JSON payloads that contain an array of model data objects.

#### Payload Structure
 
Format

The JSON payload should be an array of objects. Each object within the array must include a `name` field, which specifies the model into which the data will be imported, and a `data` field, which contains an object with the data to be imported.

Example

Below is an example payload that imports data into two models, `Model C` and `Model D`. Each object specifies the model name and the data to be imported into that model:

```json
[
    {
        "name": "Model C",
        "data": {
            "field1": "value1"
        }
    },
    {
        "name": "Model D",
        "data": {
            "field1": "value3"
        }
    }
]

