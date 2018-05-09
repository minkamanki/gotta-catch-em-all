# gotta-catch-em-all

[Heroku linkki](https://pogowiki.herokuapp.com/ "pogowiki")

Järjestelmän tarkoituksena on tarjota käyttäjälle kattava lista olemassa olevista pokémoneista, niiden ominaisuuksista. Ylläpitäjän ominaisuudessa pystyy syöttämään näitä tietoja kantaan.

Lisäksi kuka tahansa muukin tietokannan internetistä löytänyt pystyy rekisteröitymään ja kirjautumaan järjestelmään, jolloin hän pääsee pitämään kirjaa omista pokemoneistaan ja näiden ominaisuuksista.

[Käyttötapaukset](https://github.com/minkamanki/gotta-catch-em-all/blob/master/documentation/userStoryt.md "Käyttötapaukset")

[Ohjeet](https://github.com/minkamanki/gotta-catch-em-all/blob/master/documentation/Ohjeet.md "Ohjeet")

### Pokemonin ominaisuudet:
|Nimi koodissa/ sovelluksessa|Selitys|Kuvassa|
|-|-|-|
|Cp | Combat points, oltava jotain väliltä 10 - 5000. | Ympyröity oranssilla|
|Hp | Health points, oltava vähintään 1. | Ympyröity vihreällä |
|Dust / Stardust | Stardustia voidaan käyttää Pokemon Go:ssa oman pokemonin power uppaamiseen. Stardustia saa pokemoneita nappaamalla, hatchaamalla, raideja suorittamalla sekä gymeillä olevia pokemoneita ruokkimalla. Pogowikissa kenttään "Stardust" tulee syöttää kyseisen pokemonin power uppaamiseen tarvittava stardustin määrä. Syötetyn stardustin täytyy olla väliltä 200 - 10 000. | Ympyröity sinisellä|

<img src="https://github.com/minkamanki/gotta-catch-em-all/blob/master/documentation/esimerkkipokemon.png" width="300">


![luokkakaavio](https://github.com/minkamanki/gotta-catch-em-all/blob/master/documentation/AlkuviikkojenLuokkakaavio.png)

![tietokantakaavio](https://github.com/minkamanki/gotta-catch-em-all/blob/master/documentation/Loppuviikkojentietokantakaavio.png)

Tietokantataulujen Create tablet:
```sqlite3
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	lvl INTEGER NOT NULL, 
	admin BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	CHECK (admin IN (0, 1))
);

CREATE TABLE pokedata (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	number INTEGER NOT NULL, 
	info VARCHAR(1000) NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE pokemon (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	powerupped BOOLEAN NOT NULL, 
	cp INTEGER NOT NULL, 
	hp INTEGER NOT NULL, 
	dust INTEGER NOT NULL, 
	account_id INTEGER NOT NULL, 
	pokedata_id INTEGER, 
	PRIMARY KEY (id), 
	CHECK (powerupped IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(pokedata_id) REFERENCES pokedata (id)
);

CREATE TABLE pokemontype (
	type_id INTEGER, 
	pokedata_id INTEGER, 
	FOREIGN KEY(type_id) REFERENCES type (id), 
	FOREIGN KEY(pokedata_id) REFERENCES pokedata (id)
);

CREATE TABLE type (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(10) NOT NULL, 
	"strongAgainst" VARCHAR(40) NOT NULL, 
	"weakAgainst" VARCHAR(40) NOT NULL, 
	other VARCHAR(1000) NOT NULL, 
	PRIMARY KEY (id)
);
```
Muutama monimutkaisempi yhteenvetokysely koodista:
```python 
    def find_pokemons_for_user(accountId):
        stmt = text("SELECT pokemon.id, pokemon.name, pokemon.cp, pokemon.hp, pokemon.powerupped, pokedata.name FROM account"
                     " INNER JOIN pokemon ON pokemon.account_id = account.id"
                     " INNER JOIN pokedata ON pokemon.pokedata_id = pokedata.id"
                     " WHERE (account.id = :accountId)").params(accountId=accountId)
		     ......
		     
    def find_pokemons_best_for_species(pokedataId):
        stmt = text("SELECT pokemon.id, pokemon.name, pokemon.cp, pokemon.hp, pokemon.powerupped, account.username FROM pokedata"
                     " INNER JOIN pokemon ON pokemon.pokedata_id = pokedata.id"
                     " INNER JOIN account ON pokemon.account_id = account.id"
                     " WHERE (pokedata.id = :pokedataId)"
                     " ORDER BY pokemon.cp DESC"
                     " LIMIT 5").params(pokedataId=pokedataId)
		     ......
		    
    def find_pokemons_best():
        stmt = text("SELECT pokemon.id, pokemon.name, pokemon.cp, pokemon.hp, pokemon.powerupped, account.username, pokedata.name FROM pokedata"
                     " INNER JOIN pokemon ON pokemon.pokedata_id = pokedata.id"
                     " INNER JOIN account ON pokemon.account_id = account.id"
                     " ORDER BY pokemon.cp DESC"
                     " LIMIT 10")	
		     ......
		     
    def find_users_pokemons_for_type(typeId, accountId):
        stmt = text("SELECT pokemon.id, pokemon.name, pokemon.cp, pokemon.hp, pokemon.powerupped, pokedata.name FROM type"
                     " INNER JOIN pokemontype ON type.id = pokemontype.type_id"
                     " INNER JOIN pokedata ON pokemontype.pokedata_id = pokedata.id"
                     " INNER JOIN pokemon ON pokemon.pokedata_id = pokedata.id"
                     " INNER JOIN account ON pokemon.account_id = account.id"                     
                     " WHERE (type.id = :typeId)"
                     " AND (account.id = :accountId)"
                     " ORDER BY pokemon.cp DESC").params(typeId=typeId, accountId=accountId)
        	     ......	     
		    
```
