Sovellus toimii osoitteessa: https://pogowiki.herokuapp.com/

Admin tunnukset web sovellukseen ovat:

username: admin <br>
password: admin

Nykyisellään käyttäjistä  voidaan muokkaa admineita vain manuaalisesti tietokannan kautta (asettamalla rooli = true).

Sovelluksen voi lada itselleen githubista, joko zip-tiedostona tai kloonamalla.<br>
Sen voi suorittaa lokaalisti ensin luomalla virtuaaliympäristön, linuksissa esim. "python3 -m venv venv" komennolla.<br>
Tämä jälkeen tulee vielä antaa komento "pip install -r requirements.txt"<br>
Nyt ohjelman voi suorittaa komennolla "python run.py"

## Käyttöohjeet

Luo tunnus "Sign in"- nappia painamall. Täytä oma nimesi, Pokemon Go nimimerkkisi, salasana sekä Pokemon Go level. Huomioi, ettei voi olla kahta samaa käyttäjätunnusta. Paina Creare account -nappia luodaksesi tunnuksen syöttämillä arvoilla.

Tämän jälkeen voit kirjautua sisään "Login" napista. Syötä tänne käyttäjänimesi ja salasanasi.

Jos kirjaiduit sisään adminina sivun alareunass on näkyy "Admin's buttons".<br>
Ylimmän kautta voit syöttää kokonaan uusia pokemon lajeja tietokantaan.<br>
Seuraavasta lisäät uusia pokemonien tyyppejä.<br>
Alimmasta yhdistät pokemon tyypin tiettyyn pokemon lajiin.

Kaikki kirjautuneet voivat lisää pokemonejä "Add new pokemon" valikosta. Valitse dropdown valikosta mitä pokemon lajia pokemonisi on. Sen jälkeen anna sille nimi (usein pelaajat haluavat nimetä pokemoninsa IV -arvon ja iskujen mukaan). Syötä myös pokemonin oma CP ja HP, sekä power uppaamiseen tarvitava stardustin määrä. Kerro myös oletko power uppannut pokemoniasi.

