const uploadArea = document.getElementById('uploadArea');
const fileInput = document.getElementById('fileInput');
const textInput = document.getElementById('textInput');
const processBtn = document.getElementById('processBtn');
const newAnalysisBtn = document.getElementById('newAnalysisBtn');

const results = document.getElementById('results');
const loading = document.getElementById('loading');
const error = document.getElementById('error');

const fileName = document.getElementById('fileName');
const categoryName = document.getElementById('categoryName');
const responseText = document.getElementById('responseText');

uploadArea.addEventListener('click', () => fileInput.click());

uploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    uploadArea.classList.add('dragover');
});

uploadArea.addEventListener('dragleave', () => {
    uploadArea.classList.remove('dragover');
});

uploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    uploadArea.classList.remove('dragover');

    const files = e.dataTransfer.files;
    if (files.length > 0) {
        setFile(files[0]);
    }
});

fileInput.addEventListener('change', (e) => {
    if (e.target.files.length > 0) {
        setFile(e.target.files[0]);
    }
});

function setFile(file) {
    const allowedTypes = ['text/plain', 'application/pdf'];

    if (!allowedTypes.includes(file.type)) {
        showError('Selecione um arquivo .txt ou .pdf válido');
        return;
    }

    fileName.textContent = `📄 Arquivo selecionado: ${file.name}`;
    fileName.classList.add('show');
    error.classList.remove('show');
}

processBtn.addEventListener('click', analyzeDocument);

async function analyzeDocument() {
    const text = textInput.value.trim();
    const file = fileInput.files[0];

    if (!text && !file) {
        showError('Por favor, selecione um arquivo ou digite um texto para análise');
        return;
    }

    error.classList.remove('show');
    results.classList.remove('show');
    loading.classList.add('show');

    const formData = new FormData();

    if (text) formData.append('text', text);
    if (file) formData.append('file', file);

    try {
        const response = await fetch('/api/v1/classificar', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            const err = await response.text();
            throw new Error(err);
        }

        const data = await response.json();

        categoryName.textContent = data.categoria;
        responseText.textContent = data.resposta_sugerida;

        loading.classList.remove('show');
        results.classList.add('show');
        results.scrollIntoView({ behavior: 'smooth' });

    } catch (err) {
        console.error(err);
        loading.classList.remove('show');
        showError('Erro ao processar o documento. Tente novamente.');
    }
}

newAnalysisBtn.addEventListener('click', () => {
    textInput.value = '';
    fileInput.value = '';
    fileName.textContent = '';
    fileName.classList.remove('show');
    results.classList.remove('show');
    loading.classList.remove('show');
    error.classList.remove('show');

    uploadArea.scrollIntoView({ behavior: 'smooth' });
});

function showError(message) {
    error.textContent = message;
    error.classList.add('show');
}
