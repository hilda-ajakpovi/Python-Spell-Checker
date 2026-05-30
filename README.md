# Python-Spell-Checker
This program spell checks every word in a given input based on a standard dictionary or a given dictionary
Workflow for interface:
- Allow user to upload their own dictionary or use standard one
- User decides if they want to upload a file or type in something to spell check.
- The program will parse the string and spell check each word and return how many spelling errors that there are.
- The user will then be prompted to either fix all errors with the number one suggested word for each mispelled word, select a word to see suggested words and have the option to replace and then loop through the words (either going forward or backwards) to see suggested words for those words and possibly replace. For every mispelled word, the user is also allowed to add the word to the dictionary for future use.
- The user can also start from the first word for the loop.
- Once user is done with this string (If file, the user will have an option to write the edited input back to the file), they can either do this again with a new file/input or quit the program. 


# Interactive Terminal Spell Checker

## 📖 Project Overview & Real-World Use Cases

The **Interactive Terminal Spell Checker** is a professional-grade, command-line utility built to automate the detection and correction of typographical errors in plaintext assets. Instead of forcing users to rely on resource-heavy, graphical word processors, this application provides a lightweight, highly responsive, keyboard-driven environment that operates entirely within a terminal shell.

### What It Does
At its core, the program ingests source text (either directly typed into the prompt or loaded from a `.txt` file), strips out formatting to isolate individual words, and cross-references them against an optimized dictionary database. When it catches a misspelled word, it doesn't just flag it—it calculates the most statistically likely corrections using advanced natural language processing strings and opens a structural menu allowing the operator to selectively fix or track errors.

### Real-World Use Cases
* **Server-Side Document Editing**: Perfect for system administrators or developers working over SSH on remote headless servers who need to quickly verify documentation files, scripts, or markdown assets before deployment.
* **Lightweight Text Verification**: Serves as an excellent alternative for writers, developers, and researchers who prefer distraction-free terminal text editors (like Vim, Nano, or Emacs) and need a standalone command-line pipeline to sanitize text strings.
* **Educational Codebase Reference**: Demonstrates clean implementations of modular software architecture, circular list data structures, custom text tokenization engines, and dynamic programming string alignment algorithms.

---

<a name="readme-top"></a>

<br />
<div align="center">
  <h3 align="center">Interactive Terminal Spell Checker</h3>

  <p align="center">
    A robust command-line terminal utility featuring automated text tokenization, dictionary validation, and live typo correction workflows using the Damerau-Levenshtein edit distance algorithm.
    <br />
    <a href="#usage"><strong>Explore the Docs »</strong></a>
    <br />
    <br />
    <a href="#usage">View Demo</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/repo_name/issues">Request Feature</a>
  </p>
</div>

## About The Project

There are many great README templates available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a README template so amazing that it'll be the last one you ever need -- I think this is it.

Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others.
* You shouldn't be doing the same tasks over and over like creating a README from scratch.
* You should implement DRY (Don't Repeat Yourself) principles to the rest of your life 😄

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people who have contributed to expanding this template!

### Program Core Concepts & Overview
This terminal software serves as an interactive spell checking tool for plaintext assets. It isolates individual string words, references them against an optimized lookup vocabulary set, caches spelling anomalies inside a localized data structure, and gives the operator real-time correction choices.

#### Data Ingestion & Program Flow
The workflow runs through an absolute execution order across specialized modular files:
1. **Dictionary Selection (`main.py` & `input_handler.py`)**: The script initializes by prompting the user to load a custom reference lexicon or default to the local `words_alpha.txt` compilation file.
2. **Target File Ingestion**: The operator inputs raw string blocks or provides a system path to an external text asset.
3. **Word Tokenization (`spell_checker.py`)**: The input stream passes through character scanning routines to separate alphabetical terms while preserving interior special characters like hyphens and apostrophes.
4. **Validation Filter**: Validated words undergo comparative matching against the reference dataset with continuous O(1) verification speed. Unmatched terms are logged directly into a tracking list.
5. **Interactive UI (`selection_of_word.py` & `word_list.py`)**: Users navigate spelling mismatches via text-based choice selectors, utilizing a dynamic calculation algorithm to paginate word correction options.
6. **Persistence Saving**: Corrected text modifications update the terminal screen and append directly back onto storage disks.
