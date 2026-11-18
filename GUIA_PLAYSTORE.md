# 🚀 Guia de Lançamento na Google Play Store: DroneHub Brasil

Este documento orienta o processo de homologação, publicação e monetização do **DroneHub Brasil** na **Google Play Store**.

---

## 1. Requisitos Obrigatórios do Google Play Console

1. **Conta de Desenvolvedor Google Play:**
   - Acesse: [play.google.com/console/signup](https://play.google.com/console/signup)
   - Taxa única de inscrição: **US$ 25,00** (cobrado no cartão de crédito internacional).
   - Documento com foto (RG/CNH) para verificação de identidade.

2. **Regra dos 20 Testadores (Contas Pessoais novas):**
   - O Google exige que novas contas de desenvolvedor pessoa física submetam o app para um teste fechado com **pelo menos 20 pessoas por 14 dias consecutivos** antes de liberar a publicação na loja aberta.
   - *Estratégia:* Você usará exatamente a fase de **teste em APK / teste fechado** com os primeiros 20 pilotos de drone cadastrados para cumprir esse requisito com facilidade!

---

## 2. Materiais Gráficos Necessários

Para preencher a ficha da Play Store, você precisará dos seguintes arquivos visuais:

| Item | Dimensões | Formato | O que mostrar |
| :--- | :--- | :--- | :--- |
| **Ícone do App** | 512 x 512 px | PNG 32-bit (sem transparência) | Logo do DroneHub com o drone e mapa do Brasil |
| **Gráfico de Recursos (Banner)** | 1024 x 500 px | JPG ou PNG | Banner chamativo: *"Encontre Pilotos de Drone em Todo o Brasil"* |
| **Capturas de Tela (Smartphones)** | Mínimo 4 telas (1080 x 2400 px) | JPG ou PNG | Tela de Busca por Região, Perfil do Piloto, Cadastro e Mural de Demandas |
| **Política de Privacidade** | Link URL | Página Web | Texto explicando o uso de dados (nome, WhatsApp, localização para busca de serviços) |

---

## 3. Modelo de Negócio & Monetização (Como Ganhar Dinheiro com o App)

Como intermediador da rede de pilotos no Brasil, você pode faturar através de 4 modelos testados:

1. **Plano Piloto Destaque (Assinatura Mensal - ex: R$ 49/mês):**
   - O piloto assinante aparece no topo das buscas da sua cidade e estado com um selo dourado *"Piloto Pro / Verificado"*.
2. **Taxa de Intermediação de Demandas (Escrow - 10% a 15%):**
   - Para grandes serviços corporativos (mapeamento de fazendas, inspeções prediais de R$ 5.000+), o cliente paga através do app e o dinheiro só é liberado ao piloto após a aprovação das fotos/ortomosaico.
3. **Crédito de Desbloqueio de Vagas (Modelo GetNinjas):**
   - Contratantes publicam vagas de graça. Os primeiros 3 pilotos que quiserem atender compram "moedas/créditos" (ex: R$ 15 por vaga) para liberar o WhatsApp do contratante.
4. **Venda de Seguros RETA e Homologação:**
   - Parcerias com corretoras de seguro aeronáutico e despachantes ANAC/DECEA direto dentro do app.

---

## 4. Checklist Técnico para Aprovação no Google Play

- [ ] Target SDK atualizado para o Android mais recente (Android 14+ / API level 34).
- [ ] Arquivo gerado em formato **.AAB (Android App Bundle)** assinado com Keystore segura.
- [ ] Formulário de Conteúdo do App preenchido (Classificação Livre / 10+).
- [ ] Declaração de Permissões: Localização aproximada (para filtrar pilotos por estado/cidade).
- [ ] Link de exclusão de conta fácil para usuários (exigência recente da Play Store).
