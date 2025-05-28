# 🍽️ Food and Recipe Recommender System

<p align="center">
  <b>🥗 AI Recommendations | 🍳 Personalized Recipes | 🧠 Machine Learning | 🍱 Nutrition-Aware</b><br><br>
  A smart recommendation engine that suggests food and recipes tailored to user preferences, dietary needs, and ingredient availability.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Recommendation-System-green">
  <img src="https://img.shields.io/badge/UI-Streamlit-orange?logo=streamlit">
  <img src="https://img.shields.io/badge/NLP-Transformers-brightgreen">
</p>

---

## 🍴 Project Overview

The **Food and Recipe Recommender System** leverages machine learning techniques to deliver:

* Personalized recipe recommendations
* Nutritional insights
* Cuisine and ingredient-based filters

Users can input their dietary preferences, allergies, or available ingredients to get relevant and delicious food suggestions.

---

## ✅ Features

* 🔍 Search recipes by ingredients or meal type
* 🍽️ Filter by dietary restrictions (vegan, gluten-free, etc.)
* 🤖 Generate personalized meal recommendations using collaborative filtering or NLP
* 📊 Display nutritional values (optional)
* 🌐 Simple and responsive UI with Streamlit

---

## 🗃️ Datasets Used

* 🧾 **Recipe1M+** (Yummly/Kaggle) – large-scale recipe dataset with ingredients, instructions, and images
* 🍎 **Food.com Recipes Dataset** – includes reviews, nutritional info, and ingredients

Optional sources:

* 🧠 User preference logs for collaborative filtering
* 🌍 OpenFoodFacts for nutritional data

---

## 🧠 Recommendation Techniques

1. **Content-Based Filtering**

   * Ingredients similarity
   * Cuisine preference

2. **Collaborative Filtering**

   * Matrix Factorization using user-recipe interactions

3. **NLP/Transformer Models**

   * Title/description embeddings (BERT)
   * Ingredient tagging and similarity

---

## ⚙️ Tech Stack

| Tool/Library      | Purpose                                     |
| ----------------- | ------------------------------------------- |
| 🐍 Python         | Core programming language                   |
| 📊 Pandas / NumPy | Data manipulation                           |
| 🤖 Scikit-learn   | ML algorithms for recommendation            |
| 🧠 NLP / BERT     | Text similarity for recipe search           |
| 🌐 Streamlit      | Web interface                               |
| 🍽️ Food APIs     | (Optional) External nutritional information |

---

## 🧪 Evaluation Metrics

* 🔢 **Precision\@K / Recall\@K** – relevance of top-K recommendations
* 📈 **Cosine Similarity** – content vector comparison
* 🧾 **User Satisfaction** – feedback or ratings (if collected)

---

## 💻 Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Aalyan-butt/Food---Recipe-Recommender-System
cd food-recommender
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the Application

```bash
streamlit run app/main.py
```

---

## 🔎 Example Usage

> **Input:** "I have chicken, garlic, and tomatoes. What can I cook?"
> **Output:** "Suggested Recipe: Garlic Butter Chicken with Tomato Salsa"

> **Input:** "I’m vegan and want a high-protein lunch."
> **Output:** "Recommended: Lentil Salad with Tofu and Avocado"

---

## 🚀 Future Enhancements

* [ ] Integrate image recognition to identify ingredients from photos
* [ ] Add meal planner and grocery list generation
* [ ] Improve personalization using deep learning models
* [ ] Connect with nutrition and fitness APIs

---



## 🙌 Acknowledgments

* Recipe1M+ Dataset creators
* Streamlit for easy UI deployment
* Kaggle and Food.com for open recipe data

---

## 👨‍🍳 Author

**Aalyan Riasat**
📧 [aalyanriasatali@gmail.com](mailto:your.email@example.com)
🔗  • [GitHub](https://github.com/Aalyan-butt)

---
