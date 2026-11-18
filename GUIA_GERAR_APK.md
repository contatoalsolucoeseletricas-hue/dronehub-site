# 📱 Guia Prático: Como Gerar o APK do DroneHub Brasil

Este guia explica como transformar o **DroneHub Brasil** em um arquivo instalável **.APK** para testar no seu celular Android e nos celulares dos primeiros pilotos e clientes.

---

## ⚡ Método 1: Teste Instantâneo no Celular (Sem precisar de APK)

Antes mesmo de compilar o APK, você pode testar o app **exatamente como ele roda no celular**:

1. Dê dois cliques no arquivo `iniciar_app.bat` na pasta `C:\DRONE`.
2. Pegue seu celular Android conectado no **mesmo Wi-Fi** do computador.
3. Abra o Google Chrome no celular e digite:
   ```text
   http://192.168.1.3:8080/marketplace_app.html
   ```
4. **Dica de Ouro:** No Chrome do celular, toque nos 3 pontinhos (canto superior direito) e selecione:
   **"Adicionar à tela inicial"** ou **"Instalar aplicativo"**.
   *O app ganha ícone na sua tela inicial e roda em tela cheia, exatamente como um app nativo baixado da Play Store!*

---

## 🛠️ Método 2: Gerar o APK Nativo com Capacitor (Mais Rápido & Direto)

O **Capacitor** (da equipe do Ionic) é a ferramenta oficial mais recomendada para transformar projetos web em aplicativos nativos Android com APK real.

### Pré-requisitos no Computador:
- [Android Studio](https://developer.android.com/studio) instalado (com Android SDK).

### Passo a Passo no Terminal (PowerShell em `C:\DRONE`):

1. **Inicializar o projeto Node.js:**
   ```powershell
   cd C:\DRONE
   npm init -y
   ```

2. **Instalar o Capacitor:**
   ```powershell
   npm install @capacitor/core @capacitor/cli @capacitor/android
   ```

3. **Inicializar o Capacitor:**
   ```powershell
   npx cap init "DroneHub Brasil" "com.dronehub.brasil" --web-dir "."
   ```

4. **Adicionar a plataforma Android:**
   ```powershell
   npx cap add android
   ```

5. **Copiar os arquivos e abrir no Android Studio:**
   ```powershell
   npx cap sync
   npx cap open android
   ```

6. **Gerar o arquivo .APK:**
   - No Android Studio, vá no menu superior: **Build > Build Bundle(s) / APK(s) > Build APK(s)**.
   - Aguarde 1 a 2 minutos.
   - O Android Studio mostrará uma notificação: *APK(s) generated successfully*.
   - Clique em **locate**: o arquivo `app-debug.apk` estará pronto!
   - Envie esse arquivo `.apk` pelo WhatsApp ou Telegram e instale diretamente no celular.

---

## ☁️ Método 3: Gerar APK na Nuvem com Expo / React Native (Sem instalar Android Studio)

Se você preferir a arquitetura completa em **React Native**, você pode usar o **EAS Build** para compilar o APK direto nos servidores da nuvem do Expo:

1. **Instalar a CLI do EAS:**
   ```powershell
   npm install -g eas-cli
   ```

2. **Criar conta gratuita:**
   Acesse [expo.dev](https://expo.dev) e crie uma conta.

3. **Configurar para gerar APK de teste:**
   No arquivo `eas.json`:
   ```json
   {
     "build": {
       "preview": {
         "android": {
           "buildType": "apk"
         }
       }
     }
   }
   ```

4. **Executar a compilação:**
   ```powershell
   eas build -p android --profile preview
   ```
   *O Expo compilará o APK na nuvem e te dará um link com QR Code para baixar o arquivo `.apk` direto no celular.*

---

## 🌐 Método 4: PWABuilder da Microsoft (100% Automático)

Se você hospedar o `marketplace_app.html` em qualquer servidor gratuito (como Vercel, Netlify ou GitHub Pages):
1. Acesse: [https://www.pwabuilder.com](https://www.pwabuilder.com)
2. Cole a URL do seu site.
3. Clique em **"Package for Stores"** > **Android**.
4. Ele gera automaticamente o projeto Android e o arquivo APK / AAB pronto para testes e para a Google Play Store!
