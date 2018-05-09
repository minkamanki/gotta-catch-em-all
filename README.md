# gotta-catch-em-all

[Heroku linkki](https://pogowiki.herokuapp.com/ "pogowiki")

Järjestelmän tarkoituksena on tarjota käyttäjälle kattava lista olemassa olevista pokémoneista, niiden ominaisuuksista. Ylläpitäjän ominaisuudessa pystyy syöttämään näitä tietoja kantaan.

Lisäksi kuka tahansa muukin tietokannan internetistä löytänyt pystyy rekisteröitymään ja kirjautumaan järjestelmään, jolloin hän pääsee pitämään kirjaa omista pokemoneistaan ja näiden ominaisuuksista.

[Käyttötapaukset](https://github.com/minkamanki/gotta-catch-em-all/blob/master/documentation/userStoryt.md "Käyttötapaukset")

[Ohjeet](https://github.com/minkamanki/gotta-catch-em-all/blob/master/documentation/Ohjeet.md "Ohjeet")

### Pokemonin ominaisuudet:
|Nimi koodissa/ sovelluksessa|Selitys|Kuvassa|
|-|-|-|
|Cp | Combat points | Ympyröity oranssilla|
|Hp | Health points | Ympyröity vihreällä |
|Dust / Stardust | Stardustia voidaan käyttää Pokemon Go:ssa oman pokemonin power uppaamiseen. Stardustia saa pokemoneita nappaamalla, hatchaamalla, raideja suorittamalla sekä gymeillä olevia pokemoneita ruokkimalla. Pogowikissa kenttään "Stardust" tulee syöttää kyseisen pokemonin power uppaamiseen tarvittava stardustin määrä. | Ympyröity sinisellä|

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
