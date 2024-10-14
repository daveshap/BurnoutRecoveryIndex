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
        body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 20px; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
        .category { font-weight: bold; background-color: #e9e9e9; }
        input[type="radio"] { margin: 0 5px; }
        button { background-color: #4CAF50; color: white; padding: 10px 20px; border: none; cursor: pointer; font-size: 16px; }
        button:hover { background-color: #45a049; }
        #result { margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Burnout Recovery Index</h1>
    <p>When marking this assessment, please use the following guidelines:</p>
    <p>1 - disagree strongly</p>
    <p>2 - disagree somewhat</p>
    <p>3 - neutral/mixed</p>
    <p>4 - agree somewhat</p>
    <p>5 - agree strongly</p>
    <form id="burnoutForm">
        <table>
            <tr>
                <th>Question</th>
                <th>1</th>
                <th>2</th>
                <th>3</th>
                <th>4</th>
                <th>5</th>
            </tr>
'''

    current_category = ''
    with open('burnout_recovery_index.csv', 'r') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            if row['cluster'] != current_category:
                current_category = row['cluster']
                html_content += f'''
            <tr class="category">
                <td colspan="6">{current_category} {row['set']}</td>
            </tr>
'''
            
            html_content += f'''
            <tr>
                <td>{html.escape(row['question'])}</td>
                <td><input type="radio" name="q{row['id']}" value="1" required></td>
                <td><input type="radio" name="q{row['id']}" value="2"></td>
                <td><input type="radio" name="q{row['id']}" value="3"></td>
                <td><input type="radio" name="q{row['id']}" value="4"></td>
                <td><input type="radio" name="q{row['id']}" value="5"></td>
            </tr>
'''

    html_content += '''
        </table>
        <button type="submit">Calculate Scores</button>
    </form>
    <div id="result"></div>

    <script>
    document.getElementById('burnoutForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const categories = [
            'Sleep', 'Work', 'PhysicalHealth', 'MentalHealth', 'EnergyFatigue',
            'SocialRelationships', 'CognitiveFunction', 'MotivationPurpose',
            'EmotionalRegulation', 'SelfCareLeisure', 'StressManagement', 'WorkLifeBalance'
        ];
        
        let scores = {};
        let totalScore = 0;

        categories.forEach((category, index) => {
            let categoryScore = 0;
            for (let i = index * 20 + 1; i <= (index + 1) * 20; i++) {
                const value = parseInt(document.querySelector(`input[name="q${i}"]:checked`).value);
                categoryScore += (i % 20 <= 10) ? value : (6 - value); // Reverse scoring for Set B
            }
            const normalizedScore = ((categoryScore - 20) / 80) * 100;
            scores[category] = normalizedScore;
            totalScore += normalizedScore;
        });

        const aggregateScore = totalScore / categories.length;

        let resultHTML = '';
        categories.forEach(category => {
            resultHTML += `<p>${category.replace(/([A-Z])/g, ' $1').trim()} Category Score: ${scores[category].toFixed(2)} / 100</p>`;
        });
        resultHTML += `<p>Aggregate Score: ${aggregateScore.toFixed(2)} / 100</p>`;

        document.getElementById('result').innerHTML = resultHTML;
    });
    </script>
</body>
</html>
'''

    with open('widget.html', 'w') as htmlfile:
        htmlfile.write(html_content)

if __name__ == '__main__':
    generate_html()
