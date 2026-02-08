from google.adk.agents import SequentialAgent
from google.adk.runners import InMemoryRunner

from agents.mood_agent import MoodAgent
from agents.planner_agent import PlannerAgent
from agents.tutor_agent import TutorAgent
from agents.progress_agent import ProgressAgent

def build_studygoat_pipeline(model):
    mood = MoodAgent(model).get_agent()
    planner = PlannerAgent(model).get_agent()
    tutor = TutorAgent(model).get_agent()
    progress = ProgressAgent(model).get_agent()

    return SequentialAgent(
        name="StudyGOATAgent",
        sub_agents=[mood, planner, tutor, progress],
    )

def get_runner(model):
    pipeline = build_studygoat_pipeline(model)
    return InMemoryRunner(agent=pipeline)
