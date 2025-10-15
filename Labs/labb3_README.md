## 🧠 Beskrivning
Mitt program utför linjär klassificering av en uppsättning data från en given fil (`unlabelled_data.csv`).

---

## ⚙️ Hur man använder programmet
1. Säkerställ att unlabelled_data.csv ligger i samma mapp som Python-filen. 
2. Kör Python-filen. 
3. Programmet visar en graf med en linje baserad på medelvärdet av alla x, y-värden i unlabelled_data.csv samt de klassificerade punkterna utifrån den linjen.

---

## 📊 Övrigt
Efter att först ha skrivit kod som uppenbarligen hade med alldeles för mycket onödigt så som euklidiskt avstånd mellan punkterna och uppskattade mittpunkter av klusterna samt möjligheten att föra in egna punkter för klassificering så har jag nu bantat ner den till nuvarande format utifrån de synpunkter jag mottagit.

---

## 📁 Utdata
Programmet genererar även en fil `labelled_data.csv` om där inte redan finns en och skriver över innehållet i den filen om den redan finns. Där listas varje punkt med en klass (`0` eller `1`) beroende på vilken sida av linjen den ligger.

---

## Disclaimer
Slutligen ska bara tilläggas att jag använde chatGPT för att omvandla min text i readme-filen till markdown-format efter att ha bett chatGPT kontrollera att min text uppfyllde kriterierna för vad den skulle innehålla varpå den erbjöd att formatera om min text till vad vi har här vilket jag sedan bara städade upp lite till (Disclaimern gjorde jag själv dock och jag listade ut att två # gör det till en titel men jag vet inte hur jag får in de små symbolerna) 
