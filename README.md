# Mobile-Driven Purchase Behavior Analysis

A short exploratory data analysis (EDA) project exploring how mobile usage habits relate to online shopping behavior.

---

## 🎯 Objetivo

Entender cómo los hábitos de uso de dispositivos móviles impactan el comportamiento de compra online para informar decisiones de producto, personalización y estrategia de notificaciones.

---

## 📦 Datasets

1. **Ecommerce User Behavior Data**  
   – Source: Hugging Face  
   – Link: https://huggingface.co/datasets/jin-ying-so-cute/ecommerce-user-behavior-data  
   – Contiene ~35 M registros de interacciones en un e-commerce (vistas, carrito, compra, favoritos), con timestamp y categoría de producto.

2. **Mobile Device Usage & User Behavior**  
   – Source: Kaggle  
   – Link: https://www.kaggle.com/datasets/valakhorasani/mobile-device-usage-and-user-behavior-dataset  
   – Incluye tiempo diario en apps (redes, juegos, compras), notificaciones, número de apps instaladas y datos demográficos (edad, género, país, SO).


---

## ❓ Hipótesis (tentativas)

- **Tiempo en apps de compra ↔ volumen de compras**  
  ¿Los usuarios que pasan más tiempo en apps de compras registran un mayor número de compras en el e-commerce?

- **Notificaciones diarias ↔ tasa de conversión**  
  ¿El número de notificaciones recibidas al día está relacionado con el ratio de conversión (vistas → compras)?

- **Demografía y conversión**  
  ¿Influyen la edad o el género en la probabilidad de convertir una vista en compra?

- **Perfiles de carrito abandonado**  
  ¿Existen segmentos de usuarios que añaden muchos productos al carrito pero no finalizan la compra? ¿Cómo se definen sus patrones de uso móvil?

- **Sincronía horaria de uso y compra**  
  ¿Se solapan las horas de mayor actividad en el móvil con las horas pico de compra online?