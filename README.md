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

The **Interactive Terminal Spell Checker** is a command-line utility built to automate the detection and correction of typographical errors in plaintext. This application provides a lightweight, highly responsive, keyboard-driven environment that operates entirely within a terminal shell.

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
+---------------------------------------+
             |       Initialize Application          |
             |      (main.py / result_class.py)      |
             +-------------------+-------------------+
                                 |
                                 v
             +---------------------------------------+
             |       Load Reference Dictionary       |
             |        (O(1) Hash Set Lookup)         |
             +-------------------+-------------------+
                                 |
                                 v
             +---------------------------------------+
             |   Ingest Source Text (File or CLI)    |
             +-------------------+-------------------+
                                 |
                                 v
             +---------------------------------------+
             |       Tokenize & Parse Words          |
             |         (spell_checker.py)            |
             +-------------------+-------------------+
                                 |
                                 v
             +---------------------------------------+
             |  Isolate Typos into Circular List     |
             |          (word_list.py)               |
             +-------------------+-------------------+
                                 |
                                 v
             +---------------------------------------+
             |    Interactive Navigation Menu        |
             |      (selection_of_word.py)           |
             +----------+-----------------+----------+
                        |                 |
                        v                 v
         +-----------------------+   +-----------------------+
         | Compute Edit Distance |   | Commit String Changes |
         |   (suggestions.py)    |   |  & Export File State  |
         +-----------------------+   +-----------------------+
   <p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section lists the fundamental building blocks used to bootstrap your project. This tool relies cleanly on pure Python core architecture and native system libraries to provide execution portability without bulky platform stacks.

* [Python](https://www.python.org/) - Built using core standard runtimes (Core built-in libraries: `string`, `time`, `typing`).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

Follow these simple structural instructions to establish a local copy of this interactive shell environment up and running smoothly.

### Prerequisites

This environment relies entirely on standard built-in execution mechanics. There are no heavy third-party distribution packages to compile.
* **Python 3.10+** (Ensure Python is initialized inside your global system path variables).

### Installation

1. Clone the repository:
   ```sh
   git clone [https://github.com/github_username/repo_name.git](https://github.com/github_username/repo_name.git)
Verify your folder structure matches the modular script composition:

Plaintext
.
├── main.py
├── input_handler.py
├── result_class.py
├── selection_of_word.py
├── spell_checker.py
├── suggestions.py
└── word_list.py
Establish a standard wordlist text file inside a dictionaries subdirectory:

Bash
mkdir dictionaries
# Place your target word file at dictionaries/words_alpha.txt
Usage
Run the primary automation layer directly inside your console terminal shell:

Bash
python main.py
Step-by-Step Operation Guide
Choose a Dictionary File: Choose option a to route towards a custom vocabulary asset path, or option b to deploy the standard reference set.

Provide Raw Content Data: Select option a to provide a local .txt file path, or option b to write text directly into the open shell prompt.

Execute Correction Menu: If spelling errors are identified, the terminal launches the active edit interface.

Interactive Terminal Key Controls
When interacting with the main typo modification engine, manage processing loops using these input controls:

d: Navigate forward/rightward to inspect the next logged spelling error.

a: Navigate backward/leftward to review a previous spelling error.

w: Show an index table list tracking every active spelling failure.

s: Focus on the current active word to generate spelling recommendations.

c: Search for a specific misspelled word token string within the array.

i: Review the current state of your complete text block.

q: Terminate active processing blocks and exit the program safely.

Sub-Selection Menu Keys (Active Word Modification)
Once you press s on an active typo string, the calculation module generates suggestions using the Damerau-Levenshtein alignment matrix:

1, 2, 3...: Enter the numeric key corresponding to a suggestion to replace the text mismatch.

m: Paginate forward to display more word suggestions (displays 5 items per screen view).

l: Paginate backward to reveal preceding word suggestions.

d: Add the active typo directly into the active dictionary cache to prevent future alerts.

c: Type out a custom string replacement manually.

r: Erase the targeted word flag from the spelling queue without modifying the underlying text.

b: Reverse execution state back towards the previous structural tracking interface.
