# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    

    """
    for student in student_list:
        if student['major'] == major:
            yield student

