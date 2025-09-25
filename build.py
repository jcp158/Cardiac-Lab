from jinja2 import Environment, FileSystemLoader
import os
import shutil

if os.path.exists('dist'):
    shutil.rmtree('dist')
os.makedirs('dist')

# Copy stylesheets
shutil.copytree('static', 'dist/static')  # or whatever your CSS folder is called

# Copy other assets
shutil.copytree('assets', 'dist/assets')

env = Environment(loader=FileSystemLoader('templates'))

questions = [
    {
        'id': 'q1',
        'question': 'Gramma Tala, known for her graceful dancing, has been experiencing chest pain and shortness of breath, especially when performing her traditional dances. The pain is described as a heavy pressure on her chest that radiates to her left arm. After resting, the symptoms subside. What is the most likely diagnosis for Gramma Tala\'s condition?',
        'answers': [
            {'letter': 'A', 'text': 'Angina pectoris', 'explanation': 'Angina pectoris is chest pain or discomfort caused by a temporary decrease in blood flow to the heart muscle. The symptoms described <i>"exertional chest pain that resolves with rest"</i> are classic signs of angina.'},
            {'letter': 'B', 'text': 'Myocardial infarction', 'explanation': 'Myocardial infarction is a heart attack, which involves death of heart muscle due to a prolonged lack of blood flow. The symptoms described are more consistent with a temporary lack of blood flow, which is characteristic of angina.'},
            {'letter': 'C', 'text': 'Coronary artery disease', 'explanation': 'Coronary artery disease is a broad term for conditions that narrow or block the coronary arteries, often due to atherosclerosis. Angina is a symptom of this underlying disease, so while related, it is not the most specific diagnosis for her acute symptoms.'},
            {'letter': 'D', 'text': 'Heart Failure', 'explanation': 'Heart failure is a condition where the heart can\'t pump enough blood to meet the body\'s needs. While it can cause shortness of breath, the primary symptom of exertional chest pain that subsides with rest is more indicative of angina.'},
        ],
        'correct': 'A',
        'hint': 'Consider the difference between a temporary lack of blood flow and a complete blockage or chronic heart weakness.',
        'reward': 'S',
        'image': 'Tala.jpg'
    },
    {
        'id': 'q2',
        'question': 'Chief Tui, who loves to lead the village in various activities, has been feeling extremely fatigued and finds it difficult to walk to the meeting house without feeling breathless. His ankles and feet are swollen. During a physical exam, a physician notes a crackling sound in his lungs. These symptoms suggest that his heart is struggling to pump blood effectively. What is the most likely diagnosis?',
        'answers': [
            {'letter': 'A', 'text': 'Myocardial infarction', 'explanation': 'Myocardial infarction is a sudden event, whereas Chief Tui\'s symptoms, like fatigue and swelling, appear to be a more chronic, progressive condition.'},
            {'letter': 'B', 'text': 'Heart Failure', 'explanation': 'Heart failure is characterized by the heart\'s inability to pump blood efficiently, leading to a backup of fluid in the lungs and other tissues, which explains the ankle swelling and crackles in the lungs.'},
            {'letter': 'C', 'text': 'Hypertension', 'explanation': 'Hypertension, or high blood pressure, is a risk factor for heart disease but is not the end-stage condition described by Chief Tui’s symptoms. His symptoms describe the heart\'s inability to pump properly, which is heart failure.'},
            {'letter': 'D', 'text': 'Coronary artery disease', 'explanation': 'Coronary artery disease is a potential cause of the underlying issue, but the constellation of symptoms: swelling, shortness of breath, and lung sounds, points to a specific consequence of that disease, which is heart failure.'},
        ],
        'correct': 'B',
        'hint': 'Think about the condition that causes fluid to build up in the body and lungs because the heart cannot pump blood effectively.',
        'reward': 'V',
        'image': 'Tui.webp'
    },
    {
        'id': 'q3',
        'question': 'The legendary demigod Maui has been feeling increasingly run down, and during a particularly strenuous attempt to lift a large rock, he experiences a sudden, crushing chest pain that does not go away with rest. He feels dizzy and nauseous, and his skin is clammy. The symptoms are severe and immediate. Which cardiac event is Maui most likely experiencing?',
        'answers': [
            {'letter': 'A', 'text': 'Aortic dissection', 'explanation': 'While an aortic dissection also causes severe chest pain, it is often described as a tearing or ripping pain and is a different medical emergency from a myocardial infarction.'},
            {'letter': 'B', 'text': 'Myocardial infarction', 'explanation': 'The severe, crushing chest pain that does not subside, along with nausea and dizziness, is a classic presentation of a heart attack, which occurs when blood flow to a part of the heart is completely blocked.'},
            {'letter': 'C', 'text': 'Angina pectoris', 'explanation': 'Angina is a temporary condition where symptoms typically resolve with rest, but Maui\'s pain is persistent and severe, which is a key differentiator.'},
            {'letter': 'D', 'text': 'Arrhythmia', 'explanation': 'An arrhythmia is an irregular heartbeat, which may or may not cause chest pain, but the constellation of symptoms including crushing pain and nausea is more specific to a myocardial infarction.'},
        ],
        'correct': 'B',
        'hint': 'Consider the severity and duration of the symptoms; unlike temporary angina, this event involves a complete and persistent blockage.',
        'reward': 'E',
        'image': 'Maui.webp'
    },
    {
        'id': 'q4',
        'question': 'Moana\'s pet pig, Pua, has a genetic predisposition to high cholesterol. Over time, plaque has built up in the arteries supplying his heart, causing them to narrow. This process, which can lead to a heart attack if left untreated, is known as what?',
        'answers': [
            {'letter': 'A', 'text': 'Vasospasm', 'explanation': 'A vasospasm is a sudden constriction of a blood vessel, which is a different cause of reduced blood flow and not the chronic plaque buildup described.'},
            {'letter': 'B', 'text': 'Atherosclerosis', 'explanation': 'Atherosclerosis is the specific disease process in which plaque made of cholesterol and other substances builds up on the inner walls of arteries, causing them to narrow and harden.'},
            {'letter': 'C', 'text': 'Ischemia', 'explanation': 'Ischemia is the term for a temporary lack of blood flow to a tissue, which is a symptom that can result from atherosclerosis, but it is not the name of the underlying disease process itself.'},
            {'letter': 'D', 'text': 'Arteriosclerosis', 'explanation': 'Arteriosclerosis is a general term for the hardening and thickening of artery walls, whereas atherosclerosis specifically refers to the buildup of plaque.'},
        ],
        'correct': 'B',
        'hint': 'This process involves the buildup of a specific substance in the artery walls, which eventually narrows them.',
        'reward': 'A',
        'image': 'Pua.webp'
    },
    {
        'id': 'q5',
        'question': 'Heihei, the rooster, has been diagnosed with heart failure and his medical team is trying to determine the best treatment plan. He has been given a diuretic to help reduce fluid buildup in his body. Which of the following is an additional common treatment strategy for heart failure?',
        'answers': [
            {'letter': 'A', 'text': 'Medications to increase the heart\'s pumping strength', 'explanation': 'Medications that increase contractility, such as positive inotropes, are a key component of heart failure treatment, as they help the weakened heart pump more effectively.'},
            {'letter': 'B', 'text': 'A low-fat diet to reduce cholesterol levels', 'explanation': 'While a low-fat diet is beneficial for heart health in general, it is not a primary treatment for the heart\'s reduced pumping ability in heart failure.'},
            {'letter': 'C', 'text': 'Daily high-intensity cardiovascular exercise', 'explanation': 'Coronary artery disease is a broad term for conditions that narrow or block the coronary arteries, often due to atherosclerosis. Angina is a symptom of this underlying disease, so while related, it is not the most specific diagnosis for her acute symptoms.'},
            {'letter': 'D', 'text': 'Surgical removal of the sinoatrial (SA) node', 'explanation': 'The SA node is the heart\'s natural pacemaker; its removal would not treat heart failure and would instead cause severe bradycardia or even cardiac arrest.'},
        ],
        'correct': 'A',
        'hint': 'Think about what kind of medicine would help a weak heart pump more forcefully.',
        'reward': 'W',
        'image': 'heihei.webp'
    },
]

