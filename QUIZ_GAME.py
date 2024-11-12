import streamlit as st

# Introductie en animatie
def intro():
    st.title("🎉 Welkom bij de Disco Dans Knikkers Quiz! 🎉")
    st.write("Hoe goed ken je me echt? Doe de quiz en ontdek het!")
    st.markdown("""
    **Spelregels:**
    - Antwoorden zijn niet hoofdlettergevoelig.
    - Voor A/B/C vragen hoef je alleen de letter te geven.
    - Het opzoeken van antwoorden is strikt verboden! 😜
    """)
    st.write("**Druk op de knop hieronder om te beginnen!**")
    start = st.button("🚀 Start de Quiz")
    return start

# Functie voor de quiz
def quiz():
    score = 0
    penalties = 0
    total_questions = 26

    st.header("📝 Quiz Vragen")
    st.write("Beantwoord elke vraag zo goed mogelijk! 🌟")
    progress = st.progress(0)

    # Vragenlijst
    vragen = [
        {"vraag": "Geef het volgende gerecht een score op 10: gehakt met kriek", "antwoord": "5"},
        {"vraag": "Geef de eerste letter van de naam die mijn kat had.", "antwoord": "s"},
        {"vraag": "Geef de afkorting van mijn studierichting in kleine letters.", "antwoord": "iot"},
        {"vraag": "Wat is mijn lievelingsdier?", "antwoord": "pinguin"},
        {"vraag": "Welke voetbalclub is koning: Bayer Leverkusen of Bayern München?", "antwoord": "bayern münchen"},
        {"vraag": "Waar of niet waar: Ik ben tijdens een wilde zuipnacht in het ziekenhuis beland om mijn maag te laten leegpompen.", "antwoord": "niet waar"},
        {"vraag": "Raadsel: Degene die het maakt, gebruikt het niet. Degene die het koopt, wil het niet en degene die het gebruikt, weet het niet. Wat is het?", "antwoord": "doodskist"},
        {"vraag": "Waar of niet waar: Ik ben ooit eens naar de spoed geweest voor een splinter.", "antwoord": "waar"},
        {"vraag": "Rangschik deze pilsies van beste naar slechtste: 1: Maes, 2: Jupiler, 3: Stella, 4: Cristal, 5: Vedett, 6: Primus (bijv. 145623)", "antwoord": "351246"},
        {"vraag": "De Vikingen hadden een groot deel van Engeland kunnen veroveren, maar welke stad was voor hun de absolute hoofdprijs?", "antwoord": "parijs"},
        {"vraag": "Welke kleur krijg je bij het mengen van rood en groen?", "antwoord": "geel"},
        {"vraag": "Wat is mijn lievelingskleur?", "antwoord": "rood"},
        {"vraag": "Welke zus staat bekend om het uitvoeren van 'De worm'?", "antwoord": "jana"},
        {"vraag": "Waar zou ik je naartoe nemen tijdens onze huwelijksreis? A: Costa Rica, B: Hawaï, C: Cuba", "antwoord": "a"},
        {"vraag": "Ronaldo of Messi?", "antwoord": "ronaldo"},
        {"vraag": "Wat hoort er volgens mij niet in het rijtje: A: Ananas op pizza, B: Meloen met hesp, C: vlees met kriek.", "antwoord": "c"},
        {"vraag": "Welke sport heb ik niet uitgeoefend: Volleybal, Turnen, Kickboks, Basketbal, Paardrijden", "antwoord": "volleybal"},
        {"vraag": "Met welk dier zou ik ons Kirsten vergelijken: A: Konijn, B: Eekhoorn, C: Alpaca.", "antwoord": "b"},
        {"vraag": "Vul het ontbrekende woord in bij deze songtekst: 'Now if I wrote you a love note And made you smile at every word I wrote (What would you do?) Would that make you wanna change your scene And wanna be the one on my .....?'", "antwoord": "team"},
        {"vraag": "Het lied in de vorige vraag wordt gezongen door één van mijn favoriete artiesten. Wie is het?", "antwoord": "justin timberlake"},
        {"vraag": "Met wat speelde ik als klein manneke het meest: A: Lego, B: Action Man, C: Playmobil.", "antwoord": "a"},
        {"vraag": "Welke gebeurtenis heeft mij NIET doen bleiten: A: de film Titanic, B: Duitsland wint WK, C: Doos Pokémon kaarten gestolen", "antwoord": "b"},
        {"vraag": "Doorzetting, Zelfstandigheid en positiviteit zijn dingen die ik bewonder aan jou, maar door welke ben ik echt voor jou gevallen?", "antwoord": "positiviteit"},
        {"vraag": "Waar of niet waar: eerst melk dan pas cornflakes is my way.", "antwoord": "niet waar"},
        {"vraag": "Welke is niet waar: 1=Ik verzamelde vroeger sigarettenpeuken, 2=Ik eet het plastic dat rond kaas hangt, 3=Tot mijn 17e dacht ik dat de radio het echt over vallende sterren had in plaats van flitspalen.", "antwoord": "1"}
    ]

    # Verwerking van antwoorden
    for i, vraag_info in enumerate(vragen):
        antwoord = st.text_input(f"{i + 1}. {vraag_info['vraag']}")
        if antwoord:
            if antwoord.strip().lower() == vraag_info['antwoord']:
                score += 4
            else:
                penalties += 1
        progress.progress((i + 1) / total_questions)

    if st.button("Bekijk Resultaat"):
        eindscore = max(0, score - (penalties * 2))  # Eindscore berekenen
        toon_resultaat(eindscore)

