package Aula1;

import java.util.Scanner;

public class Imc {
    public static void main(String[] args) {
        Scanner tScanner = new Scanner(System.in);
        int peso;
        double altura;
        System.out.println("Digite seu peso: ");
        peso = tScanner.nextInt();
        System.out.println("Digite sua altura: ");
        altura = tScanner.nextDouble();
        double imc = peso / (altura * altura);
        System.out.printf("Seu IMC é: %.2f", imc);


    }

}
