# This module contains operations related to sets.

def unique_majors(students):
    """
    Return a set of unique student majors using set comprehension.
    
    Args:
        students: List of student tuples (ID, Name, Major)
    
    Returns:
        Set of unique majors
    
    Example:
        Given students like:
        [
            (101, "Miles", "Mathematics"),
            (102, "Laura", "Mathematics"),
            (103, "Benji", "Physics"),
            (104, "Natalia", "Physics"),
            (105, "Nadia", "Mathematics"),
        ]
        
        Returns: {"Mathematics", "Physics"}
    """
    return {student[2] for student in students}