# Documento comparativo entre herramientas

## Índice

1. [Introducción](#1-introducción)
2. [Herramientas](#2-herramientas)  
   2.1. [Nessus](#21-nessus)  
   2.2. [Openvas](#22-openvas)
3. [Comparación técnica](#3-comparación-técnica)  
   3.1. [Funcionamiento](#31-funcionamiento)  
   3.2. [Detección de vulnerabilidades](#32-detección-de-vulnerabilidades)  
   3.3. [Rendimiento](#33-rendimiento)
4. [Licenciamiento](#4-licenciamiento)
5. [Casos de uso](#5-casos-de-uso)
6. [Conclusión](#6-conclusión)

## 1. Introducción

Este documento va a consistir en  comparar dos herramientas para detección de vulnerabilidades: **Nessus** y **OpenVAS**.

## 2. Herramientas

### 2.1. Nessus

Nessus es un programa de escaneo de vulnerabilidades en diversos sistemas operativos. Consiste en un demonio o diablo, nessusd, que realiza el escaneo en el sistema objetivo, y nessus, el cliente (basado en consola o gráfico) que muestra el avance e informa sobre el estado de los escaneos. Desde consola nessus puede ser programado para hacer escaneos programados con cron. 

### 2.2. OpenVAS

OpenVAS (Open Vulnerability Assessment Scanner, originalmente conocido como GNessUs) es el componente de escaneo de Greenbone Vulnerability Management (GVM), un marco de software de varios servicios y herramientas que ofrecen escaneo y gestión de vulnerabilidades informáticas. 

## 3. Comparación técnica

Aquí se analizarán las diferencias en el funcionamiento, detección de vulnerabilidades y rendimiento de cada herramienta.

### 3.1. Funcionamiento

- **Nessus**: Es más fácil de usar ya que en dos clics y poniendo la IP y dandole a Launch ya estás escaneando. No tienes que perder tiempo configurando cosas raras, lo cual es bueno si solo quieres resultados rápidos.

- **OpenVAS**: Es un poco más difícil ya que hay que configurar los 'targets', luego crear un 'task' y después lanzarlo. No es que sea imposible, pero si vienes de algo más simple como Nessus, se siente más pesado.

### 3.2. Detección de vulnerabilidades

- **Nessus**: Supuestamente tiene una base de datos más amplia en cuanto a vulnerabilidades, pero en nuestra experiencia, al escanear las mismas máquinas con OpenVAS, Nessus encontró menos problemas. Aun así, crea muy buenos informes.

- **OpenVAS**: Cuenta con una amplia base de datos de vulnerabilidades de código abierto, aunque su detección debería de ser inferior a Nessus en escenarios empresariales. Un punto en contra de openvas es que categoriza el reporte en high, medium y low. Nessus pone las critical para poder organizar mejor las vulnerabilidades como los CVE.

### 3.3. Rendimiento

- **Nessus**: Es mucho más personalizable y tarda mucho menos en escanear. Sirve para resultados rápidos sin tanta espera. A parte gasta menos recursos del sistema y va más rapido.

- **OpenVAS**: Es más exigente en procesamiento y almacenamiento por la actualización constante de sus vulnerabilidades. Pero aún así nos ha dado más vulnerabilidades sobre la máquina

## 4. Licenciamiento

- **Nessus**: Licencia comercial con una versión gratuita limitada (Nessus Essentials).

- **OpenVAS**: Totalmente gratuito y de código abierto, con una versión empresarial (Greenbone Security Manager).

## 5. Casos de uso

- **Nessus**: Empresas que requieren una solución comercial robusta con soporte y actualizaciones constantes.

- **OpenVAS**: Es para cuando se prefiera una opción gratuita y personalizable sin costos de licencia.

## 6. Conclusión

Nessus es mucho más rápida e intuitiva, pero su versión completa es de pago. OpenVAS su version es totalmente gratuita. Es mucho más lento, pero es más detallado en el reporte. Su interfaz es mucho menos intuitiva y hace falta más configuración para empezar a escanear.

---

Documento redactado por el Grupo 3, compuesto por:

- Israel Valderrama  
- Alejandro Seoane  
- Víctor Jiménez  
- Nicolas Ruiz  
- Alejandro Díaz

