import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import call_function
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

system_prompt = """
You are a helpful AI coding agent.

You can perform the following operations:
- List files and directories
- Read file contents
- Write to files (create or update)
- Run Python files with optional arguments

All paths should be relative to the working directory. The working directory is automatically injected for security.
"""

if len(sys.argv) < 2:
    print("I need a prompt!")
    sys.exit(1)

prompt = sys.argv[1]
verbose_flag = len(sys.argv) == 3 and sys.argv[2] == "--verbose"

# Conversation messages
messages = [
    types.Content(role="user", parts=[types.Part.from_text(text=prompt)]),
]

# Register available functions
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file
    ]
)

config = types.GenerateContentConfig(
    tools=[available_functions],
    system_instruction=system_prompt
)

max_iters = 20
for _ in range(max_iters):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=config,
    )

    if response is None:
        print("Response is malformed")
        break

    # Handle verbose output
    if verbose_flag and response.usage_metadata:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    # Process candidates
    if response.candidates:
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)

    # Handle function calls
    if response.function_calls:
        function_responses = []
        for fc in response.function_calls:
            result_content = call_function(fc, verbose_flag)
            function_responses.append(result_content.parts[0])  # one Part per call

        # Append all function responses in one Content
        messages.append(types.Content(role="tool", parts=function_responses))
        continue  # let the model make the next step

    # Final text response
    if response.text:
        print(response.text)
        break


# import os
# import sys
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types
# from functions.get_files_info import schema_get_files_info
# from functions.get_file_content import schema_get_file_content
# from functions.write_file import schema_write_file
# from functions.run_python_file import schema_run_python_file
# from call_function import call_function


# def main():
#     load_dotenv()
#     api_key = os.environ.get("GEMINI_API_KEY")

#     client = genai.Client(api_key=api_key)

#     system_prompt = """
#     You are a helpful AI coding agent.

#     When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

#     - List files and directories
#     - Read file contents
#     - Write to files (create or update)
#     - Run Python file with optional arguments

#     All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
#     """

#     if len(sys.argv) < 2:
#         print("I need a prompt!")
#         sys.exit(1)

#     verbose_flag = False
#     if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
#         verbose_flag = True

#     prompt = sys.argv[1]

#     messages = [
#         types.Content(role="user", parts=[types.Part(text=prompt)]),
#     ]

#     available_functions = types.Tool(
#         function_declarations=[
#             schema_get_files_info,
#             schema_get_file_content,
#             schema_write_file,
#             schema_run_python_file,
#         ]
#     )

#     config = types.GenerateContentConfig(
#         tools=[available_functions],
#         system_instruction=system_prompt,
#     )

#     max_iters = 20
#     for _ in range(max_iters):
#         response = client.models.generate_content(
#             model="gemini-2.0-flash-001",
#             contents=messages,
#             config=config,
#         )

#         if not response or not response.candidates:
#             print("response is malformed")
#             return

#         if verbose_flag and response.usage_metadata:
#             print(f"User prompt: {prompt}")
#             print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
#             print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

#         handled_function = False
#         for candidate in response.candidates:
#             if not candidate or not candidate.content:
#                 continue

#             for part in candidate.content.parts:
#                 if part.function_call:
#                     handled_function = True
#                     print(f"- Calling function: {part.function_call.name}")
#                     result = call_function(part.function_call, verbose_flag)
#                     messages.append(result)
#                 elif part.text:
#                     print(part.text)
#                     return

#         if not handled_function:
#             return


# main()



# import os
# import sys
# from dotenv import load_dotenv
# from google import genai
# from google.genai import types
# from functions.get_files_info import schema_get_files_info
# from functions.get_file_content import schema_get_file_content
# from functions.write_file import schema_write_file
# from functions.run_python_file import schema_run_python_file
# from call_function import call_function


# def main():
#     load_dotenv()
#     api_key = os.environ.get("GEMINI_API_KEY")

#     client = genai.Client(api_key=api_key)

#     system_prompt = """
#     You are a helpful AI coding agent.

#     When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

#     - List files and directories
#     - Read file contents
#     - Write to files (create or update)
#     - Run Python file with optional arguments

#     All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
#     """

#     if len(sys.argv) < 2:
#         print("I need a prompt!")
#         sys.exit(1)

#     verbose_flag = False
#     if len(sys.argv) == 3 and sys.argv[2] == "--verbose":
#         verbose_flag = True   # ✅ no sys.exit here

#     prompt = sys.argv[1]

#     messages = [
#         types.Content(role="user", parts=[types.Part(text=prompt)]),
#     ]

#     available_functions = types.Tool(
#         function_declarations=[
#             schema_get_files_info,
#             schema_get_file_content,
#             schema_write_file,
#             schema_run_python_file
#         ]
#     )

#     config = types.GenerateContentConfig(
#         tools=[available_functions],
#         system_instruction=system_prompt
#     )

#     max_iters = 20
#     for i in range(0, max_iters):  # ✅ fixed indentation
#         response = client.models.generate_content(
#             model="gemini-2.0-flash-001",
#             contents=messages,
#             config=config,
#         )

#         if response is None or response.usage_metadata is None:
#             print("response is malformed")
#             return

#         if verbose_flag:
#             print(f"User prompt: {prompt}")
#             print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
#             print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

#         if response.candidates:        
#             for candidate in response.candidates:
#                 if candidate is None or candidate.content is None:
#                     continue
                
#         if response.function_calls:        
#             for function_call_part in response.function_calls:                
#                 result = call_function(function_call_part, verbose_flag)
#                 messages.append(result)
#         else:
#             # final agent text message
#             print(response.text)
#             return


# main()
