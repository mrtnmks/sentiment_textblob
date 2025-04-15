# Analýza sentimentu pomocí knihovny TextBlob
# Tento program provede analýzu několika anglických vět
# a pro každou z nich určí sentiment (pozitivní/negativní/neutralní).
# TextBlob funguje decentně pro angličtinu (je jednoduchý, někdy až moc.. takže to má někdy problém správně rozpoznat sentiment) – pro češtinu má výrazná omezení.

from textblob import TextBlob

# Seznam anglických vět k analýze
texts = [
    "I love spending time with my dog. ",
    "This movie was okay.",
    "I despise these people. They are so annoying and rude.",
    "The food was absolutely delicious. I'll definitely come back!",
    "I don't like the weather, but it's alright",
    "This is the worst experience I've ever had.",
    "I am excited for the weekend trip with friends!"
]

# Analýza každé věty
for i, text in enumerate(texts, start=1):
    # Vytvoření TextBlob objektu pro analýzu sentimentu
    blob = TextBlob(text)
    # Získání polarity a subjektivity
    # Polarity: -1 (negativní) až 1 (pozitivní)
    # Subjectivity: 0 (objektivní) až 1 (subjektivní)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    # Rozhodnutí podle polarity
    if polarity > 0:
        sentiment = "Pozitivní sentiment"
    elif polarity < 0:
        sentiment = "Negativní sentiment"
    else:
        sentiment = "Neutrální sentiment"

    # Výpis výsledků
    print(f"\n--- Text #{i} ---")
    print(f"Text: {text}")
    print(f"Polarity: {polarity}")
    print(f"Subjectivity: {subjectivity}")
    print(f"Závěr: {sentiment}")
