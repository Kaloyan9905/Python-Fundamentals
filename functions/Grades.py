def current_grade_text(grade_text):
    if 2.00 <= grade_text <= 2.99:
        return 'Fail'
    elif 3.00 <= grade_text <= 3.49:
        return 'Poor'
    elif 3.50 <= grade_text <= 4.49:
        return 'Good'
    elif 4.50 <= grade_text <= 5.49:
        return 'Very Good'
    elif 5.50 <= grade_text <= 6.00:
        return 'Excellent'


grade = float(input())
print(current_grade_text(grade))
