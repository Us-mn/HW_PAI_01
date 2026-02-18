# Homework: CSV Data Processing for AI

## Objective
Real-world AI data is "dirty." Your goal is to write a robust script that extracts numeric data from a CSV while ignoring non-numeric errors.

## Task
Complete the function `get_average_score` in `csv_processor.py`:
1. Open `data.csv` using `csv.reader`.
2. Skip the header row.
3. Access the **Score** column at **index 2**.
4. Use a `try-except` block to convert values to floats.
5. Ignore any rows that trigger a `ValueError` (like the "invalid" entry).
6. Return the average of all valid scores as a float.

## Local Testing (Visual Lab)
Before submitting, use the **VS Code Testing Lab** to verify your logic:
1. Click the **Beaker Icon** on the left sidebar.
2. If prompted, click **Configure Python Tests** -> **unittest** -> **Root Directory** -> **test_*.py**.
3. Click the **Play (▷)** button next to the test name.
   - **Green Check:** Your logic is correct.
   - **Red Cross:** Click the test to see the error (e.g., `Expected 70.5 but got 0.0`).

## Submission
1. **Save** your changes in VS Code.
2. Use **GitHub Desktop** to Commit and **Push** your work.
3. Verify the **Green Checkmark** appears on your GitHub repository web page.

*Note: `data.csv` and `test_csv_processor.py` are protected. Do not attempt to modify them to pass the tests; fix your logic in `csv_processor.py` instead.*
