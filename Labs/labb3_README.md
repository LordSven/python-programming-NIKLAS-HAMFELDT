## 🧠 Beskrivning
Mitt program utför linjär klassificering av en uppsättning data från en given fil (`unlabelled_data.csv`) samt eventuella egna punkter som användaren kan mata in. Punkterna klassificeras baserat på den data som lästs in.

Jag har valt att visa två exempel:

1. **Uppskattad linje:** Jag uppskattade var medelpunkten för varje kluster låg och drog en linje mellan dessa punkter som en första uppdelning.  
2. **Uträknad linje:** Därefter räknade jag ut en ny, mer träffsäker linje baserat på de faktiska medelvärdena för cluster0 och cluster1.

---

## ⚙️ Hur man använder programmet
1. Kör Python-filen.  
2. Välj om du vill mata in egna koordinater eller om du vill låta programmet slumpa fram en punkt ur den givna datan.  
3. Programmet visar två grafer:  
   - En med den **uppskattade delande linjen**.  
   - En med den **uträknade (korrekta) delande linjen**.  
4. Du får även textutskrift som visar om den valda punkten ligger **över** eller **under** linjen, vilket också kan ses i graferna.

---

## 📊 Övrigt
Anledningen till att jag valde att ha med båda graferna är att jag ville visa min tankegång för uppgiften.  
Innan jag räknade ut den mer exakta linjen hamnade alla punkter vars summa blev 0 precis på linjen, vilket gjorde att de inte kunde klassificeras. Därför hade jag också lagt till kod som kunde:
- Ge svaret att punkten ligger *på* linjen, och  
- Räkna antalet samt kartlägga eventuella felklassificeringar.

---

## 📁 Utdata
Programmet genererar även en fil `labelled_data.csv` om där inte redan finns en och skriver över innehållet i den filen om den redan finns. Där listas varje punkt med en klass (`0` eller `1`) beroende på vilken sida av linjen den ligger.

---
## Disclaimer
Slutligen ska bara tilläggas att jag använde chatGPT för att omvandla min text i readme-filen till markdown-format efter att ha bett chatGPT kontrollera att min text uppfyllde kriterierna för vad den skulle innehålla varpå den erbjöd att formatera om min text till vad vi har här vilket jag sedan bara städade upp lite till (Disclaimern gjorde jag själv dock och jag antar att två # gör det till en titel men jag vet inte hur jag får in de små symbolerna) 
