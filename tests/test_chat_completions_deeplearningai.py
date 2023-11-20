import pytest
import os
from openai_api.text_generation_api import *
from common.openai_model_define import Model
from common.logging_define import print_json_d



client = OpenAI()

# deeplearning.ai prompt enginnering
# https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/2/guidelines
#
# Principle 1: Write clear and specific instructions
#
# Tactic 1: Use delimiters to clearly indicate distinct parts of the input
#   -- Delimiters can be anything like: ```, """, < >, <tag> </tag>
#

def test_p1_t1_delimiters():
    text = f"""
    You should express what you want a model to do by \
    providing instructions that are as clear and \
    specific as you can possibly make them. \
    This will guide the model towards the desired output, \
    and reduce the chances of receiving irrelevant \
    or incorrect responses. Don't confuse writing a \
    clear prompt with writing a short prompt. \
    In many cases, longer prompts provide more clarity \
    and context for the model, which can lead to \
    more detailed and relevant outputs.
    """

    prompt = f""" 
    Summarize the text delimited by triple backticks \
    into a single sentence.
    ```{text}```
    """

    messages = [{"role": "user", "content": prompt}]
    response = fetch_chat_completion(client, messages)
    print(response)


# Tactic 2: Ask for a structured output
#   -- JSON, HTML
#
def test_p1_t2_json():
    prompt = f"""
    Generate a list of three made-up book titles along \
    with their authors and genres. \
    Provide them in JSON format with the following keys: \
    book_id, title, author, genre.
    """

    messages = [{
        "role": "user",
        "content": prompt
    }]

    try:
        response = fetch_chat_completion_json(client, messages)
    except Exception:
        assert False, "An excpetion was raised"

    print(json.dumps(response.choices[0].message.content, indent=4))



# Tactic 3: Ask the model to check whether conditions are satisfied
def test_p1_t3_check():
    text_1 = f"""
    Making a cup of tea is easy! First, you need to get some \
    water boiling. While that's happening, \
    grab a cup and put a tea bag in it. Once the water is \
    hot enough, just pour it over the tea bag. \
    Let it sit for a bit so the tea can steep. After a \
    few minutes, take out the tea bag. If you \
    like, you can add some sugar or milk to taste. \
    And that's it! You've got yourself a delicious \
    cup of tea to enjoy.
    """

    prompt = f"""
    You will be provided with text delimited by triple quotes.
    If it contains a sequence of instructions, \
    re-write those instructions in the following format:

    Step 1 - ...
    Step 2 - …
    …
    Step N - …

    If the text does not contain a sequence of instructions, \
    then simply write \"No steps provided.\"

    \"\"\"{text_1}\"\"\"
    """

    messages = [
        {
            "role": "system",
            "content": "you are helpful assistant designed to ouput JSON"
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    try:
        response = fetch_chat_completion_json(client, messages)
        LOG_D(response.choices[0].message.content)
    except Exception:
        assert False, "An exception was raised"


# Tactic 4: "Few-shot" prompting
def test_p1_t4_few_shot():
    prompt = f"""
        Your task is to answer in a consistent style.

        <child>: Teach me about patience.

        <grandparent>: The river that carves the deepest \
        valley flows from a modest spring; the \
        grandest symphony originates from a single note; \
        the most intricate tapestry begins with a solitary thread.

        <child>: Teach me about resilience.
        """

    messages = [
        {
            "role": "system",
            "content":"you are helpful assistant designed to output JSON"
        },
        {
            "role": "user",
            "content": prompt
        }]

    try:
        response = fetch_chat_completion_json(client, messages)
        LOG_D(response.choices[0].message.content)
    except Exception:
        assert Fasle, "An exception was rasied"


##################################################################
#   Principle 2: Give the model time to "think"
##################################################################
# Tactic1: Specify the steps required to complete a task
def test_p2_t1_steps_ex1():  # Principle2, Tactic1
    text = f"""
    In a charming village, siblings Jack and Jill set out on \
    a quest to fetch water from a hilltop \
    well. As they climbed, singing joyfully, misfortune \
    struck—Jack tripped on a stone and tumbled \
    down the hill, with Jill following suit. \
    Though slightly battered, the pair returned home to \
    comforting embraces. Despite the mishap, \
    their adventurous spirits remained undimmed, and they \
    continued exploring with delight.
    """
    # example 1
    prompt = f"""
    Perform the following actions:
    1 - Summarize the following text delimited by triple \
    backticks with 1 sentence.
    2 - Translate the summary into French.
    3 - List each name in the French summary.
    4 - Output a json object that contains the following \
    keys: french_summary, num_names.
    
    Separate your answers with line breaks.
    
    Text:
    ```{text}```
    """

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant and output in JSON"
        }, 
        {
            "role": "user",
            "content": prompt,
        }]

    try:
        response = fetch_chat_completion_json(client, messages)
        LOG_D(response.choices[0].message.content)
    except Exception:
        assert False, "An exception was raised"