# Functie voor het tonen van het resultaat
def toon_resultaat(score):
    st.subheader("🎯 Je Quiz Resultaten 🎯")
    st.write(f"Je hebt een score van **{score}%** behaald!")
    
    if score <= 50:
        st.write("😢 Oei, dat was niet je beste poging! Blijf proberen!")
        st.progress(50)
        st.image("https://i.imgur.com/sRzIn8G.png", use_column_width=True)  # Vervang met een eigen URL
    elif 50 < score <= 65:
        st.write("🤔 Goed geprobeerd! Bijna daar!")
        st.progress(65)
        st.image("https://i.imgur.com/2fC6u6A.png", use_column_width=True)  # Vervang met een eigen URL
    else:
        st.write("❤️ Super gedaan! Je kent me goed!")
        st.snow()
        st.progress(100)
        st.image("https://i.imgur.com/5KXSoCp.png", use_column_width=True)  # Vervang met een eigen URL

    # Knop om antwoorden te bekijken
    if st.button("Bekijk Antwoorden"):
        toon_antwoorden()

# Functie om een overzicht van antwoorden te tonen
def toon_antwoorden():
    st.write("### Overzicht van jouw antwoorden:")
    vragen = [
        ("Geef het volgende gerecht een score op 10: gehakt met kriek", "5"),
        ("Geef de eerste letter van de naam die mijn kat had.", "s"),
        ("Geef de afkorting van mijn studierichting in kleine letters.", "iot"),
        ("Wat is mijn lievelingsdier?", "pinguin"),
        ("Welke voetbalclub is koning?", "Bayern München"),
        ("Waar of niet waar: Ik ben tijdens een wilde zuipnacht in het ziekenhuis beland om mijn maag te laten leegpompen.", "niet waar"),
        ("Raadsel: Degene die het maakt, gebruikt het niet...", "doodskist"),
        # Voeg alle overige vragen toe met juiste antwoorden
    ]
    
    for i, (vraag, antwoord) in enumerate(vragen, start=1):
        st.write(f"**Vraag {i}:** {vraag}")
        st.write(f"Correct antwoord: **{antwoord}**")
        st.write("---")

# Start de applicatie
if intro():
    quiz()
