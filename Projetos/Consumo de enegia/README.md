# ⚡ Calculadora de Consumo Elétrico

## 📚 Sobre o projeto

Esse projeto foi feito para a atividade de recuperação da Agenda 5 de Desenvolvimento de Sistemas.

A proposta da atividade era criar um programa em Python que conseguisse calcular uma estimativa do consumo de energia elétrica de um aparelho durante um mês.
Eu fiz o programa pensando em deixar o cálculo simples para o usuário. Primeiro, ele informa qual aparelho quer analisar, depois coloca a potência dele em watts (W) e por quantas horas, aproximadamente, o aparelho fica ligado por dia.
Depois dessas informações, o programa faz o cálculo e mostra na tela uma estimativa de quantos kWh o aparelho consome durante um mês.
Também acrescentei uma parte para calcular um possível custo da energia, usando R$ 0,75 por kWh como valor fixo.

## 🎯 Objetivo

O principal objetivo foi criar uma calculadora que ajudasse a entender melhor o consumo dos aparelhos elétricos.
Além de cumprir a proposta da atividade, a ideia é mostrar de uma forma mais fácil como a potência de um aparelho e o tempo que ele fica ligado podem influenciar no consumo de energia.

## 🐍 Linguagem utilizada

- Python
- Visual Studio Code
- GitHub

## 🧮 Como funciona o cálculo?

 cálculo utilizado no programa é:

consumoMensal = (potencia × horasDia × 30) / 1000
A potência é informada em watts (W), o tempo é informado em horas por dia e são considerados 30 dias no mês.
O resultado é dividido por 1000 para transformar Wh em kWh.
Para calcular o custo aproximado, utilizei:
custoMensal = consumoMensal × 0,75
O valor de R$ 0,75 é apenas uma estimativa usada na atividade.

## 💻 Como o programa funciona

Quando o programa começa, ele pede:

1. O nome do aparelho;
2. A potência em watts;
3. A quantidade de horas de uso por dia.

Depois disso, o programa realiza os cálculos e apresenta o consumo mensal e o custo estimado.

## 🖥️ Exemplo

Digite:Geladeira
150
10

O resultado será: 

Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75/mês

## 📁 Organização dos arquivos

projetos/
└── consumo-energia/
    ├── app.py
    └── README.md

O arquivo app.py contém o código da calculadora.
O README.md contém as informações e explicações sobre o projeto.

## ▶️ Como executar

É necessário ter o Python instalado.
Abra a pasta do projeto no Visual Studio Code e abra o terminal.
Depois, execute:
python app.py
Após isso, é só responder às perguntas que aparecerem.

## 🌱 O que foi utilizado no projeto

O Python foi utilizado para criar a lógica da calculadora, receber os dados e realizar os cálculos.
O VS Code foi utilizado para escrever e executar o código.
O Git e o GitHub foram utilizados para organizar e publicar o projeto.

## 🚀 Commit inicial

feat: versão inicial (app.py e README)

## 👩‍💻 Autora

Isabelli MA ALMEIDA
Atividade de Recuperação — Agenda 5  
Desenvolvimento de Sistemas