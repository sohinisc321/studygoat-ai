# 🐐 StudyGOAT AI — Study Like the Greatest Of All Time

StudyGOAT AI is a mood-aware, adaptive multi-agent learning assistant designed to help students study realistically, even on low-energy or high-stress days.

## 🧠 Motivation
Most study tools assume students are always consistent and focused.
In reality, students deal with stress, fatigue, health issues, and limited time.
StudyGOAT AI adapts study plans based on the learner’s emotional and cognitive state.

## 🏗️ Architecture Overview
StudyGOAT AI is built as a **sequential multi-agent system** using Google ADK and Gemini.

Agents:
- **MoodAgent** — interprets emotional state and recommends study load
- **PlannerAgent** — creates a realistic daily study plan
- **TutorAgent** — explains one topic and generates quiz questions
- **ProgressAgent** — reflects on progress and adapts the next day’s plan

Agents communicate via structured session state (`output_key`) and run sequentially.

## ⚙️ Tech Stack
- Python
- Google Agent Development Kit (ADK)
- Gemini 2.5 Flash Lite
- Async orchestration
- dotenv-based configuration

## ▶️ How to Run
```bash
python -m venv .venv
source .venv/bin/activate  # or Windows equivalent
pip install -r requirements.txt
python run.py
