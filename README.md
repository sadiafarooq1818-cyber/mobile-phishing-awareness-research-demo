# Mobile Phishing Awareness Research Demo

**Proposed research title:** AI-Assisted Mobile Phishing Awareness and Detection: A Quantitative Evaluation of Microlearning Warnings for University Students

This repository supports a prospective Master by Research/MPhil application in Computer Science, Cybersecurity, Human-Centred Security, and Applied Machine Learning. It is designed as an early evidence package for supervisor outreach, showing that the proposed study is realistic, measurable, and technically feasible.

## Research problem

Mobile users are frequently exposed to phishing links through SMS, email, messaging applications, and social platforms. Many users make decisions quickly on small screens, where URL details, sender authenticity, and warning cues may be difficult to inspect. Although phishing detection models exist, there is still a practical gap between technical detection and user understanding. This project explores whether a simple AI-assisted detection layer combined with mobile-friendly microlearning warnings can improve user awareness and safer decision-making.

## Research aim

To design and quantitatively evaluate an AI-assisted mobile phishing awareness approach that combines a basic phishing URL classifier with short educational warning messages for mobile users.

## Research questions

1. Can a lightweight machine-learning classifier identify suspicious URLs using interpretable URL-based features?
2. Which URL features are most useful for explaining phishing risk to non-expert mobile users?
3. Can mobile-friendly warning cards and microlearning messages improve user recognition of phishing attempts?
4. How can technical detection results be translated into clear, human-centred cybersecurity guidance?

## Repository contents

```text
mobile-phishing-awareness-research-demo/
├── README.md
├── requirements.txt
├── data/
│   └── sample_urls.csv
├── notebooks/
│   └── phishing_url_classifier_demo.ipynb
├── docs/
│   ├── one_page_research_summary.md
│   ├── proposed_user_study.md
│   └── supervisor_email_template.md
└── mockups/
    └── warning_cards.md
```

## Methods overview

The technical demonstration uses a small sample URL dataset to show the planned workflow:

- URL feature extraction
- training a basic phishing classifier
- reporting accuracy, precision, recall, F1-score, and confusion matrix
- explaining how model output can be converted into mobile warning messages

The full research study would later use a larger public phishing URL dataset and a controlled user study with pre-test/post-test awareness scores.

## Planned quantitative analysis

The proposed study can use:

- descriptive statistics for awareness scores and user responses
- classifier metrics: accuracy, precision, recall, F1-score, ROC-AUC, confusion matrix
- paired t-test or Wilcoxon signed-rank test for pre/post awareness improvement
- regression or ANOVA to examine factors affecting phishing-recognition accuracy

## Current status

This is an early research demonstration repository. It is not a production phishing-detection tool. It is intended to support supervisor discussions, research proposal development, and scholarship applications.

## Candidate profile

**Applicant:** Sadia Farooq  
**Background:** BS Computer Science  
**Research interests:** Human-centred cybersecurity, phishing awareness, mobile security, applied machine learning, cybersecurity education  
**Email:** sadiafarooq1818@gmail.com

## Disclaimer

This repository is for academic research demonstration only. It should not be used as a security product or relied upon for real-world phishing protection without rigorous validation.