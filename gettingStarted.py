### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    # Students do not have to follow the skeleton for this assignment.
    # Another way to implement is using "case" statements similar to C.

    if question == "Are encoding and encryption the same? - Yes/No":
        return "No"

    elif question == "Is it possible to decrypt a message without a key? - Yes/No":
        return "No"

    elif question == "Is it possible to decode a message without a key? - Yes/No":
        return "Yes"

    elif question == "Is a hashed message supposed to be un-hashed? - Yes/No":
        return "No"

    elif question == "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
        return "568e8dd251210f81b8c110b6d95f2a5018385c898f62db1aefb207b62eee9607"  # SHA256 hash of 'zairm01@nyu.edu'

    elif question == "Is MD5 a secured hashing algorithm? - Yes/No":
        return "No"

    elif question == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        return 4  # Application layer

    elif question == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        return 3  # Network layer

    elif question == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        return "pcap" 

    else: 
        # This ensures unexpected questions are handled
        return "This is not my beautiful wife! This is not my beautiful car! How did I get here?"

# Debugging section following the given skeleton format
if __name__ == "__main__":
    # Use this space to debug and verify that the program works
    debug_question = "Are encoding and encryption the same? - Yes/No"
    print(welcome_assignment_answers(debug_question))
