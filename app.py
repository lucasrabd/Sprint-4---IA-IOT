from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Definição das perguntas e respostas
faq = [
    {"question": "O que é IoT?", "answer": "IoT é a Internet das Coisas, que permite a comunicação entre dispositivos pela internet."},
    {"question": "Como funciona o aprendizado de máquina?", "answer": "Aprendizado de máquina é um método de análise de dados que automatiza a construção de modelos analíticos."},
    {"question": "O que é inteligência artificial?", "answer": "Inteligência artificial é a simulação da inteligência humana por máquinas."},
    {"question": "Quais são os benefícios da IoT?", "answer": "Os benefícios da IoT incluem automação, eficiência, monitoramento em tempo real e a capacidade de coletar e analisar grandes quantidades de dados."},
    {"question": "Quais são as aplicações da inteligência artificial?", "answer": "A inteligência artificial é aplicada em áreas como saúde, finanças, transporte, segurança, entre outras."},
    {"question": "O que é aprendizado supervisionado?", "answer": "Aprendizado supervisionado é uma técnica de machine learning onde o modelo é treinado com dados rotulados."},
    {"question": "Quais são as linguagens de programação mais usadas para IA?", "answer": "As linguagens mais usadas em IA incluem Python, R, Java, e C++."},
    {"question": "O que é um algoritmo?", "answer": "Um algoritmo é uma sequência de instruções bem definidas para resolver um problema ou executar uma tarefa."}
]

@app.route('/')
def home():
    return render_template('index.html', faq=faq)  # Certifique-se de que 'faq' está sendo passado aqui

@app.route('/get_answer/<int:question_id>', methods=['GET'])
def get_answer(question_id):
    if 0 <= question_id < len(faq):
        return jsonify(faq[question_id])
    return jsonify({"error": "Pergunta não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
