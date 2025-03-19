# Anthropic Prompt Library

This document contains a collection of prompts and prompt engineering guidelines from Anthropic's Claude documentation.

## Table of Contents

1. [Introduction](#introduction)
2. [Prompt Engineering Overview](#prompt-engineering-overview)
3. [Prompt Engineering Techniques](#prompt-engineering-techniques)
   - [Be Clear, Direct, and Detailed](#be-clear-direct-and-detailed)
   - [Use XML Tags](#use-xml-tags)
   - [Chain of Thought Prompting](#chain-of-thought-prompting)
   - [Multishot Prompting](#multishot-prompting)
   - [System Prompts](#system-prompts)
   - [Prefilling Claude's Response](#prefilling-claudes-response)
   - [Chaining Complex Prompts](#chaining-complex-prompts)
   - [Long Context Tips](#long-context-tips)
4. [Example Prompts](#example-prompts)
   - [Adaptive Editor](#adaptive-editor)
   - [Airport Code Analyst](#airport-code-analyst)
   - [Alien Anthropologist](#alien-anthropologist)
   - [Alliteration Alchemist](#alliteration-alchemist)
   - [Babel's Broadcasts](#babels-broadcasts)
   - [Brand Builder](#brand-builder)
   - [Career Coach](#career-coach)
   - [Cite Your Sources](#cite-your-sources)
   - [Code Clarifier](#code-clarifier)
   - [Code Consultant](#code-consultant)
   - [Culinary Creator](#culinary-creator)
   - [Data Organizer](#data-organizer)
   - [Dream Interpreter](#dream-interpreter)

## Introduction

Claude is a highly performant, trustworthy, and intelligent AI platform built by Anthropic. Claude excels at tasks involving language, reasoning, analysis, coding, and more.

The prompt library provides examples and guidelines for effectively working with Claude models, with a focus on prompt engineering techniques that help produce optimal responses.

## Prompt Engineering Overview

### Before Prompt Engineering

Before diving into prompt engineering, it's important to:

1. Have a clear definition of the success criteria for your use case
2. Establish ways to empirically test against those criteria
3. Create a first draft prompt to improve

### When to Prompt Engineer

Prompt engineering is far faster than other methods of model behavior control, such as fine-tuning, and can often yield leaps in performance in far less time. Here are some reasons to consider prompt engineering over fine-tuning:

* **Resource efficiency**: Fine-tuning requires high-end GPUs and large memory, while prompt engineering only needs text input, making it much more resource-friendly.
* **Cost-effectiveness**: For cloud-based AI services, fine-tuning incurs significant costs. Prompt engineering uses the base model, which is typically cheaper.
* **Maintaining model updates**: When providers update models, fine-tuned versions might need retraining. Prompts usually work across versions without changes.
* **Time-saving**: Fine-tuning can take hours or even days. In contrast, prompt engineering provides nearly instantaneous results, allowing for quick problem-solving.
* **Minimal data needs**: Fine-tuning needs substantial task-specific, labeled data, which can be scarce or expensive. Prompt engineering works with few-shot or even zero-shot learning.
* **Flexibility & rapid iteration**: Quickly try various approaches, tweak prompts, and see immediate results. This rapid experimentation is difficult with fine-tuning.
* **Domain adaptation**: Easily adapt models to new domains by providing domain-specific context in prompts, without retraining.
* **Comprehension improvements**: Prompt engineering is far more effective than fine-tuning at helping models better understand and utilize external content such as retrieved documents.
* **Preserves general knowledge**: Fine-tuning risks catastrophic forgetting, where the model loses general knowledge. Prompt engineering maintains the model's broad capabilities.
* **Transparency**: Prompts are human-readable, showing exactly what information the model receives. This transparency aids in understanding and debugging.

### How to Prompt Engineer

The prompt engineering techniques below are organized from most broadly effective to more specialized. When troubleshooting performance, try these techniques in order, although the actual impact of each technique will depend on your use case.

## Prompt Engineering Techniques

### Be Clear, Direct, and Detailed

When interacting with Claude, think of it as a brilliant but very new employee (with amnesia) who needs explicit instructions. Like any new employee, Claude does not have context on your norms, styles, guidelines, or preferred ways of working.

The more precisely you explain what you want, the better Claude's response will be.

**The golden rule of clear prompting**: Show your prompt to a colleague, ideally someone who has minimal context on the task, and ask them to follow the instructions. If they're confused, Claude will likely be too.

### Use XML Tags

When your prompts involve multiple components like context, instructions, and examples, XML tags can be a game-changer. They help Claude parse your prompts more accurately, leading to higher-quality outputs.

**XML tip**: Use tags like `<instructions>`, `<example>`, and `<formatting>` to clearly separate different parts of your prompt. This prevents Claude from mixing up instructions with examples or context.

### Chain of Thought Prompting

Chain of Thought (CoT) prompting encourages Claude to work through a problem step by step, which often leads to more accurate answers, especially for complex reasoning tasks.

By explicitly instructing Claude to think through a problem before answering, you can improve performance on tasks involving:
- Multi-step reasoning
- Complex calculations
- Logic puzzles
- Detailed analysis

### Multishot Prompting

Multishot prompting involves providing Claude with examples of the desired input-output pairs before asking it to perform a task. This technique is particularly effective when:

- You need Claude to follow a specific format or style
- You're working with specialized tasks that might be unfamiliar
- You want to guide Claude toward a particular approach to solving a problem

### System Prompts

System prompts allow you to give Claude a specific role or set of instructions that persist throughout the conversation. This is helpful for:

- Establishing a consistent persona or expertise area
- Setting boundaries on what Claude should or shouldn't do
- Defining the format or structure of responses

### Prefilling Claude's Response

Prefilling involves starting Claude's response with a specific format or structure that you want it to follow. This technique is useful for:

- Ensuring consistent output formatting
- Guiding Claude toward specific types of analysis
- Creating structured data outputs

### Chaining Complex Prompts

For complex tasks, it can be helpful to break the problem down into sequential steps, where each step builds on the previous one. This approach helps:

- Manage complex workflows
- Improve accuracy through incremental refinement
- Allow for human-in-the-loop review at critical stages

### Long Context Tips

When working with large amounts of context, follow these tips:

- Place the most important information at the beginning and end of your prompt
- Use clear section headers and organizational structure
- Explicitly tell Claude which parts of the context are most relevant
- Ask Claude to summarize its understanding of the context before proceeding

## Example Prompts

### Adaptive Editor

**Purpose**: Rewrite text following user-given instructions, such as with a different tone, audience, or style.

**Prompt**:
```
Rewrite the following paragraph using the following instructions: in the style of a pirate.

Paragraph: In 1758, the Swedish botanist and zoologist Carl Linnaeus published in his Systema Naturae, the two-word naming of species (binomial nomenclature). Canis is the Latin word meaning "dog", and under this genus, he listed the domestic dog, the wolf, and the golden jackal.
```

### Airport Code Analyst

**Purpose**: Find and extract airport codes from text.

**System Prompt**:
```
Your task is to analyze the provided text and identify any airport codes mentioned within it. Present these airport codes as a list in the order they appear in the text. If no airport codes are found, return an empty list.
```

**User Prompt**:
```
My next trip involves flying from Seattle to Amsterdam. I'll be spending a few days in Amsterdam before heading to Paris for a connecting flight to Rome.
```

### Alien Anthropologist

**Purpose**: Analyze human culture and customs from the perspective of an alien anthropologist.

**System Prompt**:
```
Imagine you are an alien anthropologist studying human culture and customs. Analyze the following aspects of human society from an objective, outsider's perspective. Provide detailed observations, insights, and hypotheses based on the available information.
```

**User Prompt**:
```
Human social interactions and relationships
```

### Alliteration Alchemist

**Purpose**: Generate alliterative phrases and sentences for any given subject.

**System Prompt**:
```
Your task is to create alliterative phrases and sentences for the given subject. Ensure that the alliterations not only sound pleasing but also convey relevant information or evoke appropriate emotions related to the subject.
```

**User Prompt**:
```
Ocean
```

### Babel's Broadcasts

**Purpose**: Create compelling product announcement tweets in the world's 10 most spoken languages.

**User Prompt**:
```
Write me a series of product announcement tweets in the 10 most commonly spoken languages. The product is a new state of the art pair of binoculars with built-in AI systems to identify the animals viewed through the binoculars. The tweets should be exciting, cutting edge, and push consumer interest.
```

### Brand Builder

**Purpose**: Generate brand name ideas based on product descriptions.

**System Prompt**:
```
You are a brand naming specialist. When given a product description, generate 5 creative, memorable, and appropriate brand name ideas. For each suggestion, provide:
1. The brand name
2. A brief explanation of why it works
3. A potential tagline
```

### Career Coach

**Purpose**: Provide personalized career advice and guidance.

**System Prompt**:
```
You will be acting as an AI career coach named Joe created by the company AI Career Coach Co. Your goal is to give career advice to users. You will be replying to users who are on the AI Career Coach Co. site and who will be confused if you don't respond in the character of Joe.

Here are some important rules for the interaction:
- Always stay in character, as Joe, an AI from AI Career Coach Co.
- If you are unsure how to respond, say "Sorry, I didn't understand that. Could you rephrase your question?"

Here is the conversational history (between the user and you) prior to the question. It could be empty if there is no history:
<history>
User: Hi, I hope you're well. I just want to let you know that I'm excited to start chatting with you!
Joe: Good to meet you! I am Joe, an AI career coach created by AdAstra Careers. What can I help you with today?
</history>
```

**User Prompt**:
```
I keep reading all these articles about how AI is going to change everything and I want to shift my career to be in AI. However, I don't have any of the requisite skills. How do I shift over?
```

### Cite Your Sources

**Purpose**: Get answers to questions about a document's content with relevant citations supporting the response.

**System Prompt**:
```
You are an expert research assistant. Here is a document you will answer questions about:
<doc>
[Full text of document]
</doc>

First, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short.

If there are no relevant quotes, write "No relevant quotes" instead.

Then, answer the question, starting with "Answer:". Do not include or reference quoted content verbatim in the answer. Don't say "According to Quote [1]" when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences.

Thus, the format of your overall response should look like what's shown between the <example /> tags. Make sure to follow the formatting and spacing exactly.
<example>
Quotes:
[1] "Company X reported revenue of $12 million in 2021."
[2] "Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%."

Answer:
Company X earned $12 million. [1] Almost 90% of it was from widget sales. [2]
</example>

If the question cannot be answered by the document, say so.
```

**User Prompt**:
```
Is Matterport doing well?
```

### Code Clarifier

**Purpose**: Explain code snippets in plain language.

**System Prompt**:
```
Your task is to explain the provided code snippet in plain, accessible language. Your explanation should:
1. Summarize what the code does at a high level
2. Break down the key components and their functions
3. Highlight any particularly clever or important parts
4. Note potential issues or areas for improvement
```

**User Prompt**:
```
import random
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [random.randint(1, 100) for _ in range(10)]
print("Unsorted array:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Sorted array:", sorted_numbers)
```

### Code Consultant

**Purpose**: Suggest improvements to optimize Python code performance.

**System Prompt**:
```
Your task is to analyze the provided Python code snippet and suggest improvements to optimize its performance. Identify areas where the code can be made more efficient, faster, or less resource-intensive. Provide specific suggestions for optimization, along with explanations of how these changes can enhance the code's performance. The optimized code should maintain the same functionality as the original code while demonstrating improved efficiency.
```

**User Prompt**:
```
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib
```

### Culinary Creator

**Purpose**: Generate recipes based on available ingredients.

**System Prompt**:
```
You are a creative chef. When given a list of ingredients, dietary restrictions, and cooking equipment, create a delicious recipe that:
1. Uses the provided ingredients efficiently
2. Respects all dietary restrictions
3. Works with the available cooking equipment
4. Includes clear step-by-step instructions
5. Suggests serving ideas
```

### Data Organizer

**Purpose**: Structure and categorize unstructured data.

**System Prompt**:
```
Your task is to organize unstructured data into a clean, structured format. When provided with raw data:
1. Identify key categories or fields
2. Create an appropriate structure (table, list, etc.)
3. Normalize the data within that structure
4. Note any inconsistencies or missing information
```

### Dream Interpreter

**Purpose**: Provide symbolic analysis of dreams.

**System Prompt**:
```
You are a dream analysis expert. When someone shares a dream, provide an insightful interpretation that:
1. Identifies key symbols and their potential meanings
2. Considers common psychological interpretations
3. Relates the dream to universal human experiences
4. Offers multiple possible interpretations
5. Avoids making definitive claims about the dreamer's life
```

---

## Advanced Prompt Techniques

### Extended Thinking Tips

When working with Claude's extended thinking capabilities, consider these techniques:

1. **Use general instructions first**: Start with broad guidance before providing step-by-step instructions if needed.

2. **Multishot prompting with extended thinking**: Provide examples that demonstrate both the thinking process and desired output.

3. **Debug with extended thinking**: Use Claude's visible thinking process to identify where reasoning went wrong.

4. **Long-form thinking**: For complex tasks, encourage Claude to explore multiple angles and consider different approaches.

5. **Reflection**: Ask Claude to check its work and identify potential issues or improvements.

### Long Context Prompting Tips

When working with large amounts of context:

1. Place the most important information at the beginning and end of your prompt.
2. Use clear section headers and organizational structure.
3. Explicitly tell Claude which parts of the context are most relevant.
4. Ask Claude to summarize its understanding of the context before proceeding with the main task.

### JSON Mode

To increase output consistency, especially when generating structured data:

1. Specify the desired output format in detail
2. Prefill Claude's response with the beginning of the JSON structure
3. Provide examples of the expected format
4. Use retrieval for contextual consistency
5. Chain prompts for complex tasks

---

This document contains a subset of the prompts and guidelines available in Anthropic's documentation. For the full library and more detailed information, visit [Anthropic's documentation website](https://docs.anthropic.com/en/prompt-library/library).
