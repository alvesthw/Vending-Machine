# 🥤 Vending Machine — Projeto de Linguagens Formais

## 👨‍🎓 Alunos
- Matheus Alves Bueno Machado  
- Felipe Biava Favarin

## Como executar o projeto

1. Clone o repositório com:
```bash
git clone https://github.com/alvesthw/Vending-Machine.git
cd "Vending Machine"
```

2. Crie o ambiente virtual com:
```bash
python -m venv venv
```

3. E Ative o ambiente virtual com:
```bash
source venv/bin/activate
```

4. Para instalar os requisitos do código:
```bash
pip install -r requirements.txt
```

5. Rodar o projeto
```bash
python main.py
```

6. Gerar o executavel
```bash
pyinstaller --onefile --windowed main.py --add-data "images;images"
```

# 🧾 Usando o Executável (.exe)
Diretamente Vending-Machine\exe_zip

# 📝 Observações
O arquivo VendingMachine.jff pode ser aberto com o software JFLAP para visualizar o autômato.

A pasta images/ contém os recursos visuais utilizados no projeto.

As pastas .venv/, dist/ e build/ estão listadas no .gitignore e não devem ser enviadas ao GitHub.

Para qualquer alteração no executável, basta gerar um novo .exe com PyInstaller.

# 📁 Estrutura do Projeto
```bash
Vending Machine/
├── .venv/                ← Ambiente virtual
├── images/               ← Imagens do projeto
├── exe/                  ← Executável zipado
├── dist/                 ← Build temporário (PyInstaller)
├── build/                ← Build temporário (PyInstaller)
├── main.py               ← Script principal
├── utils.py              ← Código auxiliar
├── VendingMachine.jff    ← Arquivo JFLAP
├── requirements.txt      ← Dependências
├── README.md             ← Este arquivo
├── *.spec                ← Arquivos PyInstaller (temporários)
```
