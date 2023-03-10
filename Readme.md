# Textify

Textify is a script for generating the raw text equivalent of a software repository, to give tools like ChatGPT better access to context of projects.

## Installation

1. Clone the repository to your local machine.
2. Navigate to the root of the cloned repository.
3. Run the following command to add Textify to your PATH:

   ```sh
   export PATH="$PATH:$PWD"
    ```
Note: this will add Textify to your PATH temporarily. If you want to add it permanently, add the above line to your shell profile file (e.g. ~/.bash_profile or ~/.zshrc).

## Usage

To use Textify, navigate to the root of the project you want to textify and run the following command:

```sh
textify
```
