# Proyecto 7: Attacking Enterprise Networks - Acuerdo de auditoría

**Código**: P7

**Nombre**: Attacking Enterprise Networks

**Equipo de pentesting**: Grupo 3

**Fecha**: 24/04/2025

## Índice

1. [Información general](#1-información-general)
2. [Sistemas a auditar](#2-sistemas-a-auditar)
3. [Alcance](#3-alcance)
4. [Limitaciones](#4-limitaciones)
5. [Periodo de ejecución](#5-periodo-de-ejecución)
6. [Equipo responsable](#6-equipo-responsable)
7. [Consideraciones legales y éticas](#7-consideraciones-legales-y-éticas)

## 1. Información general

Este documento establece el acuerdo entre el equipo de pentesting y la empresa **_CyberSecPro S.A._** para revisar la seguridad de sus sistemas. Esto va a permitir identificar, explotar y mitigar vulnerabilidades, para robustecer la infraestructura.

## 2. Sistemas a auditar

Se auditarán los siguientes sistemas:

| Nombre          | Sistema operativo      | Dirección IP (oculta por privacidad) | Auditor                  |
| --------------- | ---------------------- | ------------------------------------ | ------------------------ |
| PC1             | Windows Vista (64-bit) | 192.168.68.8                         | Alejandro Seoane         |
| PC2 - symfonos1 | Debian (64-bit)        | 10.10.10.7                           | Nicolas Ruiz             |
| PC3 - Durian    | Debian (64-bit)        | 10.10.20.5                           | Alejandro Diaz           |
| PC4 - solstice  | Debian (64-bit)        | 10.10.10.4                           | Israel Valderrama        |
| PC5 - Corrosion | Ubuntu (64-bit)        | 10.10.30.4                           | Victor Jimenez           |

## 3. Alcance

La prueba se realizarán en los siguientes dominios y rangos de red:

- "External" facing target host: 192.168.68.166
- Rango de red interno: 10.10.10.0/24
- Rango de red interno: 10.10.20.0/24
- Rango de red interno: 10.10.30.0/24

Se permiten técnicas de prueba automatizadas, como la enumeración y el escaneo de vulnerabilidades, siempre y cuando no causen interrupciones del servicio.

## 4. Limitaciones

Las limitaciones existentes a la hora de realizar la evaluación son las siguientes:

- Phishing / Ingeniería social.
- Acciones destructivas o pruebas de Denegación de Servicio (DoS).
- Modificaciones en el entorno sin el consentimiento escrito del personal de TI autorizado.

## 5. Periodo de ejecución

Las pruebas se realizaran en un plazo de 72 horas, pudiéndose realizar las 24 horas del día, pero se solicita que cualquier escaneo de vulnerabilidades pesadas se realice fuera del horario laboral regular (después de las 19:00 hora de Cádiz).

## 6. Equipo responsable

El equipo de pentesting está formado por Grupo 3 de la especialización en Ciberseguridad del IES Rafael Alberti, actuando bajo el rol de consultores de seguridad. Los integrantes son los siguientes:

- Víctor Jiménez Corada, <vjimcor955@g.educaand.es>
- Israel Valderrama García, <ivalgar260@g.educaand.es>
- Alejandro Seoane Martínez, <aseomar110@g.educaand.es>
- Alejandro Díaz Barea, <adiabar0510@g.educaand.es>
- Nicolas Ruiz Ruiz, <nruirui214@g.educaand.es>

## 7. Consideraciones legales y éticas

Se cuenta con un documento de Alcance de Trabajo (SoW) firmado por ambas empresas y un miembro autorizado del departamento de TI de FortifyShield Inc., así como un documento de Reglas de Compromiso (RoE) firmado por la empresa y el cliente.

Fdo empresa:

| Firma de la empresa |
| ------------------- |
| CyberSecPro S.A.    |

Fdo Equipo de pentesting:

<img src="img/victorSignWhite.png" alt="firma victor" width="150"/>
<img src="img/israelSignWhite.png" alt="firma Isra" width="200"/>
