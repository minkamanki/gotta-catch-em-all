## Nykyiset:

### Käyttäjä
Voi luoda itselleen käyttäjätunnukset.

PokemonWikissä kävijä voi lisätä itselleen pokemoneita, tiettyyn pokemon lajiin.

Käyttäjä merkitsee pokemonille pokemonkohtaisia tietoja.

Näkee listattuna omat pokemoninsa.<br>
```
SELECT pokemon.id, pokemon.name, pokemon.cp, pokemon.hp, pokemon.powerupped, pokedata.name FROM account
 INNER JOIN pokemon ON pokemon.account_id = account.id
 INNER JOIN pokedata ON pokemon.pokedata_id = pokedata.id
 WHERE (account.id = :accountId)
```

Oman pokemonin voi poistaa ja sen tietoja voi muokata

Voi nähdä kaikki tietokantaan syötetyt pokemon lajit, ja lukea niistä tietoja pokemonlaji sivulla.

Voi nähdä kaikki tietokantaan syötetyt tyypit, ja lukea niistä tietoja tyypin sivulla.
```python
Type.query.all()
```
Etusivulla käyttäjä näkee listattuna 10 parasta pokemonia koko sovelluksessa.
```
SELECT pokemon.id, pokemon.name, pokemon.cp, pokemon.hp, pokemon.powerupped, account.username, pokedata.name FROM pokedata
 INNER JOIN pokemon ON pokemon.pokedata_id = pokedata.id
 INNER JOIN account ON pokemon.account_id = account.id
 ORDER BY pokemon.cp DESC
 LIMIT 10
```

Aina tietyn pokemonlajin sivulla käyttäjä näkee sovelluksen 5 parasta pokemonia tästä lajista.
```
SELECT pokemon.id, pokemon.name, pokemon.cp, pokemon.hp, pokemon.powerupped, pokedata.name FROM type
 INNER JOIN pokemontype ON type.id = pokemontype.type_id
 INNER JOIN pokedata ON pokemontype.pokedata_id = pokedata.id
 INNER JOIN pokemon ON pokemon.pokedata_id = pokedata.id
 INNER JOIN account ON pokemon.account_id = account.id                   
 WHERE (type.id = :typeId)
 AND (account.id = :accountId)
 ORDER BY pokemon.cp DESC
```
Tyypin sivulle on listattu käyttäjän omat pokemonit kyseisestä tyypistä, jos niitä on.

### Admin
Voi lisätä uusia pokemonlajeja, joista käyttäjä luo omia ilmentymiään.

Voi lisätä tyyppejä.

Pokemonlajiin voi liittää tyyppejä.


## Mahdollista jatkokehitystä

### Käyttäjä
Näytä mitä pokemoneita käyttäjällä ei vielä ole.

Omien tietojen muokkaus

### Admin
Mahdollisuus tehdä muista käyttäjistä admineita.
