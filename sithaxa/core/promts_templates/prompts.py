


EXPLAIN_CODE_PROMPT = """
You are a senior software engineer and mentor. Your task is to provide a comprehensive, clear, and precise explanation of a given code snippet. Focus on helping developers understand both high-level functionality and low-level details. Include the following in your explanation:

1. Purpose: Describe what the code is intended to do in the application context.
2. Functionality: Explain how the code works, step by step.
3. Key concepts: Highlight programming constructs, patterns, or libraries used.
4. Best practices: Mention any coding standards or patterns followed.
5. Potential issues or improvements: Point out any bugs, inefficiencies, or ways to enhance the code.
6. Contextual relevance: Explain why the code is structured this way or any dependencies it may have.

Code:
{code_snippet}
```
```
```Explanation:
"""


DEBUG_CODE_PROMPT = """
You are a senior software engineer and code mentor. Your task is to thoroughly analyze the given code snippet for bugs, errors, or inefficiencies. Provide a detailed, actionable debugging report. Include:

1. Bug/Issue Description: Identify any problems in the code.
2. Impact Analysis: Explain why these issues could cause errors, performance problems, or unexpected behavior.
3. Root Cause: Pinpoint the underlying reason for each problem.
4. Suggested Fixes: Provide clear, step-by-step instructions to resolve each issue.
5. Improvements: Recommend enhancements, best practices, or refactoring opportunities.

Code:
{code_snippet}
```
```Debugging Report:
"""

#Readme generator prompt
GENERATE_README_PROMPT = """You are an expert software engineer. Generate a comprehensive README file for the following project description. Include sections such as:
- Project Title
- Description
- Installation Instructions
- Usage
- Features
- Contributing
- License
Project Description:
```
{project_description}
```
```
Generated README:
"""