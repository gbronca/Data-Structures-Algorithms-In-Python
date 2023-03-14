# Data Structures and Algorithms in Python

- [Data Structures and Algorithms in Python](#data-structures-and-algorithms-in-python)
  - [Overview](#overview)
  - [Big-O Notation](#big-o-notation)
  - [Interview: How to Solve Problems](#interview-how-to-solve-problems)
    - [What Are Companies Looking For?](#what-are-companies-looking-for)
    - [Step By Step through a problem](#step-by-step-through-a-problem)
  - [Data Structures](#data-structures)
    - [Arrays](#arrays)
  - [Algorithms](#algorithms)

## Overview

This repository contains Python implementations of various data structures and algorithms. The implementations are meant to be educational, so they may be less efficient than the implementations in the Python standard library. Each data structure or algorithm is implemented in its own module, which contains a class with a corresponding name. The corresponding test cases are in the tests module.

## [Big-O Notation](/Big-O%20Notation/big-o.md)

## Interview: How to Solve Problems

### What Are Companies Looking For?

- **Analytical Skills** - How can you think through problems and analyse things?
- **Coding Skills** Is your code clean, simple, organised and easy to read?
- **Technical Skills/Knowledge** - Do you know the fundamentals of the job you're applying for? Do you just memorise things or do you undertand the concepts, the pros and cons of different solutions?
- **Communication Skills** - Does your personality fit the company culture? Can you communicate well with others?

[Technical Interview Mindmap](https://coggle.it/diagram/W5E5tqYlrXvFJPsq/t/master-the-interview-click-here-for-course-link/c25f98c73a03f5b1107cd0e2f4bce29c9d78e31655e55cb0b785d56f0036c9d1)

### Step By Step through a problem

1. When the interviewer says the question, write down the key points at the top (i.e. sorted array). Make sure you have all the details. Show how organised you are.
2. Make sure you double-check: What are the inputs? What are the outputs?
3. What is the most important value of the problem? Do you have time, and space and memory, etc.. What is the main goal?
4. Don't be annoying and ask too many questions.
5. Start with the naive/brute force approach. The first thing that comes to mind. It shows that you’re able to think well and critically (you don't need to write this code, just speak about it).
6. Tell them why this approach is not the best (i.e. O(n^2) or higher, not readable, etc...)
7. Walk through your approach, comment on things and see where you may be able to break things. Any repetition, bottlenecks like O(N^2), or unnecessary work? Did you use all the information the interviewer gave you? Bottleneck is the part of the code with the biggest Big O. Focus on that. Sometimes this occurs with repeated work as well.
8. Before you start coding, walk through your code and write down the steps you are going to follow.
9. Modularize your code from the very beginning. Break up your code into beautiful small pieces and add just comments if you need to.
10. Start actually writing your code now. Keep in mind that the more you prepare and understand what you need to code, the better the whiteboard will go. So never start a whiteboard interview not being sure of how things are going to work out. That is a recipe for disaster. Keep in mind: A lot of interviews ask questions that you won’t be able to fully answer on time. So think: What can I show in order to show that I can do this and I am better than other coders? Break things up in Functions (if you can’t remember a method, just make up a function and you will at least have it there). Write something, and start with the easy part.
11. Think about error checks and how you can break this code. Never make assumptions about the input. Assume people are trying to break your code and that Darth Vader is using your function. How will you safeguard it? Always check for false inputs that you don’t want. Here is a trick: Comment in the code, the checks that you want to do… write the function, then tell the interviewer that you would write tests now to make your function fail (but you won't need to actually write the tests)
12. Don’t use bad/confusing names like i and j. Write code that reads well.
13. Test your code: Check for no params, 0, undefined, null, massive arrays, async code, etc… Ask the interviewer if we can make assumption about the code. Can you make the answer return an error? Poke holes into your solution. Are you repeating yourself?
14. Finally, talk to the interviewer about where you would improve the code. Does it work? Are there different approaches? Is it readable? What would you google to improve? How can performance be improved? Possibly: Ask the interviewer what was the most interesting solution you have seen to this problem.
15. If your interviewer is happy with the solution, the interview usually ends here. It is also common that the interviewer asks you extension questions, such as how you would handle the problem if the whole input is too large to fit into memory, or if the input arrives as a stream. This is a common follow-up question at Google, where they care a lot about scale. The answer is usually a divide-and-conquer approach — perform distributed processing of the data and only read certain chunks of the input from disk into memory, write the output back to disk and combine them later.

[Google Interview Video](https://www.youtube.com/watch?v=XKu_SEDAykw)

## Data Structures

### Arrays

## Algorithms
