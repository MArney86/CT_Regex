#Task 1:
import re #given code

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com" #given code
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude.com)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text) #added a ?! grouping to check exclude.com domain isn't there before ensuring that the rest of the domain is part of the possible valid email
print(emails) #given code
