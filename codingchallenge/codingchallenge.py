import re

def extract_phone_numbers(string):
    phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"
    phone_numbers = re.findall(phone_pattern, string)
    return phone_numbers

def extract_email_addresses(string):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    email_addresses = re.findall(email_pattern, string)
    return email_addresses

def replace_email_addresses(string, replacement):
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    replaced_string = re.sub(email_pattern, replacement, string)
    return replaced_string

string = "Please contact info@example.com for assistance. Phone: (123) 456-7890 or (111) 222-3333"
print(extract_phone_numbers(string))
# Output: ['(123) 456-7890', '(111) 222-3333']
print(extract_email_addresses(string))
# Output: ['info@example.com']
print(replace_email_addresses(string, "REPLACED"))
# Output: "Please contact REPLACED for assistance. Phone: (123) 456-7890 or (111) 222-3333"
