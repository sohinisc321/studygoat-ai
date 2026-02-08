from google.adk.agents import Agent

class ProgressAgent:
    def __init__(self, model):
        self.agent = Agent(
            name="ProgressAgent",
            model=model,
            instruction=self._instruction(),
            output_key="tomorrow_plan",
        )

    def _instruction(self) -> str:
        return """
You are ProgressAgent in the StudyGOAT AI system.

You receive:
- today's plan: {study_plan}
- tutoring output: {tutoring_block}
- user's feedback in the prompt

Task:
1. Reflect on how today went.
2. Suggest how to adjust tomorrow:
   - load
   - topic difficulty
   - strategy (breaks, pacing)

Be practical, empathetic, and realistic.
"""

    def get_agent(self) -> Agent:
        return self.agent
