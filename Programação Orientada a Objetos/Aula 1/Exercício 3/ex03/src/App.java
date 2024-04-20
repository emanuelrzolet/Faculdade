import java.util.ArrayList;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        //int [] megaSena = {10,20,30,40,50,60};
        //megaSena[0] = 1;
        //ArrayList
        Scanner fScanner = new Scanner(System.in);
        ArrayList<String> listaNomes = new ArrayList<String>();
        ArrayList<Integer> megaSena = new ArrayList<Integer>();
        System.out.println("Digite a quantidade de nomes:");
        int quantidade = fScanner.nextInt();

        for(int i=0; i < quantidade; i++){
            String nome = fScanner.next();

            listaNomes.add(nome);
        }

        for(int i = listaNomes.size() -1; i >= 0; i--){
            System.out.println(listaNomes.get(i));
        }

    }
}
