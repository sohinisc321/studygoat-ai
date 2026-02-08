from google.adk.agents import Agent

class PlannerAgent:
    def __init__(self, model):
        self.agent = Agent(
            name="PlannerAgent",
            model=model,
            instruction=self._instruction(),
            output_key="study_plan",
        )

    def _instruction(self) -> str:
        return """
You are PlannerAgent in the StudyGOAT AI system.

You receive:
- the user's original input
- the mood summary from MoodAgent: {mood_summary}

Task:
Create a DAILY study plan for today only.

Guidelines:
- Respect the mood-based load.
- light → very gentle
- medium → 2–3 focused blocks
- heavy → intensive but humanly possible

Output:
- structured plan with time blocks and topics
- 1–2 sentences explaining why this plan fits the user
"""

    def get_agent(self) -> Agent:
        return self.agent
