import numpy as np
import pandas as pd
import streamlit as st
import food_recomm
import ingredients
import recipe_finder

from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="HAA",
    page_icon='🍕',
    layout='wide'
)

@st.cache_data()
def fetch_and_clean_data(file_path):
    df = pd.read_csv(file_path)

    # get all items
    items = set()
    for x in df.ingredients:
        for val in x.split(', '):
            items.add(val.lower().strip())

    # create new dataframe
    new_df = pd.DataFrame(data=np.zeros((len(df), 2 + len(items)), dtype=int), columns=['name', 'ingredients'] + list(items))

    for i, d in df.iterrows():
        new_df.loc[i, ['name', 'ingredients']] = d[:2]
        for val in d[1].split(', '):
            item = val.lower().strip()
            new_df.loc[i, item] = 1

    return new_df


data = fetch_and_clean_data('data/food_250.csv')

# --- TOP NAVBAR ---
selected = option_menu(
    menu_title=None,
    options=["Home", "About", "Menu", "Contact Us", "Recipe Finder", "Recommender", "Ingredients"],
    icons=["house", "info-circle", "list", "envelope", "search", "heart", "egg-fried"],
    orientation="horizontal"
)

# --- PAGE ROUTING ---
if selected == "Home":
    st.title("🍽️ Welcome to the Food & Recipe Recommendation System")
    st.markdown("---")

    # Intro Section
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #FF6F91, #FF9671); padding: 30px; border-radius: 15px; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
            <h2 style="font-weight: 900;">Your Ultimate Smart Cooking Assistant</h2>
            <p style="font-size: 18px; line-height: 1.6;">
                Discover personalized recipes, get smart meal recommendations, and cook delicious meals with the ingredients you already have. Whether you're a busy professional, a passionate home cook, or someone with specific dietary needs, our app is designed to make your cooking effortless and enjoyable.
            </p>
            <img src="https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=800&q=80" style="width: 100%; max-height: 300px; object-fit: cover; border-radius: 12px; margin-top: 15px;">
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # Key Features Section with background
    st.markdown(
        """
        <div style="background-color: #FFF5F5; padding: 25px; border-radius: 15px;">
            <h3 style="color: #FF4B4B; font-weight: 800; border-bottom: 3px solid #FF4B4B; padding-bottom: 5px;">🌟 Key Features</h3>
            <ul style="font-size: 18px; color: #333; line-height: 1.7;">
                <li><strong>Ingredient-based Search:</strong> Easily find recipes using what you have in your pantry.</li>
                <li><strong>Smart Recommendations:</strong> Machine learning powered suggestions tailored to your taste and dietary preferences.</li>
                <li><strong>Diet Filters:</strong> Vegan, gluten-free, keto and more — customized meal planning for your lifestyle.</li>
                <li><strong>Nutritional Info:</strong> Detailed calorie counts and macro breakdowns for healthier eating.</li>
                <li><strong>User-Friendly Interface:</strong> Intuitive design so you can find, cook, and enjoy without hassle.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # How it works
    st.markdown(
        """
        <div style="background-color: #FFF5F5; padding: 25px; border-radius: 15px; margin-top: 30px;">
            <h3 style="color: #FF4B4B; font-weight: 700;">🔍 How It Works</h3>
            <ol style="font-size: 18px; color: #444; line-height: 2;">
                <li><strong>Input Ingredients:</strong> Tell us what you have in your kitchen.</li>
                <li><strong>Get Recipe Matches:</strong> Our algorithms find recipes you can make right now.</li>
                <li><strong>Apply Filters:</strong> Choose dietary restrictions or cuisine types.</li>
                <li><strong>Explore Nutrition:</strong> See detailed nutrition and cooking instructions.</li>
                <li><strong>Cook & Enjoy:</strong> Follow the steps and savor your meal!</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Why Choose Us section with background
    st.markdown(
        """
        <div style="background-color: #FFF5F5; padding: 25px; border-radius: 15px; margin-top: 30px;">
            <h3 style="color: #FF4B4B; font-weight: 800; border-bottom: 3px solid #FF4B4B; padding-bottom: 5px;">🎯 Why Choose Our App?</h3>
            <ul style="font-size: 18px; color: #333; line-height: 1.7;">
                <li><strong>Save Time & Reduce Waste:</strong> Use what you have, no last-minute grocery runs.</li>
                <li><strong>Stay Healthy:</strong> Make informed decisions with nutrition data.</li>
                <li><strong>Expand Your Palate:</strong> Try new recipes personalized to your tastes.</li>
                <li><strong>Support Sustainability:</strong> Minimize food waste and cook responsibly.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Technologies Section
    st.markdown(
        """
        <div style="background-color: #FFF5F5; padding: 25px; border-radius: 15px; margin-top: 30px;">
            <h3 style="color: #FF4B4B; font-weight: 700;">🔧 Technologies Behind The Scenes</h3>
            <p style="font-size: 18px; color: #444;">
                Our app leverages cutting-edge technologies to deliver a seamless and intelligent cooking experience:
            </p>
            <ul style="font-size: 18px; color: #333; line-height: 1.7;">
                <li><strong>Python & Streamlit:</strong> Powering the interactive, user-friendly interface.</li>
                <li><strong>Machine Learning:</strong> Personalized recipe recommendations using content-based filtering and NLP.</li>
                <li><strong>Data Science:</strong> Pandas & NumPy for processing recipe and nutritional data efficiently.</li>
                <li><strong>Cloud Hosting:</strong> Scalable infrastructure for smooth user experience anytime, anywhere.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Call to action
    st.markdown(
        """
        <div style="text-align:center; margin-top: 40px; padding: 30px; background: linear-gradient(90deg, #FF4B4B, #FF9671); border-radius: 20px; color: white; font-size: 22px; font-weight: 700; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;">
            Ready to elevate your cooking? Use the <strong>Recipe Finder</strong> or <strong>Food Recommender</strong> from the menu above and start cooking smarter today! 🍳🍽️
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Contact Section
    st.markdown(
        """
        <div style="background-color: #1a1a1a; padding: 30px; border-radius: 15px; margin-top: 40px;">
            <h3 style="color: #FF4B4B; font-weight: 800;">📞 Contact Us</h3>
            <p style="font-size: 18px; color: #eee; line-height: 1.8;">
                We'd love to hear from you! Whether it's feedback, questions, or collaborations, reach out anytime.
                <br><br>
                📧 Email: foodapp@example.com  
                🌐 Website: www.smartfoodie.ai  
                📍 Location: New York, USA
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


elif selected == "About":
    st.title("🍽️ Food & Recipe Recommendation System")
    st.markdown("---")

    # Create two columns: left text (65%), right images (35%)
    col1, col2 = st.columns([65, 35])

    with col1:
        st.header("Welcome to Your Smart Cooking Assistant")
        st.write(
            """
            Our **Food & Recipe Recommendation System** is designed to revolutionize your cooking experience by offering personalized recipe suggestions based on the ingredients you have at hand and your dietary preferences.

            Whether you're a busy professional, a home cook, or someone managing specific dietary restrictions, this app is here to simplify meal planning and make cooking enjoyable and efficient.
            """
        )

        st.subheader("🔍 How It Works")
        st.write(
            """
            - Enter the ingredients available in your kitchen.
            - Our system uses **advanced machine learning algorithms** to find recipes that match your ingredients.
            - Filter recipes based on dietary preferences like vegan, gluten-free, or keto.
            - View detailed nutritional information to make healthier choices.
            """
        )

        st.subheader("🎯 Who Is This For?")
        st.write(
            """
            - Home cooks looking for new meal inspirations.
            - People managing food allergies or special diets.
            - Anyone wanting to minimize food waste by cooking with what's available.
            - Food enthusiasts interested in combining technology and cooking.
            """
        )

        st.subheader("🌱 Our Mission")
        st.write(
            """
            To empower individuals to cook smarter, healthier meals with ease — reducing food waste and making nutritious cooking accessible to all.
            """
        )

        # NEW additional paragraphs for more detail & style
        st.markdown(
            """
            ### Why Choose Our System?

            Cooking can be time-consuming and overwhelming, especially when you’re unsure what to make with the ingredients you have. Our system **simplifies meal planning** by offering you quick, personalized recipe ideas that save you time and money. Plus, by suggesting recipes tailored to your pantry, we help you reduce food waste — a win for your wallet and the environment! 🌍

            ### Personalized & Adaptive

            Unlike generic recipe sites, our recommendation engine learns from your preferences and adapts over time. Whether you want to try new cuisines, eat healthier, or cater to specific dietary restrictions, our system evolves with you. This makes your cooking journey more enjoyable and uniquely yours. 🎉

            ### Designed With You In Mind

            We believe that cooking should be accessible and fun. That’s why we focused on creating an interface that is **clean, intuitive, and responsive** — so you can focus on what matters most: creating delicious meals and sharing them with your loved ones. ❤️
            """
        )

        st.subheader("🔧 Technologies Used")
        st.write(
            """
            - **Python** and **Streamlit** for building the user interface.
            - **Pandas** and **NumPy** for efficient data processing.
            - Machine Learning models including content-based filtering and natural language processing (NLP).
            - Curated datasets of recipes and nutrition facts.
            """
        )

        st.markdown(
            """
            > *"Cook smart, eat well, waste less."*  — Your Food & Recipe Recommendation System
            """
        )

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80",
            caption="Fresh, healthy meals",
           use_container_width=True,
        )
        st.image(
            "https://images.unsplash.com/photo-1490645935967-10de6ba17061?auto=format&fit=crop&w=600&q=80",
            caption="Smart recipe recommendations",
           use_container_width=True,
        )
        st.image(
            "https://images.unsplash.com/photo-1600891964599-f61ba0e24092?auto=format&fit=crop&w=600&q=80",
            caption="Fresh ingredients ready to cook",
           use_container_width=True,
        )
        
elif selected == "Menu":
    st.title("📋 Menu")
    st.markdown("---")

    # Professional Menu Introduction
    st.markdown(
        """
        <div style='background-color: #FFF5F5; padding: 20px; border-radius: 8px; margin-bottom: 20px;'>
            <h3 style='color: #FF4B4B; font-weight: 700;'>Our Menu – Crafted to Delight Your Taste Buds</h3>
            <p style='font-size: 18px; color: #333; line-height: 1.6;'>
                Dive into our thoughtfully curated selection of dishes, each created to bring joy, nutrition, and convenience to your kitchen. Whether you're craving vibrant salads, hearty mains, or decadent desserts, our menu offers diverse options tailored for every palate and occasion.
            </p>
            <p style='font-size: 16px; color: #555; line-height: 1.5; font-style: italic;'>
                All dishes are paired with fresh, high-quality ingredients and designed to complement our intelligent recipe recommendations. Explore and find inspiration for your next delicious meal!
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    menu_items = [
        {
            "name": "🥗 Fresh Garden Salad",
            "desc": "A vibrant mix of crisp lettuce, tomatoes, cucumbers, and a light vinaigrette dressing — healthy and refreshing.",
            "img": "https://images.unsplash.com/photo-1568605114967-8130f3a36994?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "🍝 Classic Spaghetti Bolognese",
            "desc": "Rich, meaty tomato sauce served over al dente spaghetti noodles — a timeless Italian favorite.",
            "img": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "🍣 Sushi Platter",
            "desc": "Assortment of fresh nigiri and rolls accompanied by wasabi and pickled ginger — elegant and delicious.",
            "img": "https://images.unsplash.com/photo-1553621042-f6e147245754?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "🍛 Chicken Curry",
            "desc": "Spicy and creamy chicken curry simmered with aromatic spices and coconut milk — bursting with flavor.",
            "img": "https://images.unsplash.com/photo-1627308595229-7830a5c91f9f?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "🥖 Artisan Bread Basket",
            "desc": "Freshly baked crusty bread, perfect for dipping and pairing with your favorite meals.",
            "img": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=400&q=80"
        },
        {
            "name": "🍰 Chocolate Lava Cake",
            "desc": "Warm chocolate cake with a molten center served with vanilla ice cream — a decadent dessert.",
            "img": "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=400&q=80"
        },
    ]

    num_cols = 3
    rows = (len(menu_items) + num_cols - 1) // num_cols

    for row in range(rows):
        cols = st.columns(num_cols)
        for idx in range(num_cols):
            item_idx = row * num_cols + idx
            if item_idx < len(menu_items):
                item = menu_items[item_idx]
                with cols[idx]:
                    # Fixed container with image on top, then name and description in white bold text on dark background
                    st.markdown(
                        f"""
                        <div style='
                            background-color: #222;
                            border-radius: 10px;
                            padding: 15px;
                            height: 420px;
                            display: flex;
                            flex-direction: column;
                            justify-content: flex-start;
                            align-items: center;
                            text-align: center;
                            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                        '>
                            <img src="{item['img']}" alt="{item['name']}" style='
                                width: 280px;
                                height: 240px;
                                object-fit: cover;
                                border-radius: 10px;
                                margin-bottom: 15px;
                            ' />
                            <h3 style='
                                color: white;
                                font-weight: 900;
                                margin: 0 0 10px 0;
                                font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
                            '>{item['name']}</h3>
                            <p style='
                                color: white;
                                font-weight: 700;
                                font-size: 14px;
                                margin: 0 10px;
                                font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
                            '>{item['desc']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.write("")

    st.markdown("---")
    st.markdown(
        "💡 *Tip:* Use the **Recipe Finder** feature to get detailed cooking steps and nutritional info for each dish!"
    )


elif selected == "Contact Us":
    st.title("📞 Contact Us")
    st.markdown("---")

    st.markdown(
        """
        <div style='background-color: #FFF5F5; padding: 25px; border-radius: 10px; max-width: 700px; margin-bottom: 30px;'>
            <h3 style='color: #FF4B4B; font-weight: 700; margin-bottom: 10px;'>We'd love to hear from you!</h3>
            <p style='font-size: 18px; color: #333; line-height: 1.6;'>
                Whether you have questions, feedback, or want to suggest new features, feel free to get in touch. Our team is here to help you cook smarter and better every day.
            </p>
            <p style='font-size: 16px; color: #555;'>
                📧 Email us directly at: <a href="mailto:foodapp@example.com" style="color:#FF4B4B; font-weight:bold;">foodapp@example.com</a><br>
                📞 Call us at: <span style="color:#FF4B4B; font-weight:bold;">+1 (555) 123-4567</span><br>
                🌐 Visit our website: <a href="https://yourfoodapp.com" target="_blank" style="color:#FF4B4B; font-weight:bold;">yourfoodapp.com</a>
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("Send Us a Message")

    with st.form(key='contact_form'):
        name = st.text_input("Your Name", max_chars=50)
        email = st.text_input("Your Email", max_chars=50)
        message = st.text_area("Your Message", height=150, max_chars=500)
        submit_button = st.form_submit_button(label='Send Message')

        if submit_button:
            if name and email and message:
                st.success(f"Thank you, **{name}**! Your message has been received. We'll get back to you soon.")
                # Here, you could add logic to send the message via email or store it
            else:
                st.error("Please fill out all fields before submitting.")


elif selected == "Recipe Finder":
    recipe_finder.app(data)

elif selected == "Recommender":
    food_recomm.app(data)
    
elif selected == "Ingredients":
    ingredients.app(data)
