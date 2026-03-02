# 🤖 Automação de Newsletter Corporativa: IA & Retalho

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Power Automate](https://img.shields.io/badge/Power_Automate-0066FF?style=for-the-badge&logo=powerautomate&logoColor=white)
![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)
![Integração de Sistemas](https://img.shields.io/badge/Integração_de_APIs-Backend-success?style=for-the-badge)

Sistema de automação backend para curadoria e distribuição multicanal de newsletters corporativas sobre Inteligência Artificial, Microsoft Copilot e Tecnologia no Retalho/Moda.

---

## 📋 Visão Geral

Este projeto automatiza o processo completo de curadoria de notícias e distribuição multicanal, contornando restrições de segurança empresariais através de uma arquitetura baseada em webhooks. O sistema realiza extração inteligente de conteúdo e distribui simultaneamente através de:

- **E-mail corporativo** (via Microsoft Power Automate)
- **Mural de avisos no Discord** (via Webhook Embeds)

## 🎯 Contexto e Desafio

Em ambientes corporativos modernos, o envio automatizado de e-mails enfrenta barreiras significativas:

- **MFA/2FA obrigatório** impossibilita autenticação via script tradicional
- **Desativação de SMTP básico** por políticas de segurança de TI
- **Restrições de Active Directory** limitam permissões de automação

### Solução Implementada

Arquitetura híbrida que substitui o envio direto por SMTP através de uma pipeline de microsserviços e APIs:
```
Google News RSS → Script Python → Webhooks (JSON) → (Power Automate / Discord) → Equipa
```

**Vantagens da abordagem:**
- ✅ Conformidade total com políticas de segurança corporativa
- ✅ Distribuição multicanal sem código duplicado
- ✅ Sistema de feature flags para controlo granular de canais
- ✅ Manutenibilidade através de arquitetura modular

---

## 🏗️ Arquitetura e Componentes

### 1. Extração de Dados (`services/rss_service.py`)
- Consumo da API RSS do Google News via `feedparser`
- Filtragem inteligente por palavras-chave estratégicas
- Parsing e normalização de conteúdo estruturado

### 2. Integração Multicanal (`services/`)

**E-mail Corporativo (`email_service.py`):**
- Cliente HTTP (`requests`) envia payload JSON para API privada no Power Automate
- Power Automate utiliza credenciais Microsoft 365 homologadas para disparo seguro
- Template HTML responsivo e profissional

**Discord (`discord_service.py`):**
- Geração dinâmica de **Embeds** (cards interativos)
- Envio via Webhook diretamente para canal da equipa
- Formatação visual otimizada para leitura rápida

### 3. Orquestração e Feature Flags (`main.py`)
- Sistema de chaves de ativação (`True`/`False`) para controlo de canais
- Configuração centralizada sem necessidade de alterar lógica de negócio
- Execução seletiva de serviços baseada em flags

---

## 🛠️ Stack Tecnológica

| Categoria | Tecnologia |
|-----------|-----------|
| **Linguagem** | Python 3.8+ |
| **HTTP Client** | `requests` |
| **RSS Parser** | `feedparser` |
| **Orquestração** | Microsoft Power Automate |
| **Notificações** | Discord Webhooks (Embeds) |
| **Agendamento** | Windows Task Scheduler |

---

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- Acesso ao Microsoft Power Automate
- Servidor Discord com permissões de Webhook
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

### 4. Configurar Variáveis de Ambiente e Webhooks

Abra o arquivo `config/settings.py` e configure as URLs dos webhooks:

#### Power Automate (E-mail Corporativo)

1. Aceda ao [Power Automate](https://make.powerautomate.com)
2. Crie um fluxo com o gatilho **"Quando uma solicitação HTTP é recebida"**
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

4. Adicione a ação **"Enviar um e-mail (V2)"** do Outlook e mapeie as variáveis
5. Copie a **URL HTTP POST** gerada e cole em `URL_POWER_AUTOMATE`

#### Discord (Mural de Avisos)

1. No servidor Discord, aceda a **Configurações do Canal**
2. Navegue até **Integrações → Webhooks**
3. Crie um novo webhook e copie a URL
4. Cole a URL em `DISCORD_WEBHOOK_URL`

### 5. Executar o Script
```bash
python main.py
```

---

## 📁 Estrutura do Projeto
```
automacao-newsletter-ia/
├── config/
│   └── settings.py          # Variáveis globais e URLs de webhooks
├── services/
│   ├── email_service.py     # Integração com Power Automate
│   ├── discord_service.py   # Integração com Discord (Embeds)
│   └── rss_service.py       # Extração de dados (Google News RSS)
├── templates/
│   └── newsletter.py        # Template HTML responsivo do e-mail
├── main.py                  # Orquestrador central e feature flags
├── requirements.txt         # Dependências do projeto
├── agendador.bat           # Script batch para Task Scheduler
└── README.md               # Documentação
```

---

## 🎛️ Configuração Avançada: Painel de Controlo

O arquivo `main.py` possui um sistema de **Feature Flags** que permite ativar ou desativar canais de distribuição sem modificar a lógica de negócio:
```python
# 🎛️ PAINEL DE CONTROLO (FEATURE FLAGS)
ENVIAR_EMAIL = True      # Ativa/desativa envio via Outlook corporativo
ENVIAR_DISCORD = True    # Ativa/desativa envio para servidor Discord
```

### Cenários de Uso

| Cenário | `ENVIAR_EMAIL` | `ENVIAR_DISCORD` | Descrição |
|---------|----------------|------------------|-----------|
| Produção completa | `True` | `True` | Ambos os canais ativos |
| Apenas e-mail | `True` | `False` | Newsletter corporativa tradicional |
| Apenas Discord | `False` | `True` | Comunicação informal da equipa |
| Modo teste | `False` | `False` | Execução sem envio real |

### Agendamento Automático (Windows)

Para execução periódica automática:

1. Abra o **Agendador de Tarefas** do Windows
2. Crie uma nova tarefa básica
3. Configure o gatilho (exemplo: diariamente às 8h00)
4. Defina a ação para executar o arquivo `agendador.bat`
5. Salve e teste a tarefa

---

## 🔧 Personalização de Conteúdo

### Palavras-chave de Curadoria

Edite o arquivo `services/rss_service.py` para personalizar os tópicos de interesse:
```python
PALAVRAS_CHAVE = [
    "Microsoft Copilot",
    "IA no retalho",
    "tecnologia moda",
    "inteligência artificial varejo",
    # Adicione suas palavras-chave personalizadas
]
```

### Template de E-mail

O template HTML em `templates/newsletter.py` pode ser personalizado com:
- Logotipo corporativo
- Cores da marca
- Rodapé institucional
- Links de redes sociais

### Embeds do Discord

Configure a aparência dos cards em `services/discord_service.py`:
- Cor do embed (hexadecimal)
- Campos personalizados
- Thumbnail ou imagem de destaque
- Footer com informações adicionais

---

## 🔒 Segurança

- ✅ **Autenticação OAuth 2.0** via Power Automate
- ✅ **Zero credenciais em código** - sem senhas hardcoded
- ✅ **Comunicação HTTPS** end-to-end via requisições POST
- ✅ **Conformidade corporativa** com políticas de TI
- ✅ **Webhooks privados** com URLs não-expostas em repositório público

**Recomendação:** Utilize variáveis de ambiente ou arquivos `.env` (não versionados) para armazenar URLs de webhooks em produção.

---

## 🐛 Troubleshooting

| Problema | Causa Provável | Solução |
|----------|----------------|---------|
| Erro 401/403 no webhook | URL inválida ou expirada | Regenere o webhook e atualize `settings.py` |
| Nenhuma notícia retornada | Palavras-chave muito específicas | Amplie os termos de busca no RSS |
| E-mail não enviado | Power Automate desligado | Verifique se o fluxo está ativo |
| Discord sem mensagens | Permissões insuficientes | Verifique permissões do webhook no canal |
| Erro de importação | Dependências não instaladas | Execute `pip install -r requirements.txt` |

---

## 📈 Melhorias Futuras

- [ ] Integração com Slack via webhook
- [ ] Dashboard web para monitoramento de envios
- [ ] Análise de sentimento das notícias com NLP
- [ ] Armazenamento histórico em banco de dados
- [ ] API REST para consulta de newsletters anteriores
- [ ] Suporte a múltiplos idiomas
- [ ] Relatórios de engajamento (cliques, aberturas)

---

## 📝 Licença

Este projeto foi desenvolvido para uso interno corporativo. Todos os direitos reservados.

---

## 👨‍💻 Autor

**Kauã Hiro**  
Desenvolvimento de Sistemas, Integração de APIs & Implementação de IA

🔗 [LinkedIn](https://www.linkedin.com/in/kaua-mizumoto/)  
🏢 Desenvolvido no contexto de inovação interna corporativa (Guess Brasil)

---

**Nota:** Este projeto demonstra uma abordagem pragmática para superar restrições de infraestrutura corporativa mantendo conformidade com políticas de segurança, através de arquitetura modular e feature flags para controlo granular de funcionalidades.