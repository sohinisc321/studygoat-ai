from google.adk.agents import Agent
from google.adk.tools import google_search

class TutorAgent:
    def __init__(self, model):
        self.agent = Agent(
            name="TutorAgent",
            model=model,
            instruction=self._instruction(),
            tools=[google_search],
            output_key="tutoring_block",
        )

    def _instruction(self) -> str:
        return """
You are TutorAgent in the StudyGOAT AI system.

You receive today's study plan: {study_plan}

Task:
1. Pick ONE important topic.
2. Use google_search if needed.
3. Provide:
   - a simple explanation
   - 3–5 quiz questions (no answers)

Be clear, concise, and student-friendly.
"""

    def get_agent(self) -> Agent:
        return self.agent
