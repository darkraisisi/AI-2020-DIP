/*
Vind alle klantparen die 4 of meer dezelfde producten (de hoeveelheid is niet belangrijk) hebben gekocht 
(optioneel per aankoop, optioneel per filiaal, optioneel het aantal overeenkomstige producten).
De achtergrond van de vraag is: hoe vinden we welke klanten hetzelfde gedrag vertonen?
*/
-- De basis van de query wordt gevormd door een query die de aankopen per klant teruggeeft:
-- NB: dit is een join tussen twee tabellen. Kan met JOIN-clause maar hier gebruik ik de
-- ouderwetse manier van Carthesisch product (aankoop, klant) met een beperking (aankoop.klant_idklant = klant.idklant). 
SELECT *
FROM   aankoop,
       klant
WHERE  aankoop.klant_idklant = klant.idklant
LIMIT  10;

-- Een SELECT levert een tabel op die je in een andere SELECT weer kunt bevragen...
SELECT *
FROM   (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl1
LIMIT  10;

-- .. en dat zou je eventueel nog een keer kunnen doen...
SELECT *
FROM   (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl1,
       (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl2
LIMIT  10;

-- .. dan heb je weer zo'n carthesisch product maakt (kl1 X kl2) dat elke rij van kl1 combineert met elke rij van kl2. Als je daarin nou alle rijen selecteert die over hetzelfde product gaan .... 
SELECT *
FROM   (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl1,
       (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl2
WHERE  kl1.product_idproduct = kl2.product_idproduct
LIMIT  10;

-- .. dan ben je er bijna. Er zitten nu wel dubbele rijen in, want elke rij van kl1 is gecombineerd met elke rij van kl2. Ik los dat zelf op door alleen die resultaten terug te geven waarin kl1 < kl2
-- Deze query beep boop
SELECT *
FROM   (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl1,
       (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl2
WHERE  kl1.product_idproduct = kl2.product_idproduct
       AND kl1.klant_idklant < kl2.klant_idklant
LIMIT  10;

-- ... nu moet je de kolommen in het resultaat combineren want we moeten ze straks gaan groeperen. Ik maak het mezelf makkelijk en combineer de relevante kolommen door middel van een string concat. Let op dat je ook het moment van aankoop moet gebruiken.  
SELECT Concat(kl1.klant_idklant, "-", kl2.klant_idklant, "-", kl1.datum, "-",
       kl2.datum)                                        named,
       Concat(kl1.klant_idklant, "-", kl2.klant_idklant) pairname
FROM   (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl1,
       (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl2
WHERE  kl1.product_idproduct = kl2.product_idproduct
       AND kl1.klant_idklant < kl2.klant_idklant
LIMIT  10;

-- ... door ze te groeperen kun je ze tellen ...
SELECT Count(*),
       Concat(kl1.klant_idklant, "-", kl2.klant_idklant, "-", kl1.datum, "-",
       kl2.datum)                                        named,
       Concat(kl1.klant_idklant, "-", kl2.klant_idklant) pairname
FROM   (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl1,
       (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl2
WHERE  kl1.product_idproduct = kl2.product_idproduct
       AND kl1.klant_idklant < kl2.klant_idklant
GROUP  BY named,
          pairname
LIMIT  10;

-- ... we zijn geinteresseerd in paren waarin meer dan 3 aankopen overeenkomen...
SELECT Count(*)
       aantal_gelijke_producten,
       Concat(kl1.klant_idklant, "-", kl2.klant_idklant, "-", kl1.datum, "-",
       kl2.datum)                                        named,
       Concat(kl1.klant_idklant, "-", kl2.klant_idklant) pairname
FROM   (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl1,
       (SELECT *
        FROM   aankoop,
               klant
        WHERE  aankoop.klant_idklant = klant.idklant) AS kl2
WHERE  kl1.product_idproduct = kl2.product_idproduct
       AND kl1.klant_idklant < kl2.klant_idklant
GROUP  BY named,
          pairname
HAVING aantal_gelijke_producten > 3;

-- ... nu nog tellen hoe vaak ieder klantpaar 4-of-meer-dezelfde-producten-tegelijk kocht,  en de query is klaar. Daarvoor gebruik ik opnieuw een GROUP BY en een COUNT. 
SELECT Count(*) AS aantal_keer_4_of_meer_producten_tegelijk_gekocht,
       pairname
FROM   (SELECT Count(*)
                      aantal_gelijke_producten,
               Concat(kl1.klant_idklant, "-", kl2.klant_idklant, "-", kl1.datum,
               "-",
               kl2.datum)                                        named,
               Concat(kl1.klant_idklant, "-", kl2.klant_idklant) pairname
        FROM   (SELECT *
                FROM   aankoop,
                       klant
                WHERE  aankoop.klant_idklant = klant.idklant) AS kl1,
               (SELECT *
                FROM   aankoop,
                       klant
                WHERE  aankoop.klant_idklant = klant.idklant) AS kl2
        WHERE  kl1.product_idproduct = kl2.product_idproduct
               AND kl1.klant_idklant < kl2.klant_idklant
        GROUP  BY named,
                  pairname
        HAVING aantal_gelijke_producten > 3) AS allrecords
GROUP  BY pairname;

-- Vind alle klantparen die 4 of meer dezelfde producten hebben gekocht (optioneel per aankoop, optioneel per filiaal, optioneel het aantal overeenkomstige produceten).
SELECT Count(*) AS aantal_keer_4_of_meer_producten_tegelijk_gekocht,
       pairname
FROM   (SELECT Count(*)
                      aantal_gelijke_producten,
               Concat(kl1.klant_idklant, "-", kl2.klant_idklant, "-", kl1.datum,
               "-",
               kl2.datum)                                        named,
               Concat(kl1.klant_idklant, "-", kl2.klant_idklant) pairname
        FROM   (SELECT *
                FROM   aankoop,
                       klant
                WHERE  aankoop.klant_idklant = klant.idklant) AS kl1,
               (SELECT *
                FROM   aankoop,
                       klant
                WHERE  aankoop.klant_idklant = klant.idklant) AS kl2
        WHERE  kl1.product_idproduct = kl2.product_idproduct
               AND kl1.klant_idklant < kl2.klant_idklant
        GROUP  BY named,
                  pairname
        HAVING aantal_gelijke_producten > 3) AS allrecords
GROUP  BY pairname
LIMIT  30;

-- Bereken het totaal aantal klantparen.
SELECT Count(DISTINCT( pairname )) AS totaal_aantal_klantparen
FROM   (SELECT Count(*)
                      aantal_gelijke_producten,
               Concat(kl1.klant_idklant, "-", kl2.klant_idklant, "-", kl1.datum,
               "-",
               kl2.datum)                                        named,
               Concat(kl1.klant_idklant, "-", kl2.klant_idklant) pairname
        FROM   (SELECT *
                FROM   aankoop,
                       klant
                WHERE  aankoop.klant_idklant = klant.idklant) AS kl1,
               (SELECT *
                FROM   aankoop,
                       klant
                WHERE  aankoop.klant_idklant = klant.idklant) AS kl2
        WHERE  kl1.product_idproduct = kl2.product_idproduct
               AND kl1.klant_idklant < kl2.klant_idklant
        GROUP  BY named,
                  pairname
        HAVING aantal_gelijke_producten > 3) AS allrecords
LIMIT  30; 
 

/*
Vind welke productparen het vaakst (top-50) tegelijk gekocht worden (optioneel per filiaal) .
*/

SELECT	Count(*) AS tegelijk_gekocht,
       	Concat(a1.product_idproduct, "-", a2.product_idproduct) pairname
FROM   (SELECT *
        FROM   aankoop
        WHERE  aankoop.datum = aankoop.datum
        AND	   aankoop.product_idproduct = aankoop.product_idproduct
        AND    aankoop.filiaal_idfiliaal = 0) AS a1,
       (SELECT *
        FROM   aankoop
        WHERE  aankoop.datum = aankoop.datum
        AND	   aankoop.product_idproduct = aankoop.product_idproduct
       	AND    aankoop.filiaal_idfiliaal = 0) AS a2
        
WHERE  a1.product_idproduct != a2.product_idproduct
       AND a1.product_idproduct < a2.product_idproduct
       
GROUP BY pairname 
ORDER BY tegelijk_gekocht  DESC LIMIT  50


/*
Als klant A filiaal 1 bezoekt, en klant B bezoekt filiaal 1 en 2, en klant C bezoekt filiaal 2, 
dan kun je stellen dat klant A en B 0 filialen van elkaar verwijderd zijn, en klant A en C 1 filiaal. 
Vind hoeveel filialen twee willekeurige klanten van elkaar verwijderd zijn.
*/
SELECT DISTINCT a1.klant_idklant, a1.filiaal_idfiliaal, a2.klant_idklant, a2.filiaal_idfiliaal

FROM

(SELECT *
FROM aankoop
WHERE aankoop.klant_idklant = 0) as a1,

(SELECT *
FROM aankoop
WHERE aankoop.klant_idklant = 1) as a2

# GROUP BY a1.klant_idklant, a1.filiaal_idfiliaal, a2.klant_idklant, a2.filiaal_idfiliaal