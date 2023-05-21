
# TDD Cycle Implementation using Gradle and Github

The problem statement was to Create a function add and multiply that takes a String and returns a String with certain test cases mentioned in the Assignment's Problem statement

The actuals task was to implement TDD cycle using gradle so i used Python with Gradle to solve the given problem statement below are the detailed steps how i implemented TDD life cycle
## Run Locally

Clone the project

```bash
  git clone https://github.com/saifltr/ESTECO_TDD.git
```

Go to the project directory

```bash
 cd ESTECO_TDD
```

Install required packages

```bash
  pip install requirements.txt

```

Run the project

```bash
  python StringCalculator.py
```

Build the gradle 

```bash
  gradle build
```

Test he Gradle build 

```bash
  gradle testPython
```
## Code Output
Run the Python File to check if test cases working Correctly

```bash
  python StringCalculator.py
```

![App Screenshot](https://i.ibb.co/fNg2jrp/image.png)


Check the test cases with Gradle 

```bash
  gradle testPython
```

![App Screenshot](https://i.ibb.co/W309Zm2/image.png)


## Workflow
I have 3 branches on this repo as follows

-**main-app**: It is the main branch to merge all the features to be be publishes on production branch

I created another 2 branches to develop 2 features seperatly that is creating an **add() function** and **multiply() function** seperatly as a feature

-**feature/addString**: I created this branch to develop add function seperately and to test it

-**feature/multiplyString**: I created this branch to develop and test the multiply function alongside the add function in it which is finally merged to main branch



So to understand how actually it works i have created gradle file to check the test cases everytime a new feature is added


```python
def test_add_one_number(self):
        input_str = "1"
        expected_output = "1"
        actual_output = StringCalculator.add(input_str)
```

Each time whenever a function is created that adds one number the test_add_one_number() function tests it and then merges the feature if all test cases passes belonging to it passes

So to implement it correctly on the version control system with TDD cycle i created a workflow on github that initializes certain checks everytime i commit the changes

The workflow is implemented on main branch i.e main-app you can directly check it in actions tab

```yaml
name: Continuous Integration

on:
  push:
    branches:
      - main-app
  pull_request:
    branches:
      - main-app

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: python3 StringCalculator.py
```

It works in the following way:

![App Screenshot](https://developer.ibm.com/developer/default/articles/5-steps-of-test-driven-development/images/tdd-red-green-refactoring-v3.png)
