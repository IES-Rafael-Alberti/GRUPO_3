id: proyecto2_brs
title: Guía de Segmentación de Red
description: Guía de segmentación de red creando distintas VLANS con el método router-on-a-stick.
author: Israel Valderrama García, Alejandro Seoane, Víctor Jiménez.
summary: Codelab de guía de segmentación de red
categories: codelab, markdown
environments: Web
status: Published

# Proyecto2 - BRS


## Introducción

G3Ciber es una empresa especializada en brindar soluciones de ciberseguridad avanzadas y personalizadas para proteger la infraestructura digital de sus clientes. Con un enfoque en la protección de datos, la prevención de ataques cibernéticos y la seguridad de redes, G3Ciber se posiciona como un líder en el sector, ofreciendo servicios que aseguran un entorno digital confiable y resiliente.

En su infraestructura de red, G3Ciber utiliza un esquema de cinco VLANs (Redes de Área Local Virtual), lo cual permite una segmentación eficaz del tráfico y refuerza la seguridad interna. Cada VLAN tiene un propósito específico para optimizar la eficiencia y minimizar los riesgos asociados con posibles amenazas internas y externas. Este enfoque segmentado facilita el control y la protección de datos sensibles, la gestión de accesos y la capacidad de responder rápidamente ante incidentes de seguridad.

Con esta arquitectura robusta y bien segmentada, G3Ciber se dedica a ofrecer soluciones seguras, confiables y adaptadas a las necesidades actuales de seguridad informática.

## Planificación y definición de VLANS




## Sentido de la segmentación
### ¿Por qué hemos segmentado la red?
### Coherencia con funcionalidad y seguridad

## Calcular el direccionamiento de las ip de cada VLANS
### Tabla de direcionamiento
## Configuración Packet Tracer
### Configuración de las VLANS en los switches

Como tenemos las vlans 10 de Desarrollo,20 de Ciber, 30 de Marketing, 40 de RRHH, 50 de Dirección en los siguientes comandos de packet tracer deberiamos sustituir `{NUMERO_VLAN}`por el número en concreto de la vlan. Y para el nombre deberiamos hacer lo mismo donde pone `{NOMBRE_VLAN}`

```cisco
enable

configure terminal

vlan {NUMERO_VLAN}

name {NOMBRE_VLAN}

exit
```


### Configuración de enrutamiento con router-on-a-stick



## Validación y pruebas finales

Poner los PCs en modo DHCP para que cojan las IPs de su VLAN correspondiene.

Comprobamos que hace ping de un equipo al otro de otro departamento.

PC1-Ciber a PC2-RRHH:

![imagen]()

PC2-Desarrollo a PC2-Dirección:

![imagen]()

PC2-Marketing a PC1-Ciber

![imagen]()