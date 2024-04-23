import java.util.Scanner;


public class App {
    public static void main(String[] args) throws Exception {
        Scanner tScanner = new Scanner(System.in);
        System.out.println("Digite a nota 1: ");
        double nota1 = tScanner.nextDouble();
        System.out.println("Digite a nota 2: ");
        double nota2 = tScanner.nextDouble();
        System.out.println("Digite a nota 3: ");
        double nota3 = tScanner.nextDouble();
        tScanner.close();
        Avaliacao avaliacao1 = new Avaliacao(nota1,nota2,nota3);

        System.out.printf("Média Aritmética: %.2f \n", avaliacao1.calcMedAritmética());
        System.out.printf("Média ponderada: %.2f \n",avaliacao1.calcMedPonderada());
        
    }
}
