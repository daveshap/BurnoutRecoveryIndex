# Burnout Recovery Index




## Purpose
This project aims to create a reliable self-assessment inventory to measure burnout without medical interventions. The Burnout Recovery Index provides individuals with an objective tool to assess their current level of burnout and track changes over time.



## Disclaimer

Burnout is generally not recognized by the medical establishment. This tool is meant for informational purposes only, and is not meant to replace or supplement medical diagnosis or treatment. Always seek health advice from trained and licensed medical professionals. 



## Methodology
The assessment is based on:
- Likert-scale questions (1-5 rating)
- Bipolar question pairs (positive and negative framing)
- Split-half consistency to reduce response bias
- 12 categories of symptoms typically associated with burnout

This approach helps overcome agreement bias and provides a more accurate picture of an individual's burnout state.






## Categories
The assessment covers 12 key areas associated with burnout:

1. **Sleep**: Sleep disturbances are often early indicators of burnout. This category assesses sleep quality, duration, and the restorative nature of rest.
2. **Work**: Work-related stress is a primary contributor to burnout. This section evaluates job satisfaction, workload management, and professional relationships.
3. **Physical Health**: Burnout can manifest in physical symptoms. This category covers general health, energy levels, and physical resilience.
4. **Mental Health**: Psychological well-being is crucial in burnout assessment. This section addresses mood, anxiety, and overall mental state.
5. **Energy and Fatigue**: Chronic fatigue is a hallmark of burnout. This category measures energy levels, motivation, and the ability to complete daily tasks.
6. **Social Relationships**: Burnout can significantly impact social interactions. This section evaluates the quality and frequency of social connections.
7. **Cognitive Function**: Mental exhaustion can affect cognitive abilities. This category assesses focus, memory, and decision-making capabilities.
8. **Motivation and Purpose**: Loss of motivation is common in burnout. This section explores sense of purpose, goal-setting, and overall life satisfaction.
9. **Emotional Regulation**: Burnout can lead to emotional instability. This category evaluates emotional awareness and control.
10. **Self-Care and Leisure**: Neglecting self-care often accompanies burnout. This section assesses engagement in relaxation and personal interests.
11. **Stress Management**: The ability to cope with stress is crucial. This category measures stress perception and management techniques.
12. **Work-Life Balance**: Imbalance between work and personal life can contribute to burnout. This section evaluates the integration of professional and personal aspects of life.






## This Repo

This repository contains the necessary files to generate and use the Burnout Recovery Index assessment tool. It includes a CSV file with all the questions, a Python script to generate the HTML widget, and the resulting HTML file that can be used to administer the assessment.

Here's a breakdown of the repository contents:

| File Name | Description |
|-----------|-------------|
| README.md | This file, containing information about the project and repo |
| LICENSE | The license file for this project |
| questions.csv | CSV file containing all 240 questions for the assessment |
| generate_widget.py | Python script to generate the HTML widget from the CSV file |
| widget.html | The generated HTML file containing the interactive assessment tool |

To use this repo:

1. Clone the repository
2. Ensure you have Python installed
3. Run `generate_widget.py` to create or update the `widget.html` file
4. Open `widget.html` in a web browser to use the Burnout Recovery Index assessment tool





## Interpretation

The Burnout Recovery Index is calculated based on responses to 240 questions across 12 categories. Each category contains 20 questions: 10 positively framed (Set A) and 10 negatively framed (Set B).

### Scoring

1. Each question is scored on a 5-point Likert scale (1-5).
2. For Set A questions, the score is used as-is (1-5).
3. For Set B questions, the score is reversed (5-1).
4. Each category score is normalized to a 0-100 scale:
   - Minimum possible raw score: 20 (20 questions * 1 point)
   - Maximum possible raw score: 100 (20 questions * 5 points)
   - Normalized score = (Raw score - 20) / (100 - 20) * 100

### Results

The assessment provides:
1. Individual scores for each of the 12 categories (0-100)
2. An aggregate score (0-100), calculated as the average of all category scores

Claude offered the following interpretation scales (NOT VERIFIED!)

1. **Full Recovery/Optimal Well-being: 90-100:** This range would represent someone who is thriving in almost all areas of life.
2. **Minimal to No Burnout: 80-89:** Individuals in this range are generally doing well, with only minor areas for improvement.
3. **Mild Burnout: 70-79:** This is where you currently fall. There's room for improvement, but you're managing well overall.
4. **Moderate Burnout: 55-69:** Significant impacts on well-being and functioning, but not severe.
5. **Severe Burnout: 40-54:** Major impairments across multiple life domains.
6. **Critical Burnout: 25-39:** Extremely compromised functioning, urgent intervention needed.
7. **Full Burnout / Crisis: Below 25:** This would represent a state of complete exhaustion and dysfunction across all areas.

Note: this scale is likely wayyyyy off. It's entirely possible or likely that a score below 50 constitutes "full burnout" 


### Interpretation

- Higher scores indicate better recovery or less burnout in that area.
- Lower scores suggest more significant burnout symptoms or challenges in that category.
- The aggregate score provides an overall picture of burnout level or recovery progress.

### Tracking Progress

This assessment is designed to be taken periodically (e.g., monthly or quarterly) to track changes over time. By monitoring category and aggregate scores, individuals can:

1. Identify areas of improvement or decline
2. Recognize patterns in their burnout symptoms or recovery
3. Focus on specific categories that consistently score low
4. Celebrate progress in categories that show improvement

### Limitations

While this index provides objective measures, it is not a diagnostic tool. Individuals with persistent low scores or concerns about their mental health should consult with a healthcare professional.

As more data is gathered, future versions of this interpretation guide will include general guidelines about which aggregate scores typically represent different levels of burnout.
