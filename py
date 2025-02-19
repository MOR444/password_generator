import random
import string

def generate_password(length=12, required_chars="", keep_order=False, use_uppercase=True, use_digits=True, use_special=True):
    """Generate a secure password with user-defined requirements."""

    # קבוצות תווים אפשריות
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if use_uppercase else ''
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special else ''
    
    # כל התווים האפשריים
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars

    if not all_chars and not required_chars:
        print("Error: At least one character set must be selected!")
        return None

    # התחלת הסיסמה עם התווים שהמשתמש דרש לכלול (אם יש)
    password = list(required_chars)

    # השלמת הסיסמה עד האורך הרצוי
    while len(password) < length:
        password.append(random.choice(all_chars))

    # שמירה על הסדר או ערבוב
    if not keep_order:
        random.shuffle(password)

    return ''.join(password)

# 🔹 שלב 1: האם המשתמש רוצה לכלול תווים ספציפיים?
include_specific_chars = input("Would you like to include specific letters or numbers in your password? (y/n): ").strip().lower() == 'y'

# 🔹 שלב 2: אם המשתמש רוצה תווים ספציפיים, נאסוף אותם
required_chars = ""
keep_order = False

if include_specific_chars:
    required_chars = input("Enter specific characters to include (e.g., name, numbers): ").strip()
    keep_order = input("Keep these characters in order? (y/n): ").strip().lower() == 'y'

# 🔹 שלב 3: שאלות על מאפייני הסיסמה
length = int(input("Enter password length (default 12): ") or 12)
use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

# 🔹 שלב 4: יצירת והצגת 4 סיסמאות שונות
print("\nGenerated Passwords:")
for i in range(4):
    password = generate_password(length, required_chars, keep_order, use_uppercase, use_digits, use_special)
    if password:
        print(f"{i+1}. {password}")
