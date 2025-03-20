# Calculadora Django

## 📌 Descrição
Este projeto é uma **calculadora web** desenvolvida com Django, focada na realização de operações matemáticas básicas com uma interface simples e eficiente.

## 🚀 Tecnologias Utilizadas
- **Python 3**
- **Django**
- **HTML, CSS e JavaScript** 
- **SQLite/PostgreSQL** 

## ⚙️ Funcionalidades
- Operações matemáticas básicas: **soma, subtração, multiplicação e divisão**.
- Interface web simples e responsiva.
- Histórico de cálculos armazenado no banco de dados (se implementado).
- Validação de entradas para evitar erros de cálculo.

## 📂 Estrutura do Projeto
```
calculadora/
│── calculos/        # Aplicação principal
│── templates/       # Arquivos HTML
│── static/          # CSS, JS e imagens
│── db.sqlite3       # Banco de dados SQLite (padrão)
│── manage.py        # Comando para administrar o Django
│── requirements.txt # Dependências do projeto
```

## 🚀 Como Executar o Projeto
### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/rayssarrsilva/calculadora.git
cd calculadora
```

### 2️⃣ Criar e Ativar Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar Migrações e Iniciar o Servidor
```bash
python manage.py migrate
python manage.py runserver
```

Acesse **http://127.0.0.1:8000/** no navegador para utilizar a calculadora localmente com o "py manage.py runserver".

## 🛠️ Melhorias Futuras
- Implementação de cálculos científicos avançados.
- Armazenamento do histórico de cálculos no banco de dados.
- Interface aprimorada com Bootstrap ou TailwindCSS.

## 📄 Licença
Este projeto está sob a licença **MIT**. Sinta-se à vontade para contribuir e aprimorar.

---
🔹 **Desenvolvido por Rayssa Roberta** | [GitHub](https://github.com/rayssarrsilva)
