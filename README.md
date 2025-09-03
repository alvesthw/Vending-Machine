# 🥤 Vending Machine — Projeto de Linguagens Formais

## 👨‍🎓 Alunos
- Matheus Alves Bueno Machado  
- Felipe Biava Favarin

## 📦 Clonando o Repositório e Configurando o Ambiente

```bash
# 📦 Clonar o repositório
git clone https://github.com/alvesthw/Vending-Machine.git
cd "Vending Machine"

# ⚙️ Criar o ambiente virtual
python -m venv .venv

# Ativar o ambiente virtual

# No Windows (PowerShell)
.\.venv\Scripts\activate

# No Windows (CMD)
.venv\Scripts\activate.bat

# No Linux/macOS
source .venv/bin/activate

# Desativar o ambiente virtual
deactivate

# 📚 Instalar dependências
pip install -r requirements.txt

# 🌿 Criar uma nova branch
git checkout -b <nome-da-branch>

# Fazer commit e enviar para o GitHub
git add .
git commit -m "Mensagem do commit"
git push -u origin <nome-da-branch>

# Atualizar sua branch com a main
git checkout main
git pull origin main
git checkout <nome-da-branch>

# (Opcional) Rebase da main
git rebase main

# ▶️ Executar o projeto com Python
python main.py

# 🛠️ Gerar executável com PyInstaller
pyinstaller --onefile --windowed main.py
```

# 🧾 Usando o Executável (.exe)
Diretamente: exe/VendingMachine.exe

Via arquivo .zip: Baixe e descompacte release/VendingMachine.zip Execute VendingMachine.exe dentro da pasta descompactada

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