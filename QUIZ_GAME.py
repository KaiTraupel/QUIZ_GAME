import streamlit as st
import time

# Instellingen voor de kleurrijke stijl
st.set_page_config(page_title="Disco Dans Knikkers Quiz", page_icon="🎉", layout="centered")
st.markdown(
    """
    <style>
    .title {
        font-size: 3em; 
        color: #FF6F61;
        text-align: center;
        font-weight: bold;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .subtitle {
        font-size: 1.5em;
        color: #4C72B0;
        text-align: center;
        font-weight: bold;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .question {
        font-size: 1.2em;
        color: #2B8EAD;
        font-weight: bold;
        font-family: 'Comic Sans MS', cursive, sans-serif;
        padding: 10px;
        text-align: center;
    }
    .button {
        background-color: #FF6F61;
        color: white;
        font-size: 1.2em;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Functie voor het startmenu
def start_menu():
    st.markdown("<div class='title'>🎉 Welkom bij de Disco Dans Knikkers Quiz! 🎉</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Test je kennis en ontdek hoeveel je over mij weet!</div>", unsafe_allow_html=True)
    st.markdown("##")
    st.markdown(
        """
        **Spelregels:**
        - Antwoorden zijn niet hoofdlettergevoelig.
        - Voor vragen met opties hoef je alleen de letter of het nummer te geven.
        - Het opzoeken van antwoorden is natuurlijk verboden! 😜
        """
    )
    start = st.button("🚀 Start de Quiz", key="start_button")
    return start
# Functie om de quizvragen een voor een te tonen
def quiz():
    vragen = [
        {"vraag": "Geef het volgende gerecht een score op 10: gehakt met kriek", "antwoord": "5"},
        {"vraag": "Geef de eerste letter van de naam die mijn kat had.", "antwoord": "s"},
        {"vraag": "Geef de afkorting van mijn studierichting in kleine letters.", "antwoord": "iot"},
        {"vraag": "Wat is mijn lievelingsdier?", "antwoord": "pinguin"},
        {"vraag": "Welke voetbalclub is koning: Bayer Leverkusen of Bayern München?", "antwoord": "bayern münchen"},
        # Voeg meer vragen toe zoals gewenst...
    ]
    
    # Instellingen voor de score
    score = 0
    penalties = 0
    totaal_vragen = len(vragen)
    huidige_vraag_index = st.session_state.get("vraag_index", 0)

    if huidige_vraag_index < totaal_vragen:
        vraag_info = vragen[huidige_vraag_index]
        st.markdown(f"<div class='subtitle'>Vraag {huidige_vraag_index + 1} van {totaal_vragen}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='question'>{vraag_info['vraag']}</div>", unsafe_allow_html=True)

        antwoord = st.text_input("Jouw antwoord:", key=f"antwoord_{huidige_vraag_index}")
        
        # Ga naar de volgende vraag
        if st.button("Volgende"):
            if antwoord.strip().lower() == vraag_info['antwoord']:
                score += 4
            else:
                penalties += 1
            st.session_state.vraag_index = huidige_vraag_index + 1
            st.session_state.score = score
            st.session_state.penalties = penalties
            st.experimental_rerun()
    else:
        # Toon de resultaten
        toon_resultaat(st.session_state.score, st.session_state.penalties, totaal_vragen)
# Functie voor de eindresultaten
def toon_resultaat(score, penalties, totaal_vragen):
    st.markdown("<div class='title'>🎉 Je Quiz Resultaten 🎉</div>", unsafe_allow_html=True)
    eindscore = max(0, score - (penalties * 2))  # Eindscore berekenen

    st.write(f"Je hebt **{score // 4} van de {totaal_vragen} vragen** correct beantwoord.")
    st.write(f"Je eindscore is: **{eindscore}%**")

    # Dynamische feedback op basis van score
    if eindscore <= 50:
        st.markdown("<div class='subtitle'>😢 Oei, dat was niet je beste poging! Probeer het nog eens!</div>", unsafe_allow_html=True)
        st.balloons()
    elif 50 < eindscore <= 65:
        st.markdown("<div class='subtitle'>🤔 Goed geprobeerd! Je was er bijna!</div>", unsafe_allow_html=True)
        st.snow()
    else:
        st.markdown("<div class='subtitle'>❤️ Super gedaan! Je kent me goed!</div>", unsafe_allow_html=True)
        st.snow()

    # Knop om opnieuw te spelen
    if st.button("Opnieuw Spelen"):
        st.session_state.vraag_index = 0
        st.session_state.score = 0
        st.session_state.penalties = 0
        st.experimental_rerun()
# Start de quiz vanuit het startmenu
if "vraag_index" not in st.session_state:
    st.session_state.vraag_index = 0
    st.session_state.score = 0
    st.session_state.penalties = 0

if start_menu():
    quiz()
