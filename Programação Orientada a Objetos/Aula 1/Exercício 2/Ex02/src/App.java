import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner tScanner = new Scanner(System.in);
        System.out.println("Ajude leonidas a adivinhar quantos soldados os espartanos irão enfrentar: ");
        int numero = tScanner.nextInt();
        while (numero != 10000) {
            if (numero < 10000) {
                System.out.println("Errou o número de soldados é maior!");
                
            }
            else if (numero > 10000){
                System.out.println("Errou, o número de soldados é menor!");
            }
            else{
                System.out.println("Você Acertou!!");
                break;
            }
            System.out.println("Tente novamente, digite quantos soldados: ");
            numero = tScanner.nextInt();
            
            System.out.println(numero);
            if (numero == 10000) {
                System.out.println("Você Acertou!!");
                break;
    
            }
        }
    }
}
