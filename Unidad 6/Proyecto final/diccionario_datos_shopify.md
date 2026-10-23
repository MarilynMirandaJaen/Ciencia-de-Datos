| Campo | Tipo de Dato | Longitud | Clave | Nulo | Descripción |
| ----- | ------------ | -------- | ----- | ---- | ----------- |
| `order_id` | INT | 5 | PK | NO | Identificador de la orden |
| `order_date` | DATE | 10 | | NO | Fecha de la orden |
| `customer_id` | INT | 5 | FK | NO | Identificador del cliente |
| `product_id` | INT | 4 | FK | NO | Identificador del producto |
| `product_category` | VARCHAR | 11 | | NO | Categoría del producto |
| `product_price` | DECIMAL(5,2) | 5 | | NO | Precio de lista del producto |
| `discount_percent` | INT | 2 | | NO | Porcentaje de descuento aplicado |
| `quantity` | INT | 1 | | NO | Cantidad de unidades compradas |
| `customer_country` | VARCHAR | 9 | | NO | País del cliente |
| `traffic_source` | VARCHAR | 12 | | NO | Canal de origen de la compra |
| `payment_method` | VARCHAR | 16 | | NO | Método de pago |
| `shipping_cost` | DECIMAL(4,2) | 4 | | NO | Costo de envío |
| `rating` | DECIMAL(2,1) | 2 | | NO | Calificación del cliente |
| `is_returned` | TINYINT | 1 | | NO | Indica si la orden fue devuelta (1 = sí, 0 = no) |
| `discounted_price` | DECIMAL(5,2) | 5 | | NO | Precio unitario con descuento |
| `revenue` | DECIMAL(6,2) | 6 | | NO | Ingreso de la orden (precio con descuento x cantidad) |
| `profit` | DECIMAL(6,2) | 6 | | NO | Utilidad de la orden (ingreso - costo de envío) |
| `return_date` | DATE | 10 | | SÍ | Fecha de la devolución |
| `return_reason` | VARCHAR | 23 | | SÍ | Motivo de la devolución |
| `refund_status` | VARCHAR | 12 | | SÍ | Estado del reembolso |
| `days_to_return` | INT | 2 | | SÍ | Días entre la orden y la devolución |
