import sys
from recruitment.crew import RecruitmentCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'job_requirements': """
        job_requirement:
  title: >
    Python and React JS Engineer
  description: >
    We are seeking a skilled Python and React JS engineer to join our team.
    The ideal candidate will have experience in both backend and frontend development,

  responsibilities: >
    - Write clean, maintainable, and efficient code.
    - Ensure application performance and responsiveness.
    - Identify and resolve bottlenecks and bugs.

  requirements: >
    - Proven experience with Python and React.
    - Strong understanding of object-oriented programming.
    - Proficiency with JavaScript, HTML, CSS, and React.

  preferred_qualifications: >
    - Experience with cloud services (AWS, Google Cloud, or Azure).
    - Bachelor's degree in Computer Science or a related field.
        """
    }
    RecruitmentCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'job_requirements': """
        job_requirement:
  title: >
    Python and React JS Engineer
  description: >
    We are seeking a skilled Python and React JS engineer to join our team.
    The ideal candidate will have experience in both backend and frontend development,

  responsibilities: >
    - Develop and maintain web applications using Python and React JS.
    - Collaborate with teams to define and implement new features.
    - Write clean, maintainable, and efficient code.

  requirements: >
    - Proven experience with Python and React JS.
    - Strong understanding of object-oriented programming.
    - Proficiency with JavaScript, HTML, CSS, and React.

  preferred_qualifications: >
    - Experience with cloud services (AWS, Google Cloud, or Azure).
    - Bachelor's degree in Computer Science or a related field.
        """
    }
    try:
        RecruitmentCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")