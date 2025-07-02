import streamlit as st
from googletrans import Translator
import pyperclip

# Page Title (centered)
st.markdown("<h1 style='text-align: center;'>🗺 TransLingu</h1>", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center;color:green'>Say it in Your Way </h4>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>AI-assisted translation</p>", unsafe_allow_html=True)

# Stylish Button Styling (affects all buttons)
st.markdown(
    """
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 45px;
        width: 200px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True
)


# Language Selection
languages= {
    "English": 'en',
    "Tamil": 'ta',
    "Hindi": 'hi',
    "French": 'fr',
    "German": 'de',
    "Spanish": 'es',
    "Telugu": 'te',
    "Japanese": 'ja',
    "Chinese": 'zh-CN',
    "Arabic": 'ar',
    "Russian": 'ru',
    "Korean": 'ko',
    "Portuguese": 'pt',
    "Urdu": 'ur',
    "Bengali": 'bn',
    "Italian": 'it',
    "Malay": 'ms',
    "Indonesian": 'id',
    "Turkish": 'tr',
    "Vietnamese": 'vi'
}


# Text input area
st.markdown("### ⌨ Enter Text to Translate:")
text_to_translate = st.text_area(" ", height=150)

# Language selection in columns
col1, col2 = st.columns(2)
source_lang = col1.selectbox("🌍 From Language", list(languages.keys()))
target_lang = col2.selectbox("🎯 To Language", list(languages.keys()))


translated_text = ""

# Translator Logic
if st.button("✍Translate"):
    if text_to_translate:
        translator = Translator()
        translation = translator.translate(text_to_translate, src=languages[source_lang], dest=languages[target_lang])
        translated_text = translation.text
        st.subheader("🔤 Translated Text:")
        st.write(translated_text)






# Reliable Copy Button
        import html
        import streamlit.components.v1 as components

        escaped_text = html.escape(translated_text)

        copy_html = f"""
        <div>
            <input type="text" value="{escaped_text}" id="translatedText" readonly style="opacity: 0; position: absolute; z-index: -10;">
            <button onclick="copyText()">📋 Copy to Clipboard</button>
        </div>
        <script>
             function copyText() {{
                         var copyText = document.getElementById("translatedText");
                         copyText.select();
                         document.execCommand("copy");
                         alert("✅ Copied to clipboard!");
                                  }}
        </script>
                 """

        components.html(copy_html, height=100)


    else:
        st.warning("Please enter some text to translate.")

# Clear button
if st.button("🔄 Clear"):
    st.rerun()

# Footer
st.markdown("---")