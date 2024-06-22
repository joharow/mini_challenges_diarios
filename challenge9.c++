#include <iostream>

int main() {
    // Declarar las variables para almacenar los números
    int numero1, numero2, suma;

    // Pedir al usuario que introduzca el primer número
    std::cout << "Introduce el primer número: ";
    std::cin >> numero1;

    // Pedir al usuario que introduzca el segundo número
    std::cout << "Introduce el segundo número: ";
    std::cin >> numero2;

    // Sumar los dos números
    suma = numero1 + numero2;

    // Mostrar el resultado de la suma
    std::cout << "La suma de " << numero1 << " y " << numero2 << " es " << suma << std::endl;

    return 0;
}
