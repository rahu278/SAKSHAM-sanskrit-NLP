import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="SAKSHAM Sanskrit NLP",
    page_icon="📚",
    layout="centered"
)

st.title("📚 SAKSHAM - Sanskrit NLP")
st.subheader("Sanskrit Natural Language Processing")

st.write(
    "A basic Sanskrit NLP prototype using Python "
    "and dictionary-based word analysis."
)

# Sanskrit sample sentences
sentences = {
    "रामः पठति।": "Rama reads.",
    "बालकः गच्छति।": "Boy goes.",
    "रामः फलम् खादति।": "Rama eats fruit."
}

# Sanskrit word dictionary
dictionary = {
    "रामः": ["Rama", "Noun", "Karta (Subject)"],
    "पठति": ["Reads", "Verb", "Action"],
    "बालकः": ["Boy", "Noun", "Karta (Subject)"],
    "गच्छति": ["Goes", "Verb", "Action"],
    "फलम्": ["Fruit", "Noun", "Karma (Object)"],
    "खादति": ["Eats", "Verb", "Action"]
}

st.header("1. Select Sanskrit Sentence")

selected_sentence = st.selectbox(
    "Choose a sentence:",
    list(sentences.keys())
)

if st.button("Process Sentence"):

    st.header("2. English Translation")
    st.success(sentences[selected_sentence])

    # Tokenization
    st.header("3. Tokenization")

    words = selected_sentence.replace("।", "").split()
    st.write(words)

    # Word Analysis
    st.header("4. Word Analysis")

    result = []

    for word in words:
        if word in dictionary:
            meaning, word_type, role = dictionary[word]

            result.append({
                "Sanskrit Word": word,
                "English Meaning": meaning,
                "Word Type": word_type,
                "Grammatical Role": role
            })

    df = pd.DataFrame(result)
    st.dataframe(df, use_container_width=True)

    st.header("5. System Limitation")

    st.info(
        "Advanced Sandhi splitting is not implemented "
        "in this basic prototype."
    )

    st.success("Sentence processing completed!")

st.divider()

st.write("**Project:** SAKSHAM Sanskrit NLP")
st.write("**Developed by:** Rohit Kumar")
st.write("**Roll No.:** 65")