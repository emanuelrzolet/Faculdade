import java.util.ArrayList;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");
        Computador desktop1 = new Desktop(8, 4, 1);
        Computador Notebook1 = new Notebook(8, 8, 20);

        ArrayList<Computador> listaComputadores =  new ArrayList<>();
        listaComputadores.add(Notebook1);
        listaComputadores.add(desktop1);
        for (Computador computador : listaComputadores) {
            System.out.println(computador.calculaValor());
            System.out.println(computador.toString());            
        }
        System.out.println(desktop1.calculaValor());
        System.out.println(desktop1.toString());
    }
}
