# Phishing Detection Demo Plan

## Purpose

The technical demo will support the proposed research by showing how URL risk cues can be extracted and used in a simple phishing detection workflow. The aim is not to build a production-grade cybersecurity system. The aim is to demonstrate research readiness, technical understanding and the ability to connect AI-assisted detection with user-friendly warning explanations.

## Possible dataset sources

A future version of this repository may use public phishing URL datasets, subject to supervisor guidance and dataset licensing. The dataset should contain legitimate and phishing URLs and should not require access to private user data.

## Possible features

The demo may extract simple, interpretable URL features such as:

- URL length;
- number of dots;
- number of hyphens;
- use of HTTPS;
- presence of IP address;
- presence of suspicious words such as login, verify, update, password, reset, urgent or claim;
- domain length;
- path length;
- use of shortened or misleading domains.

## Possible model

A basic interpretable classifier can be used first, such as logistic regression or decision tree. More advanced models can be considered later only if they improve research value and remain explainable.

## Evaluation metrics

The model can be evaluated using:

- accuracy;
- precision;
- recall;
- F1-score;
- confusion matrix.

## Connection to warning-card design

The model output should not only say “phishing” or “legitimate”. It should support user education by explaining risk cues in simple language, for example:

- “This link uses urgent wording.”
- “The domain does not match the expected organisation.”
- “This URL asks for login or password reset information.”
- “The link is not using HTTPS.”

## Future development

After supervisor feedback, this plan can be converted into a Jupyter notebook with reproducible code, dataset loading instructions, feature extraction, model training and evaluation.