question_template = env.get_template('question.html')
for q in questions:
    output = question_template.render(question=q)
    with open(f'dist/{q["id"]}.html', 'w') as f:
        f.write(output)

answer_template = env.get_template('result.html')
output = answer_template.render(correctAnswers={q['id']: q['correct'] for q in questions})
with open('dist/result.html', 'w') as f:
    f.write(output)

correct_template = env.get_template('correct.html')
correct_list = []
for q in questions:
    tmp_di = {'id': q['id']}
    tmp_di['reward'] = q['reward']
    tmp_di['image'] = q['image']
    for item in q['answers']:
        if item.get('letter') == q['correct']:
            tmp_di['text'] = item.get('text')
            tmp_di['explanation'] = item.get('explanation')
            correct_list.append(tmp_di)
            break

output = correct_template.render(explanations=correct_list)
with open('dist/correct.html', 'w') as f:
    f.write(output)

incorrect_template = env.get_template('incorrect.html')
incorrect_list = []
for q in questions:
    tmp_di = {'id': q['id'], 'image': q['image']}
    tmp_di['incorrect'] = []
    tmp_di2 = []
    for item in q['answers']:
        if item.get('letter') != q['correct']:
            tmp_di2 = {'letter': item.get('letter')}
            tmp_di2['text'] = item.get('text')
            tmp_di2['explanation'] = item.get('explanation')
            tmp_di['incorrect'].append(tmp_di2)
    incorrect_list.append(tmp_di)

output = incorrect_template.render(explanations=incorrect_list)
with open('dist/incorrect.html', 'w') as f:
    f.write(output)

final_template = env.get_template('final.html')
output = final_template.render()
with open('dist/final.html', 'w') as f:
    f.write(output)
