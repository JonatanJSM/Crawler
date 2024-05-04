# Crawler
<p align="center">
<a href="#" target="blank"><img src="https://github.com/Daniel-Pliego/Proyecto_BRIW/blob/develop/resources/Uzumaki_Symbole.png" width="200" alt="equipo" /></a>
</p>
<p align="center">Clean Architecture</p>
<p align="center">

## Description

This is a [Python](https://www.python.org/) project

## Getting Started

First, run the development server:

```bash
uvicorn main:app --reload
```

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.


# Ways of working

This section serves as a guide to ensure good code quality and collaboration practices within our development environment.

Before You Start Working
Before diving into any coding tasks, it's essential to ensure that you follow these guidelines:

- **Code Quality Assurance:** We prioritize maintaining high code quality standards throughout the project. Please adhere to best practices and coding conventions outlined in our style guide, Make sure you have enabled the [ESLint extension](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) in your editor.

- **Testing:** Write comprehensive tests for all new features and ensure that existing tests remain passing. Test-driven development (TDD) is encouraged to promote reliability and stability in the codebase.

## Commit Guidelines
When making commits, please follow these guidelines:

- **Format**: Commits follow [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) conventions followed by a Ticket number.
   For example if your ticket is TS123 then your commit would look like:
   ```
   feat: describe your changes (TS123)
   ```
   Allowed prefixes are:
   - `feat`: for a new feature for the user.
   - `fix`: for a bug fix for the user, not a fix to a build script.
   - `chore`: Changes to t auxiliary tools and libraries such as documentation generation
   - `ci`: Changes to CI/CD tools such as jenkins or github actions.
   - `docs`: for changes to the documentation.
   - `style`: for formatting changes, missing semicolons, etc (NOT CSS).
   - `refactor`: for refactoring production code, e.g. renaming a variable.
   - `perf`: for performance improvements.
   - `test`: for adding missing tests, refactoring tests; no production code change.
   - `build`: [RESERVED FOR RELEASES] for deploying new builds.

- **Atomic Commits:** Keep commits focused on a single logical change. Avoid bundling unrelated changes within a single commit.

## Pull Request Guidelines
When creating a pull request, adhere to the following guidelines:

- **Single Commit:** Is desired that each pull request contains __**only one commit**__. This ensures that the changes are well-segmented and easier to review. Only in extreme cases where the change is big then is allowed multiple commits

- **Rebase Merge Strategy**: Use the rebase merge strategy when merging your changes into the main branch. This helps maintain a clean and linear commit history. If PR has more than 1 commit use Merge Commit strategy

- **Review and Approval:** Every pull request should have at least two approvals from team members before it can be merged. Peer review is crucial for maintaining code quality and knowledge sharing.

## Testing
All code changes must pass the existing test suite. Additionally, ensure that new code is accompanied by relevant tests to cover both positive and edge cases.
