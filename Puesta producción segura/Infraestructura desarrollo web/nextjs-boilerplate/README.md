# Despliegue de una Aplicación Web con Node.js, Next.js y Vercel

Este documento recoge el proceso para desplegar una aplicación web desarrollada en **Node.js**, **Next.js** en **Vercel**.

- **Enlace del despliegue:** https://nextjs-grupo-3.vercel.app/

## Prerrequisitos

1. **Cuenta en Vercel**: Crea una cuenta en [vercel.com](https://vercel.com/).
2. **Node.js y NPM**: Instala Node.js en tu sistema, ya que Next.js y sus dependencias se gestionan con npm o yarn.
3. **Repositorio en GitHub**: Vercel permite el despliegue directamente desde un repositorio GitHub.

## 1. Configura el Proyecto en Local

1. **Crea un proyecto de Next.js**:

   ```bash
   npx create-next-app@latest nombre-de-tu-proyecto
   cd nombre-de-tu-proyecto
   ```

2. **Configura las dependencias**: Asegúrate de que todas las dependencias necesarias están en el archivo `package.json`. Usa el siguiente comando para instalar cualquier dependencia adicional:

   ```bash
   npm install
   ```

3. **Verifica el entorno de desarrollo**: Inicia el servidor de desarrollo para asegurarte de que la aplicación funciona correctamente.

   ```bash
   npm run dev
   ```

## 2. Configura el Proyecto en Git

1. **Inicializa un repositorio Git**:

   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Sube el proyecto a GitHub**:

   ```bash
   git remote add origin <URL_DE_TU_REPOSITORIO>
   git push -u origin main
   ```

## 3. Despliega la Aplicación en Vercel

### Paso 1: Importa el Proyecto a Vercel

1. Ve a [vercel.com](https://vercel.com) y haz clic en **"New Project"**.
2. Conecta tu cuenta de GitHub a Vercel.
3. Selecciona el repositorio que contiene tu proyecto Next.js.

### Paso 2: Configuración Inicial en Vercel

1. **Configuración del Proyecto**:

   - Elige un nombre para tu proyecto o usa el nombre por defecto del repositorio.
   - Confirma que el **Framework Preset** es `Next.js`.
   - Selecciona la rama para el despliegue.

2. Haz clic en **Deploy** para iniciar el primer despliegue de la aplicación.

### Paso 3: Espera el Despliegue

Vercel comenzará a construir y desplegar el proyecto automáticamente. Este proceso puede tardar unos minutos.

1. **Verifica el estado**: Podrás ver el estado del despliegue en tiempo real.
2. Una vez completado el despliegue, obtendrás un enlace (como `https://tu-proyecto.vercel.app`) donde tu aplicación estará disponible. En enlace puede personalizarse una vez desplegado el proyecto.

---

Estos son los pasos que deben seguirse para desplegar una aplicación web usando Node.js y Next.js, y que sea accesible mediante Vercel.
