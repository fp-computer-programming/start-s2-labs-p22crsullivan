# Define comes_after function
def comes_after(st, letter):
    letter = letter.lower()
# Save the result
    return ''.join(b for a, b in zip(st.lower(), st[1:]) if a == letter and b.isalpha())