# ComSci-Salary-Explorer
ComSci Salary Explorer is a python-based report generator designed to explore the 2025 computer science job market, discovering insights into salaries, job growth, and demand across the tech industry US and Canada. 
## Before you start
### 1. Python Libraries
Python 3.9 or higher is recommended
Users must install the following Python packages:
```
pip install pandas matplotlib numpy
```
### 2. External Dependencies
pdfLaTeX is required for PDF reports generation
If PDF reports are desired, for Mac users:
```
brew install basictex
```
Windows users:
Download and install MiKTeX from the official website.

### 3. Dataset
ComSci Salary Explorer is based on a 2025 dataset from Kaggle, so users will need to download this dataset first:
Shamim, A. Data Science, AI & ML Job Salaries in 2025. Kaggle.com. https://www.kaggle.com/datasets/adilshamim8/salaries-for-data-science-jobs. ‌

## Report Generation
ComSci Salary Explorer provides an interactive menu that allows users to explore trends in computer science job roles, salaries, and work modes across different experience levels. Each menu option triggers a specific visualization or analysis. Users can request any combinations of the following analyses to be incorporated into the final report generated:

### 1. Job Title Distribution by Category
Displays the distribution of computer science job titles grouped by category for selected experience levels. This visualization helps identify which job categories are most common at different career stages.

### 2. Salary Comparison by Job Category
Compares salaries across different job title categories within selected experience levels, allowing users to assess how compensation varies by role and seniority.

### 3. Overall Salary Distribution
Shows the overall salary distribution across all experience levels, providing a high-level view of compensation trends in the computer science job market.

### 4. Job Title Counts by Experience Level
Visualizes the frequency of job titles for selected experience levels, highlighting how role availability changes as experience increases.

### 5. Work Mode Distribution
Analyzes the distribution of work modes (e.g., remote, hybrid, on-site) across all experience levels, offering insight into workplace flexibility in the industry.