# Tactic1-example2: Ask for output in a specific format
def test_p2_t1_steps_ex2():  # Principle2, Tactic1
    text = f"""
    In a charming village, siblings Jack and Jill set out on \
    a quest to fetch water from a hilltop \
    well. As they climbed, singing joyfully, misfortune \
    struck—Jack tripped on a stone and tumbled \
    down the hill, with Jill following suit. \
    Though slightly battered, the pair returned home to \
    comforting embraces. Despite the mishap, \
    their adventurous spirits remained undimmed, and they \
    continued exploring with delight.
    """

    prompt = f"""
    Your task is to perform the following actions: 
    1 - Summarize the following text delimited by 
      <> with 1 sentence.
    2 - Translate the summary into French.
    3 - List each name in the French summary.
    4 - Output a json object that contains the 
      following keys: french_summary, num_names.
    
    Use the following format:
    Text: <text to summarize>
    Summary: <summary>
    Translation: <summary translation>
    Names: <list of names in Italian summary>
    Output JSON: <json with summary and num_names>
    
    Text: <{text}>
    """
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant and output in JSON"
        }, 
        {
            "role": "user",
            "content": prompt,
        }]

    try:
        response = fetch_chat_completion_json(client, messages)
        LOG_D(response.choices[0].message.content)
    except Exception:
        assert False, "An exception was raised"



## Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion

# Note that the student's solution is actually not correct.
# We can fix this by instructing the model to work out its own solution first.
def test_p2_t2_own_solution_ex1():  # Principle2, Tactic1

    prompt = f"""
    Determine if the student's solution is correct or not.

    Question:
    I'm building a solar power installation and I need \
     help working out the financials. 
    - Land costs $100 / square foot
    - I can buy solar panels for $250 / square foot
    - I negotiated a contract for maintenance that will cost \
    me a flat $100k per year, and an additional $10 / square \
    foot
    What is the total cost for the first year of operations
    as a function of the number of square feet.

    Student's Solution:
    Let x be the size of the installation in square feet.
    Costs:
    1. Land cost: 100x
    2. Solar panel cost: 250x
    3. Maintenance cost: 100,000 + 100x
    Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
    """

    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant and output in JSON"
        }, 
        {
            "role": "user",
            "content": prompt,
        }]

    try:
        response = fetch_chat_completion_json(client, messages)
        LOG_D(response.choices[0].message.content)
    except Exception:
        assert False, "An exception was raised"


# fix the wrong student answer
def test_p2_t2_own_solution_ex2():  # Principle2, Tactic1
    prompt = f"""
    Your task is to determine if the student's solution \
    is correct or not.
    To solve the problem do the following:
    - First, work out your own solution to the problem. 
    - Then compare your solution to the student's solution \ 
    and evaluate if the student's solution is correct or not. 
    Don't decide if the student's solution is correct until 
    you have done the problem yourself.
    
    Use the following format:
    Question:
    ```
    question here
    ```
    Student's solution:
    ```
    student's solution here
    ```
    Actual solution:
    ```
    steps to work out the solution and your solution here
    ```
    Is the student's solution the same as actual solution \
    just calculated:
    ```
    yes or no
    ```
    Student grade:
    ```
    correct or incorrect
    ```
    
    Question:
    ```
    I'm building a solar power installation and I need help \
    working out the financials. 
    - Land costs $100 / square foot
    - I can buy solar panels for $250 / square foot
    - I negotiated a contract for maintenance that will cost \
    me a flat $100k per year, and an additional $10 / square \
    foot
    What is the total cost for the first year of operations \
    as a function of the number of square feet.
    ``` 
    Student's solution:
    ```
    Let x be the size of the installation in square feet.
    Costs:
    1. Land cost: 100x
    2. Solar panel cost: 250x
    3. Maintenance cost: 100,000 + 100x
    Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
    ```
    Actual solution:
    """

    messages = [
        {
            "role": "system",
            "content": "You are a math teacher and output in JSON"
        }, 
        {
            "role": "user",
            "content": prompt,
        }]

    try:
        response = fetch_chat_completion_json(client, messages)
        LOG_D(response.choices[0].message.content)
    except Exception:
        assert False, "An exception was raised"



