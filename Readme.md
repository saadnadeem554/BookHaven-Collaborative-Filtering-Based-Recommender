# 📚 Flask Book Recommendation App

Welcome to **Flask Book Recommendation App** — a web application that recommends books to users based on their interests.
Built with **Flask**, **Pickle**, and a trained similarity model.

---

## 🚀 Features

- Display **popular books** based on ratings and popularity.
- Recommend **similar books** when a user selects a title.
- Interactive, simple, and elegant UI with Flask templates.
- Pre-trained recommendation engine using **collaborative filtering**.
- Easy to deploy and lightweight.

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **Data Storage:** Pickle files (`popular.pkl`, `pt.pkl`, `books.pkl`, `similarity_score.pkl`)
- **Frontend:** HTML, CSS (Flask `templates` and `static` folders)
- **Deployment:** PythonAnywhere / GitHub

---

## 📂 Project Structure

```bash
├── app.py              # Main Flask application
├── books.pkl           # Book information dataset
├── popular.pkl         # Popular books dataset
├── pt.pkl              # Pivot table for recommendations
├── similarity_score.pkl# Precomputed similarity scores
├── templates/
│   ├── index.html      # Homepage
│   └── recommend.html  # Recommendation results
└── static/
    └── styles.css      # Custom CSS (if any)
```

---

## ⚡ How to Run Locally

1. **Clone the repository:**

2. **Install required packages:**
   ```bash
   pip install flask
   ```

3. **Run the app:**
   ```bash
   flask run
   ```

4. **Visit in browser:**  
   Open `http://127.0.0.1:5000/` to see the app.

---

## 🌐 Live Demo

> Deployed on: [PythonAnywhere](https://saadnadeem.pythonanywhere.com/)

---

## 🙏 Acknowledgements

- Thanks to the **Kaggle** for the providing the dataset used for training.
- Special credit to Flask's simplicity for rapid development.

---

## 📜 License

This project is open source and free to use.  
Built with ♥ by Saad.
