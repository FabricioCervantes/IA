# Tarea 6

```python
def sobreviviente(total_soldados, salto):
    if total_soldados == 1:
        return 1
    else:
        return (sobreviviente(total_soldados - 1, salto) + salto - 1) % total_soldados + 1

print(sobreviviente(41, 2))
```


La función `sobreviviente(total_soldados, salto)` resuelve el problema de Josephus, determinando la posición en la que el primer soldado debe sentarse para ser el último sobreviviente.

- **Caso Base:** Si solo hay un soldado (`total_soldados == 1`), devuelve la posición 1.
- **Caso Recursivo:** Si hay más de un soldado, realiza una llamada recursiva con un soldado menos y el mismo valor de salto. Luego, ajusta la posición resultante mediante operaciones módulo y suma.
- La llamada final con `total_soldados = 41` y `salto = 2` imprime la posición del último sobreviviente.
