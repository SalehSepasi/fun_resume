# 📄 Fun Resume Generator

> Turn a boring resume into something unforgettable. 😎

**Fun Resume Generator** is a Streamlit web application that uses AI to generate creative, humorous, and personalized resumes from simple user information.

Instead of creating another serious and boring CV, this project turns your personality, skills, hobbies, and background into a fun resume.

---

## ✨ Features

* 📝 Collect basic personal information
* 🤖 Generate a personalized resume using an LLM
* 😂 Create humorous and creative resume content
* 🎭 Customize the resume based on personality
* 🌐 Simple and interactive Streamlit interface

### Coming Soon

* 🖼️ AI-powered profile picture transformation
* 🎨 Multiple resume themes
* 🎭 Different personality styles
* 🔥 Roast level customization
* 📑 Generate a formatted PDF
* 🧑‍💼 Different resume templates

---

## 🖥️ Demo

The application allows users to enter information such as:

* Name
* Job or major
* Age
* Skills
* Hobbies
* Personality

The information is then sent to an AI model, which generates a creative resume based on the user's personality.

---

## 🛠️ Tech Stack

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| 🐍 Python        | Core programming language       |
| 🎈 Streamlit     | Web application and UI          |
| 🤖 OpenRouter    | LLM API                         |
| 🔧 Git & GitHub  | Version control                 |

---

## 📁 Project Structure

```text
fun_resume/
│
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
└── src/
    ├── main.py
    ├── llm.py
    └── resume_generator.py
```

### File Responsibilities

**`main.py`**

Handles the Streamlit user interface and connects the different parts of the application.

**`llm.py`**

Handles communication with the LLM API through OpenRouter.

**`resume_generator.py`**

Builds the prompt and generates the fun resume content.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SalehSepasi/fun_resume.git
cd fun_resume
```

### 2. Create a Python environment

Using Conda:

```bash
conda create -n fun_resume python=3.13
conda activate fun_resume
```

Or using `venv`:

```bash
python -m venv .venv
```

Activate it on Linux/WSL:

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure the API key

Create a `.env` file in the project root:

```text
OPENROUTER_API_KEY=your_api_key_here
```

You can get an API key from OpenRouter.

**Never commit your `.env` file or expose your API key publicly.**

The project already ignores `.env` through `.gitignore`.

---

### 5. Run the application

```bash
streamlit run src/main.py
```

Streamlit will start the application locally.

---

## 🔐 Environment Variables

The application uses the following environment variable:

| Variable             | Description                    |
| -------------------- | ------------------------------ |
| `OPENROUTER_API_KEY` | API key used to access the LLM |

Example:

```text
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxx
```

---

## 🧠 How It Works

The application follows a simple pipeline:

```text
                 User Input
                     │
                     ▼
              Streamlit Interface
                     │
                     ▼
             Prompt Construction
                     │
                     ▼
                OpenRouter
                     │
                     ▼
                LLM Response
                     │
                     ▼
              Resume Generator
                     │
                     ▼
        Display the Generated resume

```

The project intentionally keeps the responsibilities separated so that each component can be developed and improved independently.

---

## 🤝 Contributing

Contributions, ideas, and improvements are welcome.

If you have an idea for a funny resume style, template, or feature, feel free to open an issue or submit a pull request.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## ⭐ If You Like It

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

And remember:

> **Your resume doesn't have to be boring.** 😎
