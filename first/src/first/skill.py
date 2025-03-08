from crewai.flow.flow import Flow, start, listen
from litellm import completion
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
      
class LearningPathFlow(Flow):
    model = "gemini/gemini-2.0-flash-exp"

    @start()
    def get_user_input(self):
        """Ask user about their skills and learning goals."""
        print("Starting Learning Path Flow...")

        skills = input("Enter your current skills (e.g., Python, SQL, No experience): ")
        goal = input("Enter your learning goal (e.g., Become a Data Scientist, Web Developer): ")

        self.state["skills"] = skills
        self.state["goal"] = goal

        print(f"User Skills: {skills}")
        print(f"User Goal: {goal}")
        return skills, goal

    @listen(get_user_input)
    def generate_learning_roadmap(self, skills_goal):
        """Generate a personalized learning roadmap."""
        skills, goal = skills_goal

        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": f"Create a learning roadmap for a person with {skills} who wants to {goal}. Include books, courses, and projects."}],
            verbose=True
        )
        roadmap = response.choices[0].message.content.strip()
        self.state["roadmap"] = roadmap

        print("Generated Learning Roadmap:")
        print(roadmap)
        return roadmap

    @listen(generate_learning_roadmap)
    def generate_milestones(self, roadmap):
        """Generate weekly milestones for tracking progress."""
        response = completion(
            model=self.model,
            messages=[{"role": "user", "content": f"Break down the following learning roadmap into weekly milestones:\n{roadmap}"}],
            verbose=True
        )
        milestones = response.choices[0].message.content.strip()
        self.state["milestones"] = milestones

        print("Generated Weekly Milestones:")
        print(milestones)
        return milestones

    @listen(generate_milestones)
    def save_learning_plan(self, milestones):
        """Save the learning plan to a file."""
        print("Saving Learning Path Plan...")

        with open("learning_path.md", "w") as f:
            f.write("# Personalized Learning Path\n\n")
            f.write(f"## User Skills: {self.state['skills']}\n")
            f.write(f"## Goal: {self.state['goal']}\n\n")
            f.write(f"## Roadmap:\n{self.state['roadmap']}\n\n")
            f.write(f"## Weekly Milestones:\n{milestones}\n")

        print("Learning Path Saved Successfully!")

def kickoff():
    """Kick off the learning path flow."""
    learning_path = LearningPathFlow()
    result = learning_path.kickoff()
    print("Final Learning Plan:")
    print(result)

if __name__ == "__main__":
    kickoff()