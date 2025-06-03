from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import easyocr
import google.generativeai as genai
from dotenv import load_dotenv

# Carregar variável de ambiente do arquivo .env
load_dotenv()

# Configurar chave da API Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Inicializar o app Flask
app = Flask(__name__)

# Configurações para upload de arquivos
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'tiff', 'bmp'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Função para verificar extensões permitidas
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Rota principal para upload e regras de negócio
@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        # Verifica se as imagens foram enviadas
        if 'files[]' not in request.files:
            return render_template('index.html', error="Nenhuma imagem foi enviada.")
        
        files = request.files.getlist('files[]')
        texts = []

        # Inicializar OCR
        reader = easyocr.Reader(['en', 'pt'])

        # Processar cada arquivo enviado
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                # Realizar OCR na imagem
                results = reader.readtext(filepath, detail=0, paragraph=True)
                texts.append(" ".join(results))
            else:
                return render_template('index.html', error="Formato de arquivo não suportado.")
        
        # Combinar textos extraídos
        combined_text = "\n".join(texts)
        
        # Capturar regras de negócio fornecidas no formulário
        business_rules = request.form.get('business_rules', '').strip()
        
        # Adicionar regras de negócio ao texto extraído (se existirem)
        if business_rules:
            combined_text += f"\n\nRegras de Negócio:\n{business_rules}"

        # Gerar cenários de teste com a IA Gemini
        scenarios = generate_test_scenarios(combined_text)

        return render_template('index.html', scenarios=scenarios)

    return render_template('index.html')

# Função para chamar a IA Gemini e gerar cenários de teste
def generate_test_scenarios(combined_text):
    prompt = f"""
    A partir do texto abaixo extraído da interface de um sistema, e das regras de negócio fornecidas (se houverem),
    gere todos os cenários possíveis de teste no formato Gherkin. Certifique-se de detalhar fluxos positivos, 
    negativos e validações necessárias.

    Texto extraído e regras de negócio:
    {combined_text}

    Resultado esperado (formato Gherkin):
    """

    try:
        # Configurar e enviar a solicitação para Gemini
        model = genai.GenerativeModel(model_name="gemini-2.0-flash-001")  # Pode ser alterado conforme necessário
        response = model.generate_content(prompt).text.strip()
        return response
    except Exception as e:
        return f"Erro na geração de cenários: {str(e)}"

# Iniciar o servidor Flask
if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
