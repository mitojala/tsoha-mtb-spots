MTB-jännyyspaikat

Sovelluksen avulla voi etsiä ja lisätä tietokantaan maastopyöräily spotteja, joissa on jotain erityistä tai haastavaa. Kyseessä on siis yksittäisiä kohtia maastossa, esimerkiksi pudotus kalliolta alas tai hyppyri. Mitä tahansa, jonka ajaminen kuumottaa normaalia enemmän. Esimerkiksi pääkaupunkiseudulla näitä kohteita on paljonkin, mutta niitä ei ole koottu yhteen paikkaan, johon kaikilla halukkailla olisi helposti pääsy.

Käyttäjä voi olla peruskäyttäjä tai ylläpitäjä.

Käyttäjät voivat lisätä spotteja ja niiden metatietoja kuten spottien tyypin, vaikeusasteen 1 (helppo) - 5 (vaikea) ja sanallisen kuvauksen. Lisäksi spotteihin voi lisätä kuvia niistä tai niiden suorittamisesta.

Spotit näkyvät kartalla ja niitä voi etsiä alueen mukaan.

Käyttäjät voivat merkitä spotteihin suorituksen jolloin voidaan tilastoida esimerkiksi eniten/vähiten suorituksia keränneitä spotteja. Lisäksi muille käyttäjille voi lähettää haasteen.

Ylläpitäjä voi lisätä/poistaa spotteja.

---

Heroku:

https://tsoha-mtb-spots.herokuapp.com/

Automatic deploys on.

User must register in order to use the application. Otherwise the
functions are self explanatory at the moment.

Basic functions have been enabled. More complex things such as working
map interface is under work.

---

Database / PostgreSQL

Users - table of users:

id : integer
username : text
password : text
admin : boolean

Spots - table of mtb spots:

name : text
type : text
description : text
sent_at : timestamp

# more rows will be added

---

Background images:

index: Photo by Luca Beani on Unsplash

---

TODO:

- checkboxes for add_spot spot_type? (adds complexity to handling of
  the input)
- coordinates to add_spot form from google maps marker
- option to manually input coordinates that will update google maps
  marker position
- map search for spots
