import csv
import html

def generate_html():
    html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Burnout Recovery Index</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; table-layout: fixed; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .category { font-weight: bold; background-color: #e9e9e9; }
        .question-col { width: 300px; }
        .radio-col { width: 40px; text-align: center; }
        input[type="radio"] { margin: 0; }
        button { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; font-size: 16px; margin-right: 10px; }
        button:hover { background-color: #45a049; }
        #result { margin-top: 20px; font-weight: bold; }
        #debugButton1 { background-color: #ff6666; }
        #debugButton2 { background-color: #ffcc66; }
        #debugButton3 { background-color: #007bff; }
        #debugButton4 { background-color: #66cc66; }
        #debugButton5 { background-color: #6666cc; }
        #debugButtonRandom { background-color: #ff9800; }
    </style>
</head>
<body>
    <h1>Burnout Recovery Index</h1>
    <p>When marking this assessment, please use the following guidelines:</p>
    <p>1 - disagree strongly, 2 - disagree somewhat, 3 - neutral/mixed, 4 - agree somewhat, 5 - agree strongly</p>
    <form id="burnoutForm">
        <table>
            <tr>
                <th class="question-col">Question</th>
                <th class="radio-col">1</th>
                <th class="radio-col">2</th>
                <th class="radio-col">3</th>
                <th class="radio-col">4</th>
                <th class="radio-col">5</th>
            </tr>
'''

    current_category = ''
    with open('questions.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if row['cluster'] != current_category:
                current_category = row['cluster']
                # Add logic for distinguishing between Set A and Set B
                if "positive" in row['cluster'].lower():
                    section_label = f"{current_category} (Set A)"
                else:
                    section_label = f"{current_category} (Set B)"
                html_content += f'''
            <tr class="category">
                <td colspan="6">{section_label}</td>
            </tr>
'''
            html_content += f'''
            <tr>
                <td class="question-col">{html.escape(row['question'])}</td>
                <td class="radio-col"><input type="radio" name="q{row['id']}" value="1" required></td>
                <td class="radio-col"><input type="radio" name="q{row['id']}" value="2"></td>
                <td class="radio-col"><input type="radio" name="q{row['id']}" value="3"></td>
                <td class="radio-col"><input type="radio" name="q{row['id']}" value="4"></td>
                <td class="radio-col"><input type="radio" name="q{row['id']}" value="5"></td>
            </tr>
'''

    html_content += '''
        </table>
        <button type="submit">Generate Score</button>
        <button type="button" id="debugButton1">Debug (Set All to 1)</button>
        <button type="button" id="debugButton2">Debug (Set All to 2)</button>
        <button type="button" id="debugButton3">Debug (Set All to 3)</button>
        <button type="button" id="debugButton4">Debug (Set All to 4)</button>
        <button type="button" id="debugButton5">Debug (Set All to 5)</button>
        <button type="button" id="debugButtonRandom">Debug (Random Values)</button>
    </form>
    <div id="result"></div>

    <script>
        document.getElementById('burnoutForm').addEventListener('submit', function(e) {
            e.preventDefault();

            const categories = [
                'Sleep', 'Work', 'Physical Health', 'Mental Health', 'Energy and Fatigue',
                'Social Relationships', 'Cognitive Function', 'Motivation and Purpose',
                'Emotional Regulation', 'Self-Care and Leisure', 'Stress Management', 'Work-Life Balance'
            ];

            const reverseScoredQuestions = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]; // Example reverse-scored IDs
            let scores = {};
            let totalScore = 0;

            categories.forEach((category, index) => {
                let categoryScore = 0;
                for (let i = index * 20 + 1; i <= (index + 1) * 20; i++) {
                    const value = parseInt(document.querySelector(`input[name="q${i}"]:checked`).value);
                    if (reverseScoredQuestions.includes(i % 20)) {
                        categoryScore += (6 - value); // Reverse score for specific questions
                    } else {
                        categoryScore += value;
                    }
                }
                const normalizedScore = ((categoryScore - 20) / 80) * 100;
                scores[category] = normalizedScore;
                totalScore += normalizedScore;
            });

            const aggregateScore = totalScore / categories.length;

            let resultHTML = '';
            categories.forEach(category => {
                resultHTML += `<p>${category} Category Score: ${scores[category].toFixed(2)} / 100</p>`;
            });
            resultHTML += `<p>Aggregate Score: ${aggregateScore.toFixed(2)} / 100</p>`;

            document.getElementById('result').innerHTML = resultHTML;
        });

        // Debug function to auto-populate the form with a specific value
        function setAllValues(value) {
            const inputs = document.querySelectorAll(`input[type="radio"][value="${value}"]`);
            inputs.forEach(input => {
                input.checked = true;
            });
            alert(`Form auto-populated with all values set to ${value}.`);
        }

        document.getElementById('debugButton1').addEventListener('click', function() {
            setAllValues(1);
        });
        document.getElementById('debugButton2').addEventListener('click', function() {
            setAllValues(2);
        });
        document.getElementById('debugButton3').addEventListener('click', function() {
            setAllValues(3);
        });
        document.getElementById('debugButton4').addEventListener('click', function() {
            setAllValues(4);
        });
        document.getElementById('debugButton5').addEventListener('click', function() {
            setAllValues(5);
        });

        // Debug function to auto-populate the form with random values
        document.getElementById('debugButtonRandom').addEventListener('click', function() {
            const totalQuestions = document.querySelectorAll('input[type="radio"]').length / 5; // Get total number of questions by dividing radio inputs by 5
            for (let i = 1; i <= totalQuestions; i++) {
                const randomValue = Math.floor(Math.random() * 5) + 1; // Random value between 1 and 5
                const randomInput = document.querySelector(`input[name="q${i}"][value="${randomValue}"]`);
                if (randomInput) {
                    randomInput.checked = true;
                }
            }
            alert('Form auto-populated with random values.');
        });
    </script>
</body>
</html>
'''

    with open('widget.html', 'w') as htmlfile:
        htmlfile.write(html_content)

if __name__ == '__main__':
    generate_html()
