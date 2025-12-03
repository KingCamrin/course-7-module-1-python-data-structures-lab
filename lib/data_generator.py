# This module contains functions to lazily generate student data.

def student_generator(students, major):
    """
    Return a generator expression for all students by major.
    
    Args:
        students: List of student tuples (ID, Name, Major)
        major: String representing the major to filter by
    
    Returns:
        Generator expression yielding students matching the specified major
    
    Example:
        generator_expression = (student for student in students if student[2] == major)
    """
    return (student for student in students if student[2] == major)