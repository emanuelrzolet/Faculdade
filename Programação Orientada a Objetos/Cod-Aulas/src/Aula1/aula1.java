package Aula1;
import java.util.Scanner;

public class aula1 {
    public static void main(String[] args) {
        System.out.println("Olá mundo!");
        //Declaração das Variáveis
        String nome = "Mario"; 
        int idade = 10;
        double peso = 72.5;
        //Entrada de Dados
        Scanner tScanner = new Scanner(System.in);
        System.out.println("Digite a idade: ");
        idade = tScanner.nextInt();
        System.out.println("Digite o peso: ");
        peso = tScanner.nextDouble();
        System.out.println("Digite o nome: ");
        nome = tScanner.next();
        //Tratamento de Strings:
        System.out.println("Nome: " + nome);
        System.out.printf("Idade: %d\n", idade);
        System.out.printf("Peso: %.2f", peso);

        // Condicional
        if (idade < 18) {
            System.out.println("Acesso bloqueado");
        }
        else if(idade < 65){System.out.println("Adulto");}
        else{System.out.println("Adulto idoso");}
        // While
        while (idade > 999) {
            System.out.println("Digite uma idade valida!");
            
        }
        // For
        for(int i=0; i<10; i++){
            System.out.println(idade + i);
        }

        //Array
        int numeros[] = new int[200];//Criado array vazia
        System.out.println(numeros);
        int megaSena[] = {11,14,21,30,37,4,56};
        System.out.println(megaSena[0]);

    }

}
