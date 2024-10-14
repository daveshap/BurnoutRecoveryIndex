import csv

# Generate HTML widget from a CSV file containing questions
def generate_widget(questions_file):
    # Read the CSV file to load questions
    with open(questions_file, "r", encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        questions = list(reader)

    # Group questions by category and set type (A or B)
    categories = {}
    for question in questions:
        _, category, question_type, question_text = question  # Expecting four columns as provided
        if category not in categories:
            categories[category] = {'A': [], 'B': []}
        categories[category][question_type].append(question_text)

    # Generate HTML for the widget
    html_content = """
    <html>
    <head>
        <style>
            body {
                font-family: Arial, sans-serif;
            }
            table {
                width: auto;
                border-collapse: collapse;
            }
            th, td {
                padding: 10px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
            td.question {
                width: 300px;
            }
            button {
                margin: 5px;
                padding: 10px;
                font-size: 14px;
            }
            .section-header {
                background-color: #e0e0e0;
                font-weight: bold;
            }
            .question-row:nth-child(even) {
                background-color: #f9f9f9;
            }
            .question-row:nth-child(odd) {
                background-color: #e6f7ff;
            }
        </style>
        <script>
            function calculateScore() {
                let categoryScores = {};
                let categoryCounts = {};
                
                let inputs = document.querySelectorAll('input[type=radio]:checked');
                
                inputs.forEach(input => {
                    let category = input.name.split('-')[0];
                    let questionType = input.dataset.type;
                    let value = parseInt(input.value);
                    
                    if (!categoryScores[category]) {
                        categoryScores[category] = 0;
                        categoryCounts[category] = 0;
                    }
                    
                    // Handle reverse scoring if question is type 'B'
                    if (questionType === 'B') {
                        value = 6 - value;
                    }
                    
                    categoryScores[category] += value;
                    categoryCounts[category] += 1;
                });
                
                let results = '';
                let totalScore = 0;
                let categories = Object.keys(categoryScores);
                
                categories.forEach(category => {
                    let rawScore = categoryScores[category];
                    let questionCount = categoryCounts[category];
                    let minPossibleScore = questionCount * 1;
                    let maxPossibleScore = questionCount * 5;
                    
                    // Normalize score to percentage
                    let normalizedScore = ((rawScore - minPossibleScore) / (maxPossibleScore - minPossibleScore)) * 100;
                    totalScore += normalizedScore;
                    results += `${category} Category Score: ${normalizedScore.toFixed(2)} / 100<br>`;
                });
                
                let aggregateScore = totalScore / categories.length;
                results += `<br>Aggregate Score: ${aggregateScore.toFixed(2)} / 100`;
                
                document.getElementById('results').innerHTML = results;
            }

            function debugSetAll(value) {
                let inputs = document.querySelectorAll('input[type=radio]');
                
                inputs.forEach(input => {
                    let questionType = input.dataset.type;
                    if ((questionType === 'A' && value === parseInt(input.value)) || (questionType === 'B' && (6 - value) === parseInt(input.value))) {
                        input.checked = true;
                    }
                });
            }
        </script>
    </head>
    <body>
        <h2>Burnout Recovery Index</h2>
        <p>When marking this assessment, please use the following guidelines:</p>
        <ul>
            <li>1 - disagree strongly</li>
            <li>2 - disagree somewhat</li>
            <li>3 - neutral/mixed</li>
            <li>4 - agree somewhat</li>
            <li>5 - agree strongly</li>
        </ul>
        <form>
            <table>
                <tr>
                    <th>Question</th>
                    <th>1</th>
                    <th>2</th>
                    <th>3</th>
                    <th>4</th>
                    <th>5</th>
                </tr>
    """

    # Generate the question rows for each category and set
    for category, sets in categories.items():
        for set_type, questions in sets.items():
            html_content += f"<tr class='section-header'><td colspan='6'>{category} - Set {set_type}</td></tr>"
            for idx, question_text in enumerate(questions):
                if set_type == 'A':
                    values = [1, 2, 3, 4, 5]
                elif set_type == 'B':
                    values = [5, 4, 3, 2, 1]

                html_content += f"""
                    <tr class="question-row">
                        <td class="question">{question_text}</td>
                        <td><input type="radio" name="{category}-{set_type}-{idx}" value="{values[0]}" data-type="{set_type}"></td>
                        <td><input type="radio" name="{category}-{set_type}-{idx}" value="{values[1]}" data-type="{set_type}"></td>
                        <td><input type="radio" name="{category}-{set_type}-{idx}" value="{values[2]}" data-type="{set_type}"></td>
                        <td><input type="radio" name="{category}-{set_type}-{idx}" value="{values[3]}" data-type="{set_type}"></td>
                        <td><input type="radio" name="{category}-{set_type}-{idx}" value="{values[4]}" data-type="{set_type}"></td>
                    </tr>
                """

    # Close the HTML content
    html_content += """
            </table>
            <br>
            <button type="button" onclick="calculateScore()">Generate Score</button>
            <button type="button" onclick="debugSetAll(1)">Debug (Set All to 1)</button>
            <button type="button" onclick="debugSetAll(2)">Debug (Set All to 2)</button>
            <button type="button" onclick="debugSetAll(3)">Debug (Set All to 3)</button>
            <button type="button" onclick="debugSetAll(4)">Debug (Set All to 4)</button>
            <button type="button" onclick="debugSetAll(5)">Debug (Set All to 5)</button>
        </form>
        <div id="results"></div>
    </body>
    </html>
    """

    # Write HTML content to file
    with open('widget.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

# Generate the widget HTML
if __name__ == "__main__":
    generate_widget('questions.csv')