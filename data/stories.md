## busqueda solicitud datos cuenta
* saludo
  - utter_saludo
* solicitud_datos_cuenta{"numero_cuenta": 101177447}
  - accion_obtener_datos_usuario
* despedida
  - utter_despedida

## busqueda solicitud datos cuenta + pedir cuenta
* saludo
  - utter_saludo
* solicitud_datos_cuenta
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_obtener_datos_usuario
* despedida
  - utter_despedida

## Reclamos + pedir cuenta
* saludo
  - utter_saludo
* reclamo_valor_factura{"costo": false}
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_alto_costo
* despedida
  - utter_despedida

## Solicitud Copia de Factura
* saludo
  - utter_saludo
* solicitud_factura{"copia": "copia"}
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_solicitud_factura
* despedida
  - utter_despedida

## Reclamos
* saludo
  - utter_saludo
* reclamo_valor_factura{"numero_cuenta": 101177242, "costo": false}
  - accion_alto_costo
* despedida
  - utter_despedida

## Reclamos sin Saludo + pedir cuenta
* reclamo_valor_factura{"costo": false}
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_alto_costo
* despedida
  - utter_despedida

## Reclamos Sin Saludo
* reclamo_valor_factura{"numero_cuenta": 101177242, "costo": false}
  - accion_alto_costo
* despedida
  - utter_despedida


## informacion factura + valor a pagar + pedir cuenta
* saludo
  - utter_saludo
* explicacion_factura
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_valor_a_pagar
* despedida
  - utter_despedida

## informacion factura + valor a pagar
* saludo
  - utter_saludo
* explicacion_factura{"numero_cuenta": 101177242}
  - accion_valor_a_pagar
* despedida
  - utter_despedida

## informacion factura Sin Saludos + valor a pagar + pedir cuenta
* explicacion_factura
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_valor_a_pagar
* despedida
  - utter_despedida

## informacion factura + valor a pagar Sin Saludo
* explicacion_factura{"numero_cuenta": 101177242}
  - accion_valor_a_pagar
* despedida
  - utter_despedida

## informacion financiaciones Productos + pedir cuenta
* saludo
  - utter_saludo
* explicacion_financiaciones{"financiacion": "credito"}
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_financiacion_productos
* despedida
  - utter_despedida

## informacion financiaciones Productos
* saludo
  - utter_saludo
* explicacion_financiaciones{"numero_cuenta": 101177242, "financiacion": "credito"}
  - accion_financiacion_productos
* despedida
  - utter_despedida

## informacion financiaciones Productos + pedir cuenta Sin Saludo
* explicacion_financiaciones{"financiacion": "credito"}
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_financiacion_productos
* despedida
  - utter_despedida

## informacion financiaciones Productos Sin Saludo
* explicacion_financiaciones{"numero_cuenta": 101177242, "financiacion": "credito"}
  - accion_financiacion_productos
* despedida
  - utter_despedida

## informacion de pagos + pedir cuenta
* saludo
  - utter_saludo
* pagos_realizados{"pago": "cancelado"} 
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_informacion_pagos
* despedida
  - utter_despedida

## informacion de pagos
* saludo
  - utter_saludo
* pagos_realizados{"numero_cuenta": 101177242, "pago": "cancelado"}
  - accion_informacion_pagos
* despedida
  - utter_despedida

## informacion de pagos + pedir cuenta Sin Saludo
* pagos_realizados{"pago": "cancelado"} 
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_informacion_pagos
* despedida
  - utter_despedida

## informacion de pagos Sin Saludo
* pagos_realizados{"numero_cuenta": 101177242, "pago": "cancelado"}
  - accion_informacion_pagos
* despedida
  - utter_despedida

## informacion de pqrs + pedir cuenta
* saludo
  - utter_saludo
* informacion_pqrs_interpuestos{"pqr": "queja"} 
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_informacion_pqrs
* despedida
  - utter_despedida

## informacion de pqrs
* saludo
  - utter_saludo
* informacion_pqrs_interpuestos{"numero_cuenta": 101177242, "pqr": "queja"}
  - accion_informacion_pqrs
* despedida
  - utter_despedida

## informacion de pqrs + pedir cuenta Sin Saludo
* informacion_pqrs_interpuestos{"pqr": "queja"} 
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_informacion_pqrs
* despedida
  - utter_despedida

## informacion de pqrs Sin Saludo
* informacion_pqrs_interpuestos{"numero_cuenta": 101177242, "pqr": "queja"}
  - accion_informacion_pqrs
* despedida
  - utter_despedida


## informacion de Aliados Comerciales
* saludo
  - utter_saludo
* informacion_aliados_comerciales{"accion": "hacer"}
  - forma_aliados_comerciales
  - form{"name": "forma_aliados_comerciales"}
  - form{"name": null}
  - utter_pedir_cuenta
* cuenta{"numero_cuenta": 101177242}
  - accion_aliados_comerciales
* despedida
  - utter_despedida