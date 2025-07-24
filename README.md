# 📄 Resume Parser & Job Title Recommender

This project is a smart resume parser and job title recommender that extracts key details (like name, email, phone, and skills) from a resume PDF and matches them to the most relevant job titles based on skill similarity.

> ✅ Built with real-world freelance use cases in mind (HR tools, applicant tracking systems, etc.)

---

## 🚀 Features

- 🔍 **Resume Parsing** from PDF (name, email, phone, skills)
- 🤖 **Skill Matching** with job title profiles
- 💼 **Job Title Recommendation** using fuzzy skill comparison
- 📦 Clean modular code: easy to integrate with web dashboards or ATS

---

## 🛠 Tech Stack

- Python 3
- `pdfplumber` – extract text from PDF
- `spaCy` – NLP for name recognition
- `fuzzywuzzy` – fuzzy string matching
- JSON for job profiles and output data

---

## 📁 Project Structure

```

resume-parser-project/
│
├── main.py              # Main entry point
├── parser.py            # Resume parsing logic
├── recommender.py       # Job matching logic
├── job_titles.json      # Job roles and required skills
├── output.json          # Example parsed output
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
└── .gitignore           # Git ignore rules for Python projects

````

---

## 📌 How to Use

1. ✅ Install requirements:

```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
```

2. 📄 Place your resume PDF as `sample_resume.pdf`

3. ▶️ Run the project:

   ```bash
   python main.py
   ```

4. 📤 Output is shown in console and saved to `output.json`.

---

## 📊 Sample Output

```
🔍 Resume Analysis Result:
Name: Name: Hadi Dadashzade
Email: hadi@example.com
Phone: +98 923 456 789
Skills: ['Python', 'SQL']

💼 Recommended Job Titles:
Backend Developer (50% match)
Data Analyst (50% match)
AI Engineer (25% match)
```

---

## 💡 Use Cases

* Freelance tools for HR and recruitment
* AI-powered applicant screening
* Resume sorting by relevance
* Educational / portfolio project for AI + Python

---

## 🧠 Author

> Hadi Dadashzade — Python Developer | AI Enthusiast
> 🔗 [GitHub Profile](https://github.com/hadidadashzade)

---

## 🗂 License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for more details.
