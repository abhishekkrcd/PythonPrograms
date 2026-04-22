#This programs uses a class function to check if a string is a pallindrome or not
class Pallindrome:
    def __init__(self, string):
        self.string = string

    def is_pallindrome(self):
        # Remove spaces and convert to lowercase for uniformity
        cleaned_string = self.string.replace(" ", "").lower()
        # Check if the cleaned string is equal to its reverse
        return cleaned_string == cleaned_string[::-1]

# Example usage:
if __name__ == "__main__":
    test_string = input("Enter a string to check if it's a palindrome: ")
    p = Pallindrome(test_string)
    if p.is_pallindrome():
        print(f"'{test_string}' is a palindrome.")
    else:
        print(f"'{test_string}' is not a palindrome.")
        