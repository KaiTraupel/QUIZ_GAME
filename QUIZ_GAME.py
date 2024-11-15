import streamlit as st
import time

# Instellingen voor de kleurrijke stijl en achtergrondafbeelding
st.set_page_config(page_title="KaiHarde Quiz Game", page_icon="🎉", layout="centered")

st.markdown(
    f"""
    <style>
    html, body, .stApp {{
        background: url("https://i.imgur.com/OvK6DFY.png");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}
    .title {{
        font-size: 3em; 
        color: #FFD700;
        text-align: center;
        font-weight: bold;
        font-family: 'Raleway', sans-serif;
    }}
    .subtitle {{
        font-size: 2em;
        color: #000000;
        text-align: center;
        font-weight: bold;
        font-family: 'Raleway', sans-serif;
    }}
    .question {{
        font-size: 2em;
        color: #FFD700;
        font-weight: bold;
        font-family: 'Raleway', sans-serif;
        padding: 10px;
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Initialiseer sessievariabelen
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "penalties" not in st.session_state:
    st.session_state.penalties = 0
if "vraag_index" not in st.session_state:
    st.session_state.vraag_index = 0

# Functie voor het startmenu
def start_menu():
    st.markdown("<div class='title'>🎉 Welkom bij de KaiHarde Quiz! 🎉</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Is zien of gij wel naar mij luistert hehe!</div>", unsafe_allow_html=True)
    st.markdown("##")
    st.markdown(
        """
        **SPELREGELS:**
        - Antwoorden zijn niet hoofdlettergevoelig.
        - Voor vragen met opties hoef je alleen de letter of het nummer te geven.
        - Het opzoeken van antwoorden is natuurlijk verboden dus daaarft ni! 😜
        - Juist = +4
        - Fout = -2
        """
    )
    start = st.button("🚀 Start de Quiz", key="start_button")
    if start:
        st.session_state.quiz_started = True  # Vlag om aan te geven dat de quiz gestart is
    
# Functie om de quizvragen een voor een te tonen
def quiz():
    vragen = [
        {"vraag": "Met het volgende gerecht trekt oep niks: ja / nee: gehakt met kriek", "antwoord": "nee"},
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
    
    totaal_vragen = len(vragen)
    huidige_vraag_index = st.session_state.vraag_index

    if huidige_vraag_index < totaal_vragen:
        vraag_info = vragen[huidige_vraag_index]
        st.markdown(f"<div class='subtitle'>Vraag {huidige_vraag_index + 1} van {totaal_vragen}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='question'>{vraag_info['vraag']}</div>", unsafe_allow_html=True)

        antwoord = st.text_input("Jouw antwoord:", key=f"antwoord_{huidige_vraag_index}")
        
        if st.button("Volgende"):
            if antwoord.strip().lower() == vraag_info['antwoord']:
                st.session_state.score += 4
            else:
                st.session_state.penalties += 1
            st.session_state.vraag_index += 1  # Ga naar de volgende vraag
    else:
        toon_resultaat(st.session_state.score, st.session_state.penalties, totaal_vragen)


# Functie voor de eindresultaten
def toon_resultaat(score, penalties, totaal_vragen):
    st.markdown("<div class='title'>🎉 Je Quiz Resultaten 🎉</div>", unsafe_allow_html=True)
    eindscore = max(0, score - (penalties * 2))

    st.write(f"Je hebt **{score // 4} van de {totaal_vragen} vragen** correct beantwoord.")
    st.write(f"Je eindscore is: **{eindscore}%**")

    if eindscore <= 50:
        st.markdown("<div class='subtitle'>😢 Slechte score! Probeer het nog eens!</div>", unsafe_allow_html=True)
    elif 50 < eindscore <= 65:
        st.markdown("<div class='subtitle'>🤔 Goed geprobeerd! Nog iets beter kan wel!</div>", unsafe_allow_html=True)
    else:
        st.markdown("<div class='subtitle'>❤️ Uitstekend! Je kent me goed!</div>", unsafe_allow_html=True)

    if st.button("Opnieuw Spelen"):
        st.session_state.quiz_started = False
        st.session_state.vraag_index = 0
        st.session_state.score = 0
        st.session_state.penalties = 0
        st.experimental_rerun()

# Start de quiz vanuit het startmenu of ga verder met de quiz als deze al gestart is
if not st.session_state.quiz_started:
    start_menu()
else:
    quiz()
