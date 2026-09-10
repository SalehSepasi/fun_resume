from llm import generate_resume


def build_prompt(name, job, age, skills, hobbies, personality):
    return f"""
Create a funny and creative resume for the following person.

Name: {name}
Job or Major: {job}
Age: {age}
Skills: {skills}
Hobbies: {hobbies}
Personality: {personality}

Rules:
- Make the resume humorous and creative.
- Keep it friendly and not offensive.
- Exaggerate the person's personality in a funny way.
- Include:
  1. A funny professional title
  2. About Me
  3. Skills
  4. Experience
  5. Interests
  6. Career Goal
- Do not mention that AI generated the resume.
- Return only the resume text.
"""


def generate_fun_resume(name, job, age, skills, hobbies, personality):
    prompt = build_prompt(
        name,
        job,
        age,
        skills,
        hobbies,
        personality,
    )

    return generate_resume(prompt)