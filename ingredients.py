import streamlit as st
import time
import pandas as pd

data = pd.DataFrame({
    "Recipe Name": ["Pasta Carbonara", "Chicken Curry", "Veggie Stir Fry"],
    "Ingredients": [
        "Pasta, Eggs, Parmesan, Black Pepper, Bacon",
        "Chicken, Onion, Garlic, Curry Powder, Coconut Milk",
        "Broccoli, Bell Peppers, Soy Sauce, Garlic, Carrots"
    ]
})

# Renamed from show_ingredients_page to app
def app(data):
    st.title('🧂 Recipe Ingredients Explorer')
    
    st.image('./images/food_image.png', use_container_width=True)

    st.markdown(
        """
        <div style="background-color:#1f1f1f; padding:20px; border-radius:15px; color:white;">
            <h3>See what ingredients are needed for your favorite meals</h3>
            <p style="font-size:16px; line-height:1.6;">
                Just pick a recipe and instantly get the full list of ingredients you’ll need to prepare it.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected_foods = st.multiselect(
        label="🍽️ Select a recipe",
        options=data.iloc[:, 0].tolist()
    )

    show_button = st.button('Show Ingredients')

    if show_button:
        if not selected_foods:
            st.warning("⚠️ Please select at least one recipe.")
        else:
            st.markdown("<br>", unsafe_allow_html=True)
            st.header("📋 Ingredients List")

            for food in selected_foods:
                ingredients = data[data.iloc[:, 0] == food].iloc[0, 1]
                st.success(f"**{food}**")
                st.write(ingredients)
                st.markdown("---")

    # Hide Streamlit Footer and Menu
    st.markdown("""
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
