# Contribution Guidelines

Thank you for considering contributing to our project! We welcome contributions from everyone. Before you start, please take a moment to review these guidelines to ensure your contributions are aligned with the project’s goals.

## How to Contribute

### 1. Fork the Repository
Fork the repository by clicking the "Fork" button on the top right of the repository page. This creates a copy of the repository under your GitHub account.

### 2. Clone Your Fork
Clone the forked repository to your local machine. Replace `your-username` with your GitHub username.

        <!-- ```bash -->
        git clone https://github.com/your-username/gurkhageeks.git


### 3. Create a New Branch
Create a new branch for your feature or bug fix. Use a descriptive name for the branch.
    
        ```bash
        git checkout -b feature/amazing-feature

### 4. Make Your Changes
Make the necessary changes in your local branch. Ensure your code follows the project's coding standards.

### 5. Commit Your Changes
Commit your changes with a clear and descriptive commit message. Use the following conventions:

feat: for new features.
fix: for bug fixes.
Example Commit Messages:

feat: add user authentication
fix: resolve issue with login form validation

    <!-- ```bash -->
    git add .
    git commit -m "feat: add amazing feature"


### 6. Push Your Changes
Push the changes to your forked repository.

    <!-- ```bash -->
    git push origin feature/amazing-feature

### 7. Submit a Pull Request
Go to the original repository on GitHub and click on the "Pull Request" button. Choose the branch you just pushed to and submit your PR.

    
## Guidelines for Sending a PR
1. Ensure your code passes all tests.
2. Include a clear and detailed description of the changes.
3. Reference any relevant issues or tickets.
4. Make sure your code is well-commented, especially in complex sections.
5. Keep your pull request small and focused. Larger pull requests are more difficult to review.
6. If your PR is not ready for review, create it as a "Draft" pull request.


# Pull Request Template
When you submit a pull request, please include the following details in the PR description:

## Description
A brief description of the changes made in this PR.

## Related Issue
Link to the related issue (e.g., #123).

## Motivation and Context
Why is this change required? What problem does it solve?

## How Has This Been Tested?
Describe the tests that you ran to verify your changes. Include any relevant details for your testing setup.

- [ ] Test A
- [ ] Test B

## Screenshots (if appropriate):

## Types of Changes
What types of changes does your code introduce? Put an `x` in all the boxes that apply:
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update

## Checklist
Go over all the following points, and put an `x` in all the boxes that apply. If you're unsure about any of these, don't hesitate to ask.
- [ ] My code follows the code style of this project.
- [ ] My change requires a change to the documentation.
- [ ] I have updated the documentation accordingly.
- [ ] I have added tests to cover my changes.
- [ ] All new and existing tests passed.
- [ ] I have checked my code and corrected any misspellings.
- [ ] I have added a `Changelog` entry for my changes.

## Further Comments
If this is a large or complex change, start the conversation by explaining why you chose the solution you did and what alternatives you considered, etc.

## Instructions for Using the PR Template
1. Copy and paste the template above into the description of your pull request.
2. Fill out each section with the relevant details.
3. Remove any sections that are not applicable to your changes.




