Aqui está o README refatorado com melhorias na estrutura, clareza e profissionalismo:
markdown# 🤖 Automação de Newsletter Corporativa: IA & Retalho

Sistema de automação backend para curadoria e distribuição de newsletters corporativas sobre Inteligência Artificial, Microsoft Copilot e Tecnologia no Retalho/Moda.

## 📋 Visão Geral

Este projeto automatiza o processo de curadoria de notícias e criação de newsletters corporativas, contornando restrições de segurança empresariais através de uma arquitetura baseada em webhooks e integração com Microsoft Power Automate.

## 🎯 Contexto e Desafio

Em ambientes corporativos modernos, o envio automatizado de e-mails enfrenta barreiras significativas:

- **MFA/2FA obrigatório** impossibilita autenticação via script
- **Desativação de SMTP básico** por políticas de TI
- **Restrições de Active Directory** limitam permissões de automação

### Solução Implementada

Arquitetura híbrida que substitui o envio direto por SMTP por uma pipeline de microsserviços:
```
Google News RSS → Script Python → Webhook (JSON) → Power Automate → Outlook Corporativo
```

## 🏗️ Arquitetura

### Componentes Principais

1. **Extração de Dados**
   - Consumo da API RSS do Google News via `feedparser`
   - Filtragem por palavras-chave estratégicas
   - Parsing e normalização de conteúdo

2. **Processamento e Template**
   - Formatação de dados em HTML estruturado
   - Injeção dinâmica de conteúdo em template pré-definido

3. **Integração via Webhook**
   - Cliente HTTP (`requests`) envia payload JSON
   - API privada no Power Automate recebe requisição

4. **Disparo Seguro**
   - Power Automate utiliza credenciais Microsoft 365 autenticadas
   - Envio através de canais corporativos homologados

## 🛠️ Stack Tecnológica

| Categoria | Tecnologia |
|-----------|-----------|
| **Linguagem** | Python 3.x |
| **HTTP Client** | `requests` |
| **RSS Parser** | `feedparser` |
| **URL Handling** | `urllib.parse` |
| **Orquestração** | Microsoft Power Automate |
| **E-mail** | Microsoft 365 Outlook |
| **Agendamento** | Windows Task Scheduler |

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- Acesso ao Microsoft Power Automate
- Conta corporativa Microsoft 365

### 1. Clonar o Repositório
```bash
git clone https://github.com/kaua-hiro/automacao-newsletter-ia.git
cd automacao-newsletter-ia
```

### 2. Configurar Ambiente Virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar Webhook do Power Automate

1. Aceda ao [Power Automate](https://make.powerautomate.com)
2. Crie um novo fluxo com o gatilho **"Quando uma solicitação HTTP é recebida"**
3. Configure o esquema JSON:
```json
{
    "type": "object",
    "properties": {
        "destinatario": { "type": "string" },
        "assunto": { "type": "string" },
        "corpo_html": { "type": "string" }
    }
}
```

4. Adicione a ação **"Enviar um e-mail (V2)"** do Outlook
5. Mapeie as variáveis dinâmicas aos campos do e-mail
6. Copie a **URL HTTP POST** gerada
7. Cole a URL na variável `URL_POWER_AUTOMATE` em `curadoria_newsletter.py`

### 5. Executar o Script
```bash
python curadoria_newsletter.py
```

## 📁 Estrutura do Projeto
```
automacao-newsletter-ia/
├── curadoria_newsletter.py    # Script principal
├── requirements.txt            # Dependências Python
├── template_newsletter.html    # Template HTML da newsletter
├── agendador.bat              # Script batch para Task Scheduler
└── README.md                  # Documentação
```

## 🔧 Configuração Avançada

### Agendamento Automático (Windows)

1. Abra o **Agendador de Tarefas**
2. Crie uma nova tarefa básica
3. Configure o gatilho (diário, semanal, etc.)
4. Defina a ação para executar `agendador.bat`

### Personalização de Palavras-chave

Edite a lista de palavras-chave no ficheiro `curadoria_newsletter.py`:
```python
PALAVRAS_CHAVE = [
    "Microsoft Copilot",
    "IA no retalho",
    "tecnologia moda",
    # Adicione suas palavras-chave
]
```

## 🔒 Segurança

- ✅ Autenticação via OAuth 2.0 (Power Automate)
- ✅ Sem armazenamento de credenciais em código
- ✅ Comunicação HTTPS end-to-end
- ✅ Conformidade com políticas corporativas de TI

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| Erro de conexão ao webhook | Verifique a URL do Power Automate |
| Falha na instalação de dependências | Execute `pip install --upgrade pip` |
| RSS não retorna resultados | Verifique conectividade com Google News |

## 📝 Licença

Este projeto foi desenvolvido para uso interno corporativo. Todos os direitos reservados.

## 👨‍💻 Autor

**Kauã Hiro**  
Desenvolvimento de Sistemas & Implementação de IA

🔗 [LinkedIn](https://www.linkedin.com/in/kaua-mizumoto/)  
🏢 Desenvolvido no contexto de inovação interna corporativa

---

**Nota:** Este projeto demonstra uma abordagem pragmática para superar restrições de infraestrutura c
