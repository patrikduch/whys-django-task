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