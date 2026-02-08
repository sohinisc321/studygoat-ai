import asyncio

from core.config import get_llm
from core.orchestrator import get_runner


async def main():
    # Initialize LLM (Gemini)
    model = get_llm()

    # Build runner with StudyGOAT pipeline
    runner = get_runner(model)

    user_message = """
    Exam: Data Structures exam in 5 days.
    Syllabus topics: Arrays, Stacks, Queues, Trees, Graphs.
    I can study around 3 hours today.

    Mood: I am very tired and a bit anxious.
    Yesterday I couldn't concentrate properly and felt guilty.
    """

    print("\n--- FINAL OUTPUT ---\n")
    response = await runner.run_debug(user_message)
    print(response)


if __name__ == "__main__":
    asyncio.run(main())
